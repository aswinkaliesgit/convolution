#!/bin/bash
# Compile the C++ code
g++ convolution_nchw.cpp -o convolution_nchw
# Execute the compiled program
./convolution_nchw
# Run the Python script for convolution
python3 convolution_nchw.py
# Compare the outputs
python3 compare.py 