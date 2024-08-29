#!/bin/bash
# Compile the C++ code
g++ convolution_shape_nhwc.cpp -o convolution_shape_nhwc
# Execute the compiled program
./convolution_shape_nhwc
# Run the Python script for convolution
python3 convolution_shape_nhwc.py
# Compare the outputs
python3 compare_shape_nhwc.py