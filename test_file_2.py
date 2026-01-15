import torch
import numpy as np

# Create tensors
tensor_a = torch.tensor([1.0, 2.0, 3.0, 4.0])
tensor_b = torch.tensor([5.0, 6.0, 7.0, 8.0])

# Perform operations
sum_tensor = tensor_a + tensor_b
product_tensor = tensor_a * tensor_b

print(f"Sum: {sum_tensor}")
print(f"Product: {product_tensor}")

# Fixing the shape mismatch error by creating a tensor with the same shape as tensor_a
tensor_c = torch.tensor([1.0, 2.0, 3.0, 4.0])  # Same shape as tensor_a
result = tensor_a + tensor_c  # Now this will work
print(f"Result: {result}")

# CodeSentinal: created for you by RuchirAdnaik.