import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def _fail(msg):
    raise AssertionError(msg)

# generic/NumPy/pandas
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

def check_file_exists(path):
    if not os.path.exists(path):
        _fail(f"❌ File not found: {path}")
    print("✅ File exists.")

#  Matplotlib/Seaborn helpers for checkpoint 03 
def check_axes_instance(ax):
    if not hasattr(ax, "get_xlabel") or not hasattr(ax, "get_ylabel"):
        _fail(f"❌ Expected a Matplotlib Axes-like object, got {type(ax)}")
    print("✅ Axes instance check passed.")

def check_xlabel(ax, expected):
    label = ax.get_xlabel()
    if label != expected and expected not in label:
        _fail(f"❌ X label mismatch. Got '{label}', expected '{expected}' (or containing it).")
    print("✅ X label ok.")

def check_ylabel(ax, expected):
    label = ax.get_ylabel()
    if label != expected and expected not in label:
        _fail(f"❌ Y label mismatch. Got '{label}', expected '{expected}' (or containing it).")
    print("✅ Y label ok.")

def check_title_contains(ax, keyword):
    title = ax.get_title()
    if keyword not in title:
        _fail(f"❌ Title does not contain '{keyword}'. Got '{title}'")
    print("✅ Title contains keyword.")

def check_num_lines(ax, expected_n):
    n = len(ax.lines)
    if n != expected_n:
        _fail(f"❌ Expected {expected_n} line(s), got {n}")
    print("✅ Number of lines ok.")

def check_num_collections(ax, expected_n):
    n = len(ax.collections)
    if n != expected_n:
        _fail(f"❌ Expected {expected_n} collection(s), got {n}")
    print("✅ Number of collections ok.")

def check_num_patches(ax, expected_n):
    n = len(ax.patches)
    if n != expected_n:
        _fail(f"❌ Expected {expected_n} patch(es), got {n}")
    print("✅ Number of patches ok.")
