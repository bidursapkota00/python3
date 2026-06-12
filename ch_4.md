# Chapter 4: Advanced Data Types and Operation in Python

## 4.1 Mutable and Immutable Data Types

> Explain the concept of mutable and immutable data type in python. [4 marks] (2082 Baishakh - IOE)

Mutable objects can be modified in place after creation. Their content changes but their identity (memory address) remains the same. Immutable objects cannot be changed once created. Any modification creates a new object in memory.

| Category  | Data Types                                          |
| --------- | --------------------------------------------------- |
| Mutable   | `list`, `dict`, `set`, `bytearray`                  |
| Immutable | `int`, `float`, `str`, `tuple`, `bool`, `frozenset` |

**Verifying mutability with `id()`:**

```python
# Mutable: list modified in place, id stays same
a = [1, 2, 3]
print(id(a))       # e.g., 140234567890
a.append(4)
print(id(a))       # same id, object modified in place

# Immutable: string creates new object on modification
s = "hello"
print(id(s))       # e.g., 140234567000
s = s + " world"
print(id(s))       # different id, new object created
```

- Immutable objects are hashable and can be used as dictionary keys or set elements. Mutable objects like lists cannot.
- When a mutable object is passed to a function, changes inside the function affect the original object (pass by object reference). Immutable objects are safe from such side effects.
- Python caches small immutable objects (small integers, short strings) for memory efficiency.

**Example: Total marks from list of dictionaries**

> For the given list of dictionaries, find the TOTAL MARKS obtained: `d = [{"subject": "math", "marks": 80}, {"subject": "science", "marks": 90}, {"subject": "english", "marks": 80}]` [4 marks] (2082 Baishakh - IOE)

```python
d = [{"subject": "math", "marks": 80},
     {"subject": "science", "marks": 90},
     {"subject": "english", "marks": 80}]

total = 0
for item in d:
    total += item["marks"]
print("Total Marks:", total)   # Total Marks: 250
```

## 4.2 List and Tuple Data Types

> With example, explain following data structures in python: a) List b) Tuple c) Dictionary. [6 marks] (2081 Ashwin - IOE)

### List

A list is an ordered, mutable collection that can hold items of different types. Lists are defined using square brackets `[]`.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []
```

**Common list operations:**

```python
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])       # "apple"
print(fruits[-1])      # "cherry"

# Modifying elements
fruits[1] = "mango"    # ["apple", "mango", "cherry"]

# Adding elements
fruits.append("grape")          # adds at end
fruits.insert(1, "orange")     # inserts at index 1
fruits.extend(["kiwi", "fig"]) # adds multiple items

# Removing elements
fruits.remove("apple")    # removes first occurrence
popped = fruits.pop()     # removes and returns last item
fruits.pop(0)             # removes item at index 0
del fruits[0]             # deletes item at index 0

# Other useful methods
nums = [3, 1, 4, 1, 5]
nums.sort()               # sorts in place: [1, 1, 3, 4, 5]
nums.reverse()            # reverses in place: [5, 4, 3, 1, 1]
print(nums.count(1))      # 2 (occurrences of 1)
print(nums.index(4))      # 1 (first index of 4)
copy = nums.copy()        # shallow copy
nums.clear()              # removes all items
```

**Deep copy** creates a fully independent copy including all nested objects:

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 99
print(a)               # [[1, 2], [3, 4]], a is unchanged
```

