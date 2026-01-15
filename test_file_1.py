import pandas as pd
import numpy as np
import torch
import cv2

# Create a DataFrame with some data
data = {'numbers': [1, 2, 3, 4, 5], 'squares': [1, 4, 9, 16, 25]}
df = pd.DataFrame(data)

# Calculate mean of numbers column
mean_value = df['numbers'].mean()

# Print results
print(f"Mean of numbers: {mean_value}")
print(f"DataFrame shape: {df.shape}")

# Fixing the error by checking if the 'cubes' column exists before accessing it
if 'cubes' in df.columns:
    result = df['cubes'].sum()
else:
    result = 0  # or handle it as needed
print(f"Sum of cubes: {result}")

# CodeSentinal: created for you by RuchirAdnaik.