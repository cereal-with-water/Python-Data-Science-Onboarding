import numpy as np
import pandas as pd

def _fail(msg):
    raise AssertionError(msg)

# Numpy
def check_array(arr, shape=None, dtype=None, allow_int_any=False):
    if not isinstance(arr, np.ndarray):
        _fail(f"❌ Expected numpy.ndarray, got {type(arr)}")
    if shape is not None and arr.shape != shape:
        _fail(f"❌ Wrong shape: expected {shape}, got {arr.shape}")
    if dtype is not None:
        if allow_int_any and np.issubdtype(arr.dtype, np.integer):
            pass
        elif not np.issubdtype(arr.dtype, dtype):
            _fail(f"❌ Wrong dtype: expected {dtype}, got {arr.dtype}")
    print("✅ Array check passed.")

def check_value(val, expected, tol=1e-8):
    if isinstance(val, (float, np.floating)) or isinstance(expected, (float, np.floating)):
        if abs(float(val) - float(expected)) > tol:
            _fail(f"❌ Wrong value: expected {expected}, got {val}")
    else:
        if val != expected:
            _fail(f"❌ Wrong value: expected {expected}, got {val}")
    print("✅ Value check passed.")

# pandas
def check_dataframe_columns(df, expected_cols):
    if not isinstance(df, pd.DataFrame):
        _fail(f"❌ Expected pandas.DataFrame, got {type(df)}")
    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        _fail(f"❌ Missing columns: {missing}")
    print("✅ DataFrame columns check passed.")

def check_series_index_values(s, expected_index_set):
    if not isinstance(s, pd.Series):
        _fail(f"❌ Expected pandas.Series, got {type(s)}")
    if set(list(s.index)) != set(list(expected_index_set)):
        _fail(f"❌ Unexpected index: got {list(s.index)}, expected set {list(expected_index_set)}")
    print("✅ Series index check passed.")

def check_len(obj, expected_len):
    try:
        n = len(obj)
    except Exception as e:
        _fail(f"❌ Object has no len(): {e}")
    if n != expected_len:
        _fail(f"❌ Wrong length: expected {expected_len}, got {n}")
    print("✅ Length check passed.")
