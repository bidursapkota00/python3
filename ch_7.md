# Chapter 7: Python Libraries and Maths

## 7.1 Modules, Packages and Libraries

> Discuss the difference between a Python module, package, and library. What are the different ways to import modules? [3+3 marks] (2082 Baishakh - IOE)

A **module** is a single Python file (`.py`) containing functions, classes, and variables. It is the basic unit of code organization.

A **package** is a directory containing multiple modules and an `__init__.py` file. Packages allow hierarchical structuring of modules using dot notation (e.g., `package.module`). The `__init__.py` file is executed when the package is imported and can be used to define the package's public API.

A **library** is a collection of related packages and modules bundled together to provide specific functionality (e.g., NumPy, Pandas, Requests). It is a broader, conceptual term.

```
my_library/                  # Library
├── __init__.py
├── utils.py                 # Module
├── core/                    # Package
│   ├── __init__.py
│   ├── engine.py            # Module
│   └── helpers.py           # Module
```

**Ways to import modules:**

```python
import math                     # import entire module
print(math.sqrt(16))            # access via module name

import math as m                # import with alias
print(m.pi)

from math import sqrt, pi      # import specific items
print(sqrt(25))                 # use directly without prefix

from math import *              # import everything (this is discouraged because it may cause name conflicts)
```

**Example: Custom module**

> Write a Python program that creates a custom module `mathutils.py` with functions `factorial(n)`, `is_even(n)`, and `gcd(a, b)`. Import and use this module in another script.

**mathutils.py:**

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_even(n):
    return n % 2 == 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

**main.py:**

```python
# Method 1: import module
import mathutils
print(mathutils.factorial(5))      # 120

# Method 2: import with alias
import mathutils as mu
print(mu.is_even(4))               # True

# Method 3: import specific functions
from mathutils import gcd
print(gcd(12, 8))                  # 4
```

## 7.2 The Standard Library and Library Functions

Python's standard library is a vast collection of modules included with every Python installation ("batteries included"). No external installation is needed.

**Commonly used standard library modules:**

- `math`: Mathematical functions such as `sqrt()`, `ceil()`, `floor()`, `factorial()`, and `log()`, along with constants like `pi` and `e`.
- `os`: Operating system interfaces such as `getcwd()`, `listdir()`, `mkdir()`, `path.join()`, and `remove()`.
- `sys`: System-specific parameters including `argv` (command-line args), `exit()`, `path` (module search path), and `version`.
- `datetime`: Date and time manipulation using `datetime.now()`, `timedelta`, and formatting with `strftime()`.
- `random`: Random number generation using `random()`, `randint()`, `choice()`, and `shuffle()`.
- `json`: JSON encoding and decoding using `dumps()`, `loads()`, `dump()`, and `load()`.
- `collections`: Specialized containers like `Counter`, `defaultdict`, `namedtuple`, and `deque`.
- `re`: Regular expressions using `match()`, `search()`, `findall()`, and `sub()`.
- `itertools`: Iterator tools including `chain()`, `permutations()`, `combinations()`, and `cycle()`.
- `functools`: Higher-order functions like `reduce()`, `lru_cache`, and `partial`.

```python
import math
print(math.sqrt(144))         # 12.0
print(math.factorial(6))      # 720
print(math.pi)                # 3.141592653589793

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

import random
print(random.randint(1, 100))
print(random.choice(["a", "b", "c"]))
```

## 7.3 Adding More Python Libraries