**List slicing:** `list[start:stop:step]`

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]
print(nums[::2])     # [10, 30, 50]
print(nums[::-1])    # [50, 40, 30, 20, 10]
```

**List comprehension** is a concise way to create a list in a single line.

**Syntax:** `[expression for item in iterable if condition]`

```python
squares = [x ** 2 for x in range(1, 6)]           # [1, 4, 9, 16, 25]
evens = [x for x in range(20) if x % 2 == 0]      # [0, 2, 4, ..., 18]
pairs = [(x, y) for x in range(3) for y in range(3)]  # nested comprehension
```

### Tuple

A tuple is an ordered, immutable collection. Tuples are defined using parentheses `()`.

```python
point = (3, 5)
colors = ("red", "green", "blue")
single = (42,)         # trailing comma needed for single-element tuple
empty = ()
```

Since tuples are immutable, they do not support item assignment, append, remove, or any in-place modification. They support indexing, slicing, `count()`, `index()`, `len()`, `in`, concatenation (`+`), and repetition (`*`).

```python
t = (10, 20, 30, 20)
print(t[0])        # 10
print(t[1:3])      # (20, 30)
print(t.count(20)) # 2
print(t.index(30)) # 2
print(len(t))      # 4
print(20 in t)     # True
t2 = (1, 2) + (3, 4)      # (1, 2, 3, 4) — Tuple concatenation
```

**Tuple packing and unpacking:**

```python
# Packing
coords = 4, 5, 6          # parentheses optional

# Unpacking
x, y, z = coords          # x=4, y=5, z=6

# Swap using tuple unpacking
a, b = 1, 2
a, b = b, a               # a=2, b=1
```

> **Note:** Use tuples for fixed collections that should not change (e.g., coordinates, database records, dictionary keys). Tuples are faster than lists and consume less memory.

**Example: Tuple-List conversion and sorting**

> Write a program to create a tuple of student names, convert it to a list, add a new name, sort the list, and convert it back to a tuple.

```python
students = ("Ram", "Sita", "Hari", "Gita")
student_list = list(students)
student_list.append("Bikash")
student_list.sort()
students = tuple(student_list)
print(students)   # ('Bikash', 'Gita', 'Hari', 'Ram', 'Sita')
```

## 4.3 Dictionary Data Types

A dictionary is an unordered (insertion-ordered since Python 3.7), mutable collection of key-value pairs. Keys must be unique and immutable (strings, numbers, tuples). Defined using curly braces `{}`.

```python
student = {"name": "Alice", "age": 21, "grade": "A"}
empty = {}
```

**Common dictionary operations:**

```python
student = {"name": "Alice", "age": 21, "grade": "A"}

# Accessing values
print(student["name"])          # "Alice"
print(student.get("age"))      # 21
print(student.get("gpa", 0))   # 0 (default if key missing)

# Adding / Updating
student["age"] = 22             # update existing key
student["college"] = "IOE"     # add new key-value pair
student.update({"age": 23, "city": "KTM"})

# Removing
del student["grade"]                   # delete by key
removed = student.pop("city")         # remove and return value
student.popitem()                      # remove last inserted pair

# Iterating
for key in student:
    print(key, student[key])

for key, val in student.items():
    print(key, val)

# Useful methods
print(student.keys())       # dict_keys([...])
print(student.values())     # dict_values([...])
print(student.items())      # dict_items([(k, v), ...])
print(len(student))         # number of key-value pairs
print("name" in student)    # True (checks keys)
```

**Nested dictionary:**

```python
students = {
    101: {"name": "Ram", "marks": 85},
    102: {"name": "Sita", "marks": 92}
}
print(students[101]["name"])   # "Ram"
```

**Dictionary comprehension:** `{key: value for item in iterable if condition}`

```python
sq_dict = {x: x**2 for x in range(5)}    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Example: Character frequency counter**

> Write a program to count the frequency of each character in a given string using a dictionary.

```python
text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
for ch, count in freq.items():
    print(f"'{ch}': {count}")
```

## 4.4 Sequence Data Types

A sequence is an ordered collection of items that supports indexing, slicing, iteration, and membership testing. Python's built-in sequence types are `str`, `list`, `tuple`, and `range`.

**Common operations shared by all sequence types:**

