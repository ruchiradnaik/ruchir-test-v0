import pandas as pd
import numpy as np
import torch
import cv2
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

# This will cause an error - trying to access a non-existent column
result = df['cubes'].sum()  # ERROR: 'cubes' column doesn't exist
print(f"Sum of cubes: {result}")

