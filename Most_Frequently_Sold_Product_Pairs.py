import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code
# Group products by Date
grouped = df.groupby("Date")["Product"].apply(list)

# Generate product pairs for each date
pair_counter = Counter()

for products in grouped:
    unique_products = list(set(products))
    pairs = combinations(sorted(unique_products), 2)
    pair_counter.update(pairs)

# Find the highest frequency
max_count = max(pair_counter.values())

# Get all pairs with highest frequency
most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

# Output the most frequent product pairs
for p1, p2 in most_frequent_pairs:
    print(f"{p1} and {p2}: {max_count} times")