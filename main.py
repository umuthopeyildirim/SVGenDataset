import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import cairosvg
import pandas as pd

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")
dataset = "dataset/noto-emoji-vector-512-svg.csv"
max_new_tokens = 512


def convertSVGtoPNG(svg):
    # Convert svg to png
    cairosvg.svg2png(bytestring=svg, write_to='output.png')


# unconditional image captioning
def imageCaptioning(image):
    # Convert svg to png
    convertSVGtoPNG(image)
    # Load image
    raw_image = Image.open('output.png').convert('RGB')

    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs, max_length=max_new_tokens)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Get output svg from dataset and caption it using imageCaptioning function


def captionSVG(dataset):
    df = pd.read_csv(dataset)
    for index, row in df.iterrows():
        # progress bar
        print(index)
        # Get svg
        svg = row['output']
        # Caption svg
        caption = imageCaptioning(svg)
        # Add caption to dataframe
        df.at[index, 'caption'] = caption
    # Save dataframe to csv
    df.to_csv(dataset, index=False)


captionSVG(dataset)
