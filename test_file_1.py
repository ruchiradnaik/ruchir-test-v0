import pandas as pd
import numpy as np

# Create a DataFrame with some data
data = {'numbers': [1, 2, 3, 4, 5], 'squares': [1, 4, 9, 16, 25]}
df = pd.DataFrame(data)

# Calculate mean of numbers column
mean_value = df['numbers'].mean()

# Print results
print(f"Mean of numbers: {mean_value}")
print(f"DataFrame shape: {df.shape}")

# Fix the error by calculating the sum of cubes using the existing 'numbers' column
result = (df['numbers'] ** 3).sum()  # Calculate sum of cubes
print(f"Sum of cubes: {result}")

# CodeSentinal: created for you by RuchirAdnaik.