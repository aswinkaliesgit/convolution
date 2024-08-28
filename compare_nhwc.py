import numpy as np

def bin_to_numpy(file_path, dtype=np.float32, shape=None):
    """
    Convert a binary file to a NumPy array.

    Parameters:
    - file_path: Path to the binary file.
    - dtype: Data type of the binary data (default is np.float32).
    - shape: Shape of the array to reshape to. If None, returns a flat array.

    Returns:
    - NumPy array with the data from the binary file.
    """
    # Read binary file into NumPy array
    data = np.fromfile(file_path, dtype=dtype)

    # Reshape if shape is provided
    if shape:
        data = data.reshape(shape)

    return data

def compare_arrays(arr1, arr2, precision=4):
    """
    Compare two NumPy arrays up to a specified precision.

    Parameters:
    - arr1: First NumPy array.
    - arr2: Second NumPy array.
    - precision: Number of decimal places to compare.

    Returns:
    - Boolean indicating if the arrays are approximately equal up to the given precision.
    """
    # Round both arrays to the specified precision
    arr1_rounded = np.round(arr1, decimals=precision)
    arr2_rounded = np.round(arr2, decimals=precision)

    # Compare the rounded arrays
    are_equal = np.allclose(arr1_rounded, arr2_rounded, atol=10**-precision)

    return are_equal, arr1_rounded, arr2_rounded

# Paths to the binary files
file_path_cpp = 'outputcpp.bin'
file_path_python = 'outputpy.bin'

# Specify the dtype and shape
dtype = np.float32
shape = (128,56,56)  # Change this to your actual shape

# Convert binary files to NumPy arrays
numpy_array_cpp = bin_to_numpy(file_path_cpp, dtype=dtype, shape=shape)
numpy_array_python = bin_to_numpy(file_path_python, dtype=dtype, shape=shape)
# Compare the arrays
are_equal, rounded_array_cpp, rounded_array_python = compare_arrays(numpy_array_cpp, numpy_array_python, precision=8)

print(f"Convolution results are approximately equal up to {4} decimal places: {are_equal}")