Third-party libraries are installed using pip (Python's package manager), which downloads packages from the Python Package Index (PyPI).

```bash
pip install numpy              # install a package
pip install numpy==1.24.0      # install specific version
pip install --upgrade numpy    # upgrade to latest version
pip uninstall numpy            # remove a package
pip list                       # list installed packages
pip freeze > requirements.txt  # export dependencies
pip install -r requirements.txt # install from requirements file
```

**Virtual environments** isolate project dependencies, preventing version conflicts between projects:

```bash
python -m venv myenv           # create virtual environment
myenv\Scripts\activate         # activate (Windows)
source myenv/bin/activate      # activate (Linux/macOS)
deactivate                     # deactivate
```

## 7.4 Python Frameworks

A framework provides a complete structure and set of tools for building applications. Unlike a library (which you call), a framework calls your code (Inversion of Control).

**Web development frameworks:**

- **Django**: This is a full-stack, "batteries-included" framework with an ORM, an admin panel, authentication, and templating. It is used for large, complex web applications.
- **Flask**: This is a lightweight, micro-framework with minimal built-in features. It is flexible and suitable for small to medium applications and APIs.
- **FastAPI**: This is a modern, high-performance framework for building APIs. It is based on type hints and auto-generates documentation.

**Data science and machine learning frameworks:**

- **NumPy**: This is used for numerical computing with multi-dimensional arrays.
- **Pandas**: This is used for data manipulation and analysis with DataFrames.
- **Matplotlib**: This is used for data visualization and plotting.
- **Scikit-learn**: This provides machine learning algorithms.
- **TensorFlow / PyTorch**: These are deep learning frameworks.

**Other frameworks:**

- **Tkinter**: This provides GUI development and is part of the standard library.
- **Pygame**: This is used for game development.
- **Scrapy**: This is used for web scraping.

## 7.5 Introduction to the NumPy Library

> Explain the advantages of using NumPy array over python sequences with an example. [3 marks] (2081 Ashwin - IOE)

**NumPy** (Numerical Python) is a library for efficient numerical computation. Its core object is the ndarray (N-dimensional array), a fixed-size, homogeneous container of elements of the same type.

**Advantages of NumPy arrays over Python lists:**

- **Performance**: NumPy arrays are stored in contiguous memory and implemented in C, making operations 10 to 100 times faster than Python lists.
- **Memory efficiency**: Using a fixed data type means there is less memory overhead per element compared to Python objects.
- **Vectorized operations**: These allow element-wise operations without explicit loops. For example, `arr * 2` multiplies every element, unlike lists.
- **Broadcasting**: This enables operations on arrays of different shapes without manual reshaping.
- **Built-in mathematical functions**: NumPy provides a comprehensive library for linear algebra, statistics, random numbers, and more.

```python
import numpy as np

# Python list vs NumPy array for element-wise multiplication
py_list = [1, 2, 3, 4, 5]
np_arr = np.array([1, 2, 3, 4, 5])

# List: requires loop or comprehension
result_list = [x * 2 for x in py_list]       # [2, 4, 6, 8, 10]

# NumPy: vectorized operation
result_arr = np_arr * 2                       # array([2, 4, 6, 8, 10])
```

**Installing NumPy:** `pip install numpy`

**Importing:** `import numpy as np`

## 7.6 Creating, Indexing and Slicing NumPy Arrays

> Write a program to create a NumPy array, demonstrate indexing, slicing, and copying (shallow vs deep copy). Modify the copy and show that the original array remains unchanged.

**Creating arrays:**

```python
import numpy as np

# From Python lists
a = np.array([1, 2, 3, 4, 5])                # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]])         # 2D array (2×3)

# Using built-in functions
zeros = np.zeros((3, 4))          # 3×4 array of zeros
ones = np.ones((2, 3))            # 2×3 array of ones
full = np.full((2, 2), 7)         # 2×2 array filled with 7
eye = np.eye(3)                   # 3×3 identity matrix
rng = np.arange(0, 10, 2)         # array([0, 2, 4, 6, 8])
lin = np.linspace(0, 1, 5)        # array([0., 0.25, 0.5, 0.75, 1.])
emp = np.empty((2, 3))            # uninitialized 2×3 array
```

**Array attributes:**

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)      # (2, 3) represents the dimensions
print(arr.ndim)       # 2 represents the number of dimensions
print(arr.size)       # 6 is the total number of elements
print(arr.dtype)      # int64 is the data type
```

**Indexing:**

```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])       # 10
print(a[-1])      # 50

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 1])    # 2 (row 0, col 1)
print(b[2, -1])   # 9 (row 2, last col)
```

**Slicing:** `array[start:stop:step]` returns a view rather than a copy.

```python
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])     # [20, 30, 40]
print(a[:3])      # [10, 20, 30]
print(a[::2])     # [10, 30, 50]
print(a[::-1])    # [50, 40, 30, 20, 10]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0:2, 1:3])    # [[2, 3], [5, 6]]
print(b[:, 1])         # [2, 5, 8] (entire column 1)
print(b[1, :])         # [4, 5, 6] (entire row 1)
```

**Boolean indexing (fancy indexing):**

```python
a = np.array([10, 20, 30, 40, 50])
print(a[a > 25])      # [30, 40, 50]
print(a[a % 20 == 0]) # [20, 40]
```

## 7.7 Copying and Editing NumPy Arrays

**View (shallow copy):** Slicing returns a view. Modifying the view modifies the original.

```python
a = np.array([1, 2, 3, 4, 5])
view = a[1:4]          # view, not a copy
view[0] = 99
print(a)               # [1, 99, 3, 4, 5]. The original array has changed.
```

**Copy (deep copy):** The `copy()` method creates an independent copy. Modifications do not affect the original.

```python
a = np.array([1, 2, 3, 4, 5])
copy = a.copy()
copy[0] = 99
print(a)               # [1, 2, 3, 4, 5]. The original array is unchanged.
print(copy)            # [99, 2, 3, 4, 5]
```

**Editing arrays:**

```python
a = np.array([1, 2, 3, 4, 5])
a[0] = 10              # modify single element
a[1:3] = [20, 30]      # modify slice

