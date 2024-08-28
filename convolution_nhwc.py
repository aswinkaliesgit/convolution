import torch
import torch.nn as nn
import numpy as np

input_channels = 64
output_channels = 128
input_height = 112
input_width = 112
K_H = 3
K_W = 3

# Create input tensor a and filter tensor b
a = np.zeros((input_channels, input_height, input_width))
b = np.zeros((output_channels, input_channels, K_H, K_W))

# Initialize input tensor values
for k in range(input_channels):
    for i in range(input_height):
        for j in range(input_width):
            a[k, i, j] = i * input_width + j + 1

# Initialize filter tensor values
for c in range(output_channels):
    for k in range(input_channels):
        for l in range(K_H):
            for m in range(K_W):
                b[c, k, l, m] = k * K_H * K_W + l * K_W + m + 1

# Convert to PyTorch tensors
a_torch = torch.tensor(a, dtype=torch.float32).unsqueeze(0)  # Add batch dimension
b_torch = torch.tensor(b, dtype=torch.float32)

# Define convolutional layer
conv = nn.Conv2d(
    in_channels=input_channels,
    out_channels=output_channels,
    kernel_size=(K_H, K_W),
    padding=(1, 1),
    stride=(2,2),
    bias=False
)

# Set weights for the convolutional layer
with torch.no_grad():
    conv.weight = nn.Parameter(b_torch)

# Perform the convolution
output = conv(a_torch)

# Convert the output tensor to a NumPy array (detach the tensor first)
output_np = output.detach().numpy()

# Write the output tensor to a binary file
with open('outputpy.bin', 'wb') as f:

    # Write data
    f.write(output_np.tobytes())

print("Output tensor written to outputpy.bin")