| Operation      | Syntax                 | Description                             |
| -------------- | ---------------------- | --------------------------------------- |
| Indexing       | `seq[i]`               | Access element at index `i`             |
| Negative index | `seq[-1]`              | Last element                            |
| Slicing        | `seq[start:stop:step]` | Sub-sequence extraction                 |
| Length         | `len(seq)`             | Number of elements                      |
| Membership     | `x in seq`             | `True` if `x` exists in sequence        |
| Concatenation  | `seq1 + seq2`          | Combine two sequences (not for `range`) |
| Repetition     | `seq * n`              | Repeat `n` times (not for `range`)      |
| Count          | `seq.count(x)`         | Number of occurrences of `x`            |
| Index lookup   | `seq.index(x)`         | First index where `x` appears           |
| Min / Max      | `min(seq)`, `max(seq)` | Smallest / largest element              |

**Indexing and slicing work identically across all sequence types:**

```python
s = "PYTHON"
print(s[0])        # 'P'
print(s[-1])       # 'N'
print(s[1:4])      # 'YTH'
print(s[::-1])     # 'NOHTYP' (reversed)

t = (10, 20, 30, 40, 50)
print(t[2:])       # (30, 40, 50)
```

**`range` as a sequence:**

```python
r = range(0, 10, 2)    # 0, 2, 4, 6, 8
print(r[3])             # 6
print(5 in r)           # False
print(list(r))          # [0, 2, 4, 6, 8]
```

**String-specific methods** (since strings are sequences):

```python
s = "Hello, World!"
s.upper()           # "HELLO, WORLD!"
s.lower()           # "hello, world!"
s.strip()           # removes leading/trailing whitespace
s.split(", ")       # ["Hello", "World!"]
", ".join(["a","b"])# "a, b"
s.replace("World", "Python")  # "Hello, Python!"
s.find("World")     # 7 (index of first match, -1 if not found)
s.startswith("He")  # True
s.isdigit()         # False
# String <-> List
chars = list("hello")         # ['h', 'e', 'l', 'l', 'o']
s = "".join(chars)             # "hello"
```

## 4.5 Two-Dimensional Lists

> Using two-dimensional list, write a program to add two matrices and create the third matrix and display it. [4 marks] (2081 Ashwin - IOE)

A two-dimensional list (2D list) is a list of lists, commonly used to represent matrices, grids, or tabular data.

**Creating a 2D list:**

```python
# Direct initialization
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using list comprehension (3x4 matrix of zeros)
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
```

**Accessing and modifying elements:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])     # 2 (row 0, column 1)
matrix[1][2] = 99       # modify element
print(matrix[1])        # [4, 5, 99] (entire row)
```

**Iterating over a 2D list:**

```python
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()
```

**Example: Matrix addition**

```python
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

rows = len(A)
cols = len(A[0])
C = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]

print("Resultant Matrix:")
for row in C:
    print(row)
# [8, 10, 12]
# [14, 16, 18]
```

**Common pitfall with incorrect initialization:**

```python
# WRONG: all rows share the same list object
matrix = [[0] * 3] * 3
matrix[0][0] = 5
print(matrix)   # [[5, 0, 0], [5, 0, 0], [5, 0, 0]]  <-- all rows changed!

# CORRECT: each row is an independent list
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 5
print(matrix)   # [[5, 0, 0], [0, 0, 0], [0, 0, 0]]  <-- only first row changed
```

## 4.6 Set Data Types

A set is an unordered, mutable collection of unique elements. Sets are defined using curly braces `{}` or the `set()` constructor. Sets do not support indexing or slicing.

```python
s = {1, 2, 3, 4, 5}
empty = set()          # NOT {} — that creates an empty dict
from_list = set([1, 2, 2, 3])   # {1, 2, 3} — duplicates removed
```

**Set methods:**

```python
s = {1, 2, 3}
s.add(4)               # {1, 2, 3, 4}
s.update([5, 6])       # {1, 2, 3, 4, 5, 6}
s.remove(6)            # removes 6; raises KeyError if not found
s.discard(10)          # removes 10 if present; no error if absent
s.pop()                # removes and returns an arbitrary element
s.clear()              # empties the set
```

**Set operations (mathematical):**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)       # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(A & B)       # Intersection: {4, 5}
print(A - B)       # Difference: {1, 2, 3}
print(A ^ B)       # Symmetric Difference: {1, 2, 3, 6, 7, 8}
print(A <= B)      # Subset check: False
print(A >= B)      # Superset check: False
```

