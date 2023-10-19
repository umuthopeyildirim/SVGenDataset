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


# Get first output column from dataset
df = pd.read_csv(dataset)
df = df['output']

# Convert svg to png
convertSVGtoPNG(df[0])

raw_image = Image.open('output.png').convert('RGB')

# unconditional image captioning
inputs = processor(raw_image, return_tensors="pt")

out = model.generate(**inputs, max_length=max_new_tokens)
caption = processor.decode(out[0], skip_special_tokens=True)
