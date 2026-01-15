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

# Fixing the error by calculating the sum of squares instead of a non-existent cubes column
result = df['squares'].sum()  # Changed 'cubes' to 'squares'
print(f"Sum of squares: {result}")

# CodeSentinal: created for you by RuchirAdnaik.