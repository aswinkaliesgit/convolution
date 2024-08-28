#!/bin/bash
# Compile the C++ code
g++ convolution_nhwc.cpp -o convolution_nhwc
# Execute the compiled program
./convolution_nhwc
# Run the Python script for convolution
python3 convolution_nhwc.py
# Compare the outputs
python3 compare_nhwc.py