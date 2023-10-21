# We have more than 300k svgs in one dataset so we will simply lazy caption them.

import pandas as pd

# Load the CSV file into a DataFrame
csv_path = '../dataset/svgrepo_modified_reordered.csv'
df = pd.read_csv(csv_path)

# Add a new column 'description' based on the 'input' column
df['description'] = 'Icon of ' + df['input']

# Save the modified DataFrame back to a new CSV file
output_csv_path = '../dataset/svgrepo_modified_with_description.csv'
df.to_csv(output_csv_path, index=False)
