import pandas as pd
import subprocess

# instruct-svg.csv
# Convert to CSV
# df = pd.read_parquet('dataset/instruct-svg.parquet')
# df.to_csv('dataset/instruct-svg.csv')

# Drop Image Table
# df = pd.read_csv('dataset/instruct-svg.csv')
# df = df.drop('image', axis=1)
# df.to_csv('dataset/instruct-svg.csv', index=False)

# Drop Id Table
# df = pd.read_csv('dataset/instruct-svg.csv')
# df = df.drop(df.columns[0], axis=1)
# df.to_csv('dataset/instruct-svg.csv', index=False)

# Merge description_0 and description_1 into description column and remove description_0 and description_1 column to description
# df = pd.read_csv('dataset/instruct-svg.csv')
# df['description'] = df['description_0'] + df['description_1']
# df = df.drop(['description_0', 'description_1'], axis=1)
# df.to_csv('dataset/instruct-svg.csv', index=False)

# Add source column and fill with 'instruct-svg'
# df = pd.read_csv('dataset/instruct-svg.csv')
# df['source'] = 'instruct-svg'
# df.to_csv('dataset/instruct-svg.csv', index=False)

# Add license column and fill with 'CC0'
# df = pd.read_csv('dataset/instruct-svg.csv')
# df['license'] = 'CC0'
# df.to_csv('dataset/instruct-svg.csv', index=False)


#  noto-emoji-vector-512-svg.csv
notoEmojiRaw = 'dataset/noto-emoji-vector-512-svg.parquet'
notoEmoji = 'dataset/noto-emoji-vector-512-svg.csv'

# Convert to CSV
# df = pd.read_parquet(notoEmojiRaw)
# df.to_csv(notoEmoji)

# Drop first column
# df = pd.read_csv(notoEmoji)
# df = df.drop(df.columns[0], axis=1)
# df.to_csv(notoEmoji, index=False)

# Drop Image Table
# df = pd.read_csv(notoEmoji)
# df = df.drop('image', axis=1)
# df.to_csv(notoEmoji, index=False)

# Drop codepoints column
# df = pd.read_csv(notoEmoji)
# df = df.drop('codepoints', axis=1)
# df.to_csv(notoEmoji, index=False)

# Drop text column
# df = pd.read_csv(notoEmoji)
# df = df.drop('text', axis=1)
# df.to_csv(notoEmoji, index=False)

# Drop svg_path column
# df = pd.read_csv(notoEmoji)
# df = df.drop('svg_path', axis=1)
# df.to_csv(notoEmoji, index=False)

# Rename name column to input
# df = pd.read_csv(notoEmoji)
# df = df.rename(columns={'name': 'input'})
# df.to_csv(notoEmoji, index=False)

# Rename svg_text to output
# df = pd.read_csv(notoEmoji)
# df = df.rename(columns={'svg_text': 'output'})
# df.to_csv(notoEmoji, index=False)

# Add source column and fill with 'noto-emoji'
# df = pd.read_csv(notoEmoji)
# df['source'] = 'noto-emoji'
# df.to_csv(notoEmoji, index=False)

# Add license column and fill with 'OFL'
# df = pd.read_csv(notoEmoji)
# df['license'] = 'OFL'
# df.to_csv(notoEmoji, index=False)


# svgrepo.csv
svgRepo = 'dataset/svgrepo-raw.csv'

# Drop web-scraper-order,web-scraper-start-url,collection_link-href,sub_collection_pagination,icon_show-src columns
# df = pd.read_csv(svgRepo)
# df = df.drop('web-scraper-order', axis=1)
# df = df.drop('web-scraper-start-url', axis=1)
# df = df.drop('collection_pagination', axis=1)
# df = df.drop('collection_link-href', axis=1)
# df = df.drop('sub_collection_pagination', axis=1)
# df.to_csv(svgRepo, index=False)

# !!!! NOT OPTIMIZED
# Get each icon_show-src and download it to downloadsvgs folder using wget
# df = pd.read_csv(svgRepo)
# for index, row in df.iterrows():
#     url = row['icon_show-src']
#     filename = url.split('/')[-1]
#     print('Downloading', filename)
#     subprocess.run(['wget', url, '-P', 'downloadsvgs'])

# Convert CSV to excel format
# df = pd.read_csv('dataset/svgrepo.csv')
# df.to_excel('dataset/svgrepo.xlsx', index=False)