# Append, insert, delete (these return new arrays since NumPy arrays have fixed size)
a = np.append(a, [6, 7])           # append at end
a = np.insert(a, 2, 99)            # insert 99 at index 2
a = np.delete(a, 0)                # delete element at index 0

# Where is used for conditional replacement
a = np.array([1, 2, 3, 4, 5])
result = np.where(a > 3, a, 0)     # [0, 0, 0, 4, 5]
```

## 7.8 Stacking and Restructuring NumPy Arrays

> How do you reshape a NumPy array? Write a program to solve following system of linear equations using NumPy: `2x + 3y = 12`, `4x - 5y = -2`. [2+4 marks] (2082 Baishakh - IOE)

**Reshaping** changes the dimensions of an array without altering its data. The total number of elements must remain the same.

```python
a = np.arange(1, 13)          # [1, 2, 3, ..., 12]
b = a.reshape(3, 4)           # 3×4 matrix
c = a.reshape(2, 2, 3)        # 2×2×3 3D array
d = a.reshape(4, -1)          # -1 means auto-calculate: 4×3
```

**Flatten and ravel:**

```python
b = np.array([[1, 2], [3, 4]])
print(b.flatten())    # [1, 2, 3, 4] returns a copy
print(b.ravel())      # [1, 2, 3, 4] returns a view
```

**Transpose:**

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.T)            # [[1, 4], [2, 5], [3, 6]]
print(b.transpose())  # same as b.T
```

**Stacking arrays:**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))    # vertical stack: [[1,2,3], [4,5,6]]
print(np.hstack((a, b)))    # horizontal stack: [1,2,3,4,5,6]

c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print(np.vstack((c, d)))    # [[1,2], [3,4], [5,6], [7,8]]
print(np.hstack((c, d)))    # [[1,2,5,6], [3,4,7,8]]
```

**Example: Reshape 1D to 3×4, then vstack with transpose.**

> Write a program to create a 1D NumPy array of 12 elements, reshape it into a 3×4 matrix, then vertically stack it with its transpose (after reshaping).

```python
import numpy as np

a = np.arange(1, 13)
matrix = a.reshape(3, 4)
print("Original (3×4):\n", matrix)

