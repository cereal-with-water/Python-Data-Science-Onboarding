# ✅ Checkpoint 01 — NumPy Basics

**Goal**
- Create/reshape arrays, vectorized ops, boolean masking

**Rules**
- Fill only where marked as `# TODO`
- Do not change test cells (🔒)
- Run all cells before submitting

**References**
- NumPy docs: https://numpy.org/doc/

---

```python
# 🔧 Setup
import numpy as np
import pandas as pd
from utils.grader import check_array, check_value

np.random.seed(42)
```


# Q1) Create a 3x3 array with values 0..8 (row-major)
# TODO: assign to variable 'A'
A = ...  # TODO

# 🔒 Test
check_array(A, shape=(3,3), dtype=np.integer)
check_value(A.sum(), 36)

# Q2) From A, create a boolean mask selecting even numbers
# TODO: assign to variable 'mask_even'
mask_even = ...  # TODO

# 🔒 Test
check_array(mask_even, shape=(3,3), dtype=bool)
check_value(int(mask_even.sum()), 5)  # number of evens in 0..8

# Q3) Reshape, stack, and compute row-wise means → 'means'
# TODO: assign to variable 'means' (1D array length 3)
B = ...  # TODO
means = ...  # TODO

# 🔒 Test
check_array(means, shape=(3,))


# Q4) Broadcasting: A (3x3) and v (1x3) → 'C'
v = np.array([10, 0, -10])
C = ...  # TODO

# 🔒 Test
check_array(C, shape=(3,3), dtype=np.integer)
check_value(int(C[0,0] + C[2,2]), (A[0,0]+10) + (A[2,2]-10))


# Q5) Fancy indexing / boolean masking
# Extract odd numbers ≥ 3 from A → 'odd_ge3'
odd_ge3 = ...  # TODO

# 🔒 Test
check_array(
    odd_ge3,
    shape=(np.count_nonzero((A>=3)&(A%2==1)),),
    dtype=np.integer,
    allow_int_any=True
)
check_value(int(odd_ge3.min()), 3)
