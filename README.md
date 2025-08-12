# Python-Data-Science-Onboarding

Welcome to the WMU DSC/Developer Club!<br>
This repository is designed to help new members get familiar with the tools and workflows commonly used in our data science projects.
<br>
<br>



## 🚀 Who is this for?

This tutorial assumes you already have *basic Python knowledge*, including:

- Using numpy and pandas for data handling  
- Knowing what a .ipynb Jupyter Notebook file is  
- Using scikit-learn to build simple machine learning models

<details>
<summary><b>❓Don't know Python yet? No problem!❓</b></summary>
<br>

>  **Start with the resources below before continuing:**<br>
> &emsp;&emsp;[W3Schools Python Tutorial](https://www.w3schools.com/python/)  
> &emsp;&emsp;[Google's Python Class](https://developers.google.com/edu/python)  
> &emsp;&emsp;[Python for Beginners (YouTube)](https://www.youtube.com/watch?v=K5KVEU3aaeQ&t=56s)  
</details>


<details>
<summary> <b>❓Python Installation Guide For Beginners❓</b></summary>
<br>
  
> ### To follow along with the notebooks in this repository, you need Python installed on your machine.
> ### 🎥 How to Install Python
> &emsp;&emsp;  [For macOS](https://www.youtube.com/watch?v=nhv82tvFfkM)  
> &emsp;&emsp;  [For Windows](https://www.youtube.com/watch?v=YagM_FuPLQU)<br><br>
> 📌 *Important*: During installation, make sure to check:  
>  *“Add Python to PATH”*

###  Verify Your Installation

After installing, open a terminal (or Command Prompt on Windows), and run:

```bash
python --version
pip --version
```
</details>
<br>
<br>



## 📦 Recommended Libraries

In Python, you install packages by running:
```bash
pip install <package-name>
```

Before you dive into the notebooks, make sure you have the core data-science libraries installed. You can install them all at once via pip:

```bash
pip install \
  numpy \
  pandas \
  matplotlib \
  seaborn \
  scikit-learn \
  notebook
```
<br>
<br>



## 📘 Core Topics

<details>
<summary> <b>🔥Data Handling with NumPy & Pandas🔥</b></summary>
 Learn how to load, clean, and manipulate data using NumPy arrays and Pandas DataFrames.

## 🔍 Library Overview

Before we dive in, here's a quick intro to the two core libraries we’ll use:

###  NumPy
- **The fundamental package for numerical computing in Python.**
- **Key features:**
  - **Arrays:** Homogeneous, N-dimensional arrays (faster and more memory-efficient than Python lists)  
  - **Vectorized ops:** Element-wise arithmetic without explicit loops  
  - **Linear algebra & random:** Built-in support for matrix operations and pseudo-random number generation  

###  Pandas
- **A powerful data analysis and manipulation library built on top of NumPy.**  
- **Key features:**
  - **DataFrame:** 2D tabular data structure with labeled axes (rows & columns)  
  - **IO tools:** Read/write CSV, Excel, SQL, JSON, and more  
  - **Series:** 1D labeled array, great for time series and single-column tables  
  - **Grouping & aggregation:** Split-apply-combine workflows for summarizing data  



### 1. What  
> **What you will learn in this section.**  
> By the end of this notebook, you will be able to:  
> - Create and manipulate NumPy arrays of different shapes and dtypes  
> - Perform element-wise arithmetic and universal functions
> - Index, slice, and reshape arrays for efficient computation  

---

### 2. Why  
> **Why this topic matters.**  
> NumPy arrays are the foundation of nearly all scientific computing in Python.  
> They provide:  
> - **Speed:** Vectorized operations run much faster than Python loops  
> - **Memory efficiency:** Compact storage of homogeneous data  
> - **Interoperability:** A common data structure for libraries like Pandas, SciPy, and scikit-learn  

---

### 3. How  
> **How to do it.**  
> Follow these step-by-step examples:

```python
import numpy as np

# 1) Create arrays
a = np.array([1, 2, 3, 4])
b = np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
c = np.zeros((2, 3), dtype=int)  # 2×3 array of zeros

# 2) Element-wise arithmetic
sum_ab = a + b[:4]               # adds element by element
prod_ab = a * b[:4]              # multiplies element by element

# 3) Universal functions
sqrt_b = np.sqrt(b)              # square root of each element
exp_a  = np.exp(a)               # eᵃ for each element

# 4) Indexing & slicing
row = b[2:5]                     # slice subarray
c[0, :] = row                    # assign a row

# 5) Reshape & combine
d = np.linspace(0, 1, 6).reshape(2, 3)
stacked = np.vstack([c, d])      # vertical stack of two 2×3 arrays


```
</details>



<details>
<summary> <b>🔥Understanding Jupyter Notebooks (.ipynb)</b>🔥</summary>
What are text vs code cells, how to run them, and best practices for documenting your analysis.
# 📝 Jupyter Notebook Quickstart Guide

This guide will introduce you to Jupyter Notebook—from “what it is” to how to install and use it locally or in the cloud—then walk you through basic operations, hands-on examples, Markdown usage, and sharing.

---

## 🔍 What Is Jupyter Notebook?

Jupyter Notebook is an interactive computing environment where you can combine live code, equations, visualizations, and narrative text in a single document (`.ipynb`). It’s widely used for data analysis, teaching, and rapid prototyping.

- **Key Features**  
  - Interactive code execution  
  - Rich text via Markdown (headings, lists, LaTeX)  
  - Inline data visualizations  
  - Easy sharing and reproducibility  

---

## ⚙️ Installation & Access

### 1. Install Locally

You’ll need Python installed first. Then:

```bash
# Install Jupyter Notebook via pip
pip install notebook
```
Or, if you use Conda:
```bash
conda install -c conda-forge notebook
```
After installation, launch the notebook server:
```bash
jupyter notebook
```
Your default browser will open at http://localhost:8888, showing the notebook dashboard.

### 2. Use JupyterLab (Optional)
For a more full-featured interface:

```bash
pip install jupyterlab
jupyter lab
```
### 3. Cloud / Web Options
Google Colab

1. Go to colab.research.google.com
2. Sign in with your Google account
3. Open or upload any .ipynb file
</details>



<details>
<summary> <b>🔥Basic Machine Learning with scikit-learn</b>🔥</summary>
  Build your first regression and classification models, split data, and evaluate performance.
</details>

---

