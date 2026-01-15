import pandas as pd
import numpy as np
import torch
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Create a DataFrame with some data
data = {'numbers': [1, 2, 3, 4, 5], 'squares': [1, 4, 9, 16, 25]}
df = pd.DataFrame(data)

# Calculate mean of numbers column
mean_value = df['numbers'].mean()

# Print results
print(f"Mean of numbers: {mean_value}")
print(f"DataFrame shape: {df.shape}")

# Fixing the error - adding a 'cubes' column to the DataFrame
df['cubes'] = df['numbers'] ** 3

# Now we can safely calculate the sum of the cubes
result = df['cubes'].sum()
print(f"Sum of cubes: {result}")

# CodeSentinal: created for you by RuchirAdnaik.