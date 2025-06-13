import os
import pandas as pd

# Ensure input path exists
input_path = "input/input.csv"
output_path = "output/cleaned_data.csv"

# Read the CSV
print(f"Reading data from {input_path}")
df = pd.read_csv(input_path)

# Basic cleaning: drop rows with any missing values
df = df.dropna()

# Trim whitespace from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Write cleaned data to CSV
df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")