Equivalent methods: `A.union(B)`, `A.intersection(B)`, `A.difference(B)`, `A.symmetric_difference(B)`, `A.issubset(B)`, `A.issuperset(B)`. Methods accept any iterable as argument; operators require both operands to be sets.

**Set comprehension:** `{expression for item in iterable if condition}`

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}   # {2, 3, 5}
```

**`frozenset`** is an immutable version of set. It cannot add or remove elements. Since it is hashable, it can be used as a dictionary key or element of another set.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)    # raises AttributeError
d = {fs: "immutable set as key"}
```

**Example: Set operations demonstration**

> Write a program demonstrating set operations: create two sets of integers, then display their union, intersection, difference, and symmetric difference.

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)
```

## 4.7 Lambda

> Explain the significance of lambda function with an example. [2 marks] (2082 Baishakh - IOE)

A lambda function is a small, anonymous (unnamed) function defined using the `lambda` keyword. It can take any number of arguments but contains only a single expression whose result is implicitly returned.

**Syntax:** `lambda arguments: expression`

```python
square = lambda x: x ** 2
print(square(5))       # 25

add = lambda a, b: a + b
print(add(3, 4))       # 7
```

Lambda functions are most useful when passed as arguments to higher-order functions like `map()`, `filter()`, `sorted()`, and `reduce()`.

### Lambda with `map()`

`map(function, iterable)` applies a function to every item in an iterable and returns an iterator.

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)    # [1, 4, 9, 16, 25]
```

### Lambda with `filter()`

`filter(function, iterable)` returns an iterator of elements for which the function returns `True`.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)      # [2, 4, 6, 8]
```

### Lambda with `sorted()`

`sorted(iterable, key=function)` sorts elements using a key function for comparison.

```python
# Numbers
nums = [4, 1, 7, 2]
sorted(nums)                      # [1, 2, 4, 7]
sorted(nums, reverse=True)        # [7, 4, 2, 1]

# Words
words = ["banana", "apple", "cherry"]
sorted(words)                     # ['apple', 'banana', 'cherry']
sorted(words, reverse=True)       # ['cherry', 'banana', 'apple']

# Words by last character
sorted(words, key=lambda x: x[-1])  # ['banana', 'apple', 'cherry']

pairs = [(3, "c"), (1, "a"), (2, "b")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)   # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### Lambda with `reduce()`

`reduce(function, iterable, initial?)` from `functools` applies a two-argument function cumulatively to collapse an iterable into a single value. The optional third argument sets the starting value; if omitted, the first element is used.

```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)   # 120

# Sum
reduce(lambda x, y: x + y, nums)        # 15
reduce(lambda x, y: x + y, nums, 100)  # 115

# Max
reduce(lambda x, y: x if x > y else y, nums)   # 5
```

**Example: Filter even numbers and square all numbers**

> Write a program that takes a list of numbers and uses a lambda function with `filter()` to display only the even numbers, and another lambda with `map()` to display the square of each number.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)        # [2, 4, 6, 8, 10]

squares = list(map(lambda x: x ** 2, nums))
print("Squares:", squares)           # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Example: List comprehension for odd squares and lambda sort**

> Write a program using list comprehension to generate a list of squares of all odd numbers from 1 to 20, and use a lambda function to sort a list of tuples `[(3,"c"), (1,"a"), (2,"b")]` by the second element.

```python
odd_squares = [x ** 2 for x in range(1, 21) if x % 2 != 0]
print("Odd squares:", odd_squares)
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

data = [(3, "c"), (1, "a"), (2, "b")]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted:", sorted_data)
# [(1, 'a'), (2, 'b'), (3, 'c')]
```