transposed = matrix.T        # 4×3
reshaped_t = transposed.reshape(3, 4)
result = np.vstack((matrix, reshaped_t))
print("Stacked (6×4):\n", result)
```

## 7.9 Arithmetic Operations with NumPy Arrays

> Write a python program to create two 2×2 NumPy arrays and perform matrix addition, subtraction and element-wise multiplication and display the result. [9 marks] (2081 Ashwin - IOE)

NumPy performs element-wise operations by default using standard operators.

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise operations
print("Addition:\n", a + b)             # [[ 6,  8], [10, 12]]
print("Subtraction:\n", a - b)          # [[-4, -4], [-4, -4]]
print("Multiplication:\n", a * b)       # [[ 5, 12], [21, 32]]
print("Division:\n", a / b)             # [[0.2, 0.333], [0.428, 0.5]]
print("Power:\n", a ** 2)               # [[ 1,  4], [ 9, 16]]
print("Modulus:\n", b % a)              # [[0, 0], [1, 0]]
```

**Matrix multiplication** (dot product) is not element-wise:

```python
print("Matrix Multiply:\n", a @ b)          # [[19, 22], [43, 50]]
print("Matrix Multiply:\n", np.dot(a, b))   # same result
```

**Aggregate functions:**

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(a))          # 21
print(np.sum(a, axis=0))  # [5, 7, 9]  (column-wise)
print(np.sum(a, axis=1))  # [6, 15]    (row-wise)
print(np.min(a))          # 1
print(np.max(a))          # 6
print(np.mean(a))         # 3.5
```

**Universal functions (ufuncs):**

```python
a = np.array([1, 4, 9, 16])
print(np.sqrt(a))         # [1., 2., 3., 4.]
print(np.exp(a))          # [2.718, 54.598, 8103.08, ...]
print(np.log(a))          # [0., 1.386, 2.197, 2.772]
print(np.abs(np.array([-1, -2, 3])))  # [1, 2, 3]
```

## 7.10 Operations with NumPy Arrays of Different Shapes

> Write a program using NumPy to create two arrays of different shapes and demonstrate broadcasting by performing addition between them.

**Broadcasting** allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array to match the larger one. No actual copying of data occurs because it is handled internally for efficiency.

**Broadcasting rules:**

- NumPy compares shapes element-wise from the trailing dimensions (rightmost).
- Two dimensions are compatible if they are equal, or one of them is 1.
- If dimensions don't match and neither is 1, broadcasting fails with a `ValueError`.

```python
import numpy as np

# Scalar + Array (scalar broadcast to all elements)
a = np.array([1, 2, 3])
print(a + 10)             # [11, 12, 13]

# 1D + 2D broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])       # shape (2, 3)
b = np.array([10, 20, 30])     # shape (3,)
print(a + b)
# [[11, 22, 33],
#  [14, 25, 36]]

# Column vector + Row vector
col = np.array([[1], [2], [3]])   # shape (3, 1)
row = np.array([10, 20, 30])     # shape (3,)
print(col + row)
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]
```

## 7.11 Concatenation, Reversion and Persistence of NumPy Arrays

**Concatenation** joins arrays along an existing axis:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))     # [1, 2, 3, 4, 5, 6]

c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6]])
print(np.concatenate((c, d), axis=0))    # [[1,2], [3,4], [5,6]]
print(np.concatenate((c, d.T), axis=1))  # [[1,2,5], [3,4,6]]
```

**Reversing arrays:**

```python
a = np.array([1, 2, 3, 4, 5])
print(a[::-1])                    # [5, 4, 3, 2, 1]
print(np.flip(a))                 # [5, 4, 3, 2, 1]

b = np.array([[1, 2], [3, 4]])
print(np.flip(b))                 # [[4, 3], [2, 1]]
print(np.flip(b, axis=0))        # [[3, 4], [1, 2]] flips rows
print(np.flip(b, axis=1))        # [[2, 1], [4, 3]] flips columns
```

