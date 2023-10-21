# !pip install Pillow transformers torch cairosvg pandas tqdm

from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
import cairosvg
import pandas as pd
from tqdm.notebook import tqdm
import os
import shutil
import logging

logging.basicConfig(filename='exceptions.log', level=logging.ERROR)


def initialize_transformer():
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
    model = Blip2ForConditionalGeneration.from_pretrained(
        "Salesforce/blip2-flan-t5-xl")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return processor, model, device


def copy_dataset_to_base(dataset_path):
    if not os.path.exists(dataset_path):
        shutil.copy(dataset_path, '/content/')


def save_description_to_recovery(index, description):
    with open("recovery.csv", "a") as f:
        f.write(f"{index}, {description}\n")


def get_last_processed_index():
    if os.path.exists("recovery.csv"):
        df = pd.read_csv("recovery.csv")
        return df['index'].max()
    return 0


def convert_svg_to_png(svg):
    cairosvg.svg2png(bytestring=svg, write_to='output.png',
                     output_width=128, output_height=128)


def generate_description(processor, model, device, svg):
    convert_svg_to_png(svg)
    raw_image = Image.open('output.png').convert('RGB')
    prompt = "Write a detailed description for this icon."
    inputs = processor(raw_image, prompt, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_length=512)
    description = processor.decode(out[0], skip_special_tokens=True).strip()
    return description


def update_dataset_with_descriptions(dataset, processor, model, device):
    df = pd.read_csv(dataset)
    start_index = get_last_processed_index()
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        if index <= start_index:
            continue
        try:
            svg = row['output']
            description = generate_description(processor, model, device, svg)
            df.at[index, 'description'] = description
            save_description_to_recovery(index, description)
        except Exception as e:
            logging.error(f"Exception at index {index}: {e}")
            save_description_to_recovery(index, "Exception occurred")
            break
    df.to_csv('updated_' + os.path.basename(dataset), index=False)


if __name__ == "__main__":
    processor, model, device = initialize_transformer()
    dataset = "/content/drive/MyDrive/your_path/your_dataset.csv"
    copy_dataset_to_base(dataset)
    update_dataset_with_descriptions(dataset, processor, model, device)
