import numpy as np

def check_array(arr, shape=None, dtype=None, allow_int_any=False):
    if not isinstance(arr, np.ndarray):
        raise AssertionError(f"❌ Expected numpy.ndarray, got {type(arr)}")
    if shape is not None and arr.shape != shape:
        raise AssertionError(f"❌ Wrong shape: expected {shape}, got {arr.shape}")
    if dtype is not None:
        if allow_int_any and np.issubdtype(arr.dtype, np.integer):
            pass
        elif not np.issubdtype(arr.dtype, dtype):
            raise AssertionError(f"❌ Wrong dtype: expected {dtype}, got {arr.dtype}")
    print("✅ Array check passed.")

def check_value(val, expected):
    if val != expected:
        raise AssertionError(f"❌ Wrong value: expected {expected}, got {val}")
    print("✅ Value check passed.")