**Persistence (saving and loading arrays):**

```python
a = np.array([1, 2, 3, 4, 5])

# Save/load single array (.npy)
np.save("myarray.npy", a)
loaded = np.load("myarray.npy")

# Save/load multiple arrays (.npz)
b = np.array([6, 7, 8])
np.savez("arrays.npz", arr1=a, arr2=b)
data = np.load("arrays.npz")
print(data["arr1"])       # [1, 2, 3, 4, 5]
print(data["arr2"])       # [6, 7, 8]

# Save/load as text file
np.savetxt("data.csv", a.reshape(1, -1), delimiter=",")
loaded_txt = np.loadtxt("data.csv", delimiter=",")
```

## 7.12 Applications of NumPy Random Number Generation

> Write a program to create a NumPy array of 20 random integers between 1 and 100, then find and display the mean, median, standard deviation, and variance using NumPy functions.

```python
import numpy as np

# Random integers
arr = np.random.randint(1, 101, size=20)
print("Array:", arr)

# Random floats [0.0, 1.0)
floats = np.random.random(5)
print("Random floats:", floats)

# Random from normal distribution
normal = np.random.randn(5)           # standard normal (mean=0, std=1)
normal2 = np.random.normal(50, 10, 5) # mean=50, std=10, size=5

# Random choice
choices = np.random.choice([10, 20, 30, 40], size=3)

# Shuffle (in-place)
a = np.array([1, 2, 3, 4, 5])
np.random.shuffle(a)

# Seed for reproducibility
np.random.seed(42)
print(np.random.randint(1, 100, 5))   # same output every time
```

## 7.13 Applications of NumPy Statistics

```python
import numpy as np

arr = np.random.randint(1, 101, size=20)
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std Dev:", np.std(arr))
print("Variance:", np.var(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Sum:", np.sum(arr))

# Percentile and quantile
print("25th Percentile:", np.percentile(arr, 25))
print("75th Percentile:", np.percentile(arr, 75))

# Along specific axis for 2D arrays
b = np.array([[10, 20, 30], [40, 50, 60]])
print("Column means:", np.mean(b, axis=0))    # [25., 35., 45.]
print("Row means:", np.mean(b, axis=1))       # [20., 50.]
```

**Complete example: Random array with statistics.**

```python
import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=20)
print("Array:", arr)
print(f"Mean: {np.mean(arr):.2f}")
print(f"Median: {np.median(arr):.2f}")
print(f"Standard Deviation: {np.std(arr):.2f}")
print(f"Variance: {np.var(arr):.2f}")
```

## 7.14 Applications of NumPy Linear Algebra

The `numpy.linalg` module provides functions for linear algebra operations.

**Solving a system of linear equations:** For `Ax = b`, use `np.linalg.solve(A, b)`:

> Solve: 2x + 3y = 12, 4x - 5y = -2. [4 marks] (2082 Baishakh - IOE)

```python
import numpy as np

# 2x + 3y = 12
# 4x - 5y = -2
A = np.array([[2, 3],
              [4, -5]])
b = np.array([12, -2])

x = np.linalg.solve(A, b)
print(f"x = {x[0]}, y = {x[1]}")    # x = 3.0, y = 2.0

# Verify: A @ x should equal b
print("Verification:", np.allclose(A @ x, b))   # True
```

**Other linear algebra operations:**

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])

# Determinant
print("Determinant:", np.linalg.det(A))        # -2.0

# Inverse
print("Inverse:\n", np.linalg.inv(A))

# Matrix multiplication
B = np.array([[5, 6], [7, 8]])
print("A × B:\n", A @ B)                       # [[19, 22], [43, 50]]

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Matrix rank
print("Rank:", np.linalg.matrix_rank(A))       # 2

# Norm
print("Norm:", np.linalg.norm(A))              # Frobenius norm

# Transpose
print("Transpose:\n", A.T)
```
