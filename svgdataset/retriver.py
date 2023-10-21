import pandas as pd
import numpy as np
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Function to fetch SVG data with retry mechanism


def fetch_svg(url, max_retries=3):
    retries = 0
    while retries <= max_retries:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                retries += 1
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            retries += 1
    return None

# Function to process each small DataFrame


def process_df(small_df):
    output = []
    for url in tqdm(small_df['icon-src'], desc='Fetching SVGs', leave=False):
        output.append(fetch_svg(url))
    small_df['output'] = output
    return small_df


# Read the main DataFrame
df = pd.read_csv('../dataset/svgrepo-raw.csv')

# Automatically get the number of cores
num_cores = os.cpu_count()

# Split the DataFrame into smaller DataFrames
dfs = np.array_split(df, num_cores)

# Perform parallel processing
with ThreadPoolExecutor(max_workers=num_cores) as executor:
    results = list(tqdm(executor.map(process_df, dfs),
                   total=len(dfs), desc='Processing DataFrames'))

# Concatenate the results into a single DataFrame
final_df = pd.concat(results, ignore_index=True)

# Save the updated DataFrame
final_df.to_csv('../dataset/svgrepo.csv', index=False)
