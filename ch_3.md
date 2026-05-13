# Chapter 3: Basic Programming Concept in Python

## 3.1 Keywords

Keywords are reserved words in Python that have predefined meanings and cannot be used as variable names, function names, or identifiers. They are case-sensitive. Python 3 has 35 keywords:

```
False      None       True       and        as
assert     async      await      break      class
continue   def        del        elif       else
except     finally    for        from       global
if         import     in         is         lambda
nonlocal   not        or         pass       raise
return     try        while      with       yield
```

You can list all keywords programmatically:

```python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))  # 35
```

**Soft keywords** (e.g., `case`, `_` inside `match` statements) are reserved only in specific contexts and can be used as identifiers elsewhere.

## 3.2 Basic Data Types

Python is dynamically typed. Variable types are determined at runtime, and no explicit type declaration is needed.

### Numeric Types

- **`int`**: Whole numbers, positive or negative, with no size limit (arbitrary precision). Example: `x = 42`
- **`float`**: Numbers with a decimal point, represented with double precision (64-bit IEEE 754). Example: `pi = 3.14`
- **`complex`**: Numbers with a real and imaginary part, written with a `j` suffix. Example: `z = 3 + 5j`. Access parts with `z.real` and `z.imag`.

### Text Type

- **`str`**: Sequence of Unicode characters, enclosed in single (`'...'`), double (`"..."`), or triple quotes (`'''...'''` / `"""..."""`). Strings are immutable. Example: `name = "Python"`

### Boolean Type

- **`bool`**: Has only two values: `True` and `False`. `bool` is a subclass of `int` (`True == 1`, `False == 0`). Used in conditional and logical expressions.

### None Type

- **`NoneType`**: Has a single value: `None`. Represents the absence of a value. Commonly used as a default return value of functions and for initializing variables.

### Type Checking and Conversion

```python
x = 10
print(type(x))           # <class 'int'>
print(isinstance(x, int)) # True
```

**Implicit conversion** (coercion): Python automatically converts smaller types to larger types during operations to prevent data loss:

```python
result = 10 + 3.5   # int + float → float (13.5)
```

**Explicit conversion** (casting): The programmer manually converts using built-in functions:

```python
int("25")      # 25 (string → int)
int(3.99)      # 3  (float → int, truncates decimal)
float(10)      # 10.0
str(100)       # "100"
bool(0)        # False
bool("hello")  # True (non-empty string)
```

## 3.3 Variables and Inputs

### Variables

A variable is a name that refers to a value stored in memory. Python uses dynamic typing. The type is inferred from the assigned value. No declaration keyword is needed.

```python
x = 10          # int
name = "Alice"  # str
pi = 3.14       # float
```

**Naming rules:**

- Must start with a letter (a–z, A–Z) or underscore (`_`).
- Can contain letters, digits (0–9), and underscores.
- Cannot be a keyword.
- Case-sensitive (`age` and `Age` are different variables).

**Multiple assignment:**

```python
a, b, c = 1, 2, 3       # assign different values
x = y = z = 0            # assign same value
a, b = b, a              # swap values
```

### User Input

The `input()` function reads input from the user as a string. You must explicitly convert it for numeric use.

```python
name = input("Enter your name: ")        # returns str
age = int(input("Enter your age: "))      # convert to int
height = float(input("Enter height: "))   # convert to float
```

### Output

The `print()` function outputs data to the console.

```python
print("Hello", name)                # space-separated by default
print("Age:", age, sep=" = ")        # custom separator
print("Line1", end="")              # suppress newline
print(f"Name: {name}, Age: {age}")  # f-string formatting
```

## 3.4 Logic and Comparison Operations

> **What do you mean by operators? Explain different types of operators available in python with example. [2+4 marks] (2081 Ashwin - IOE)**

An operator is a special symbol or keyword that performs an operation on one or more operands (values/variables). Python supports seven types of operators:

### Arithmetic Operators

| Operator | Description      | Example  | Result  |
| -------- | ---------------- | -------- | ------- |
| `+`      | Addition         | `7 + 3`  | `10`    |
| `-`      | Subtraction      | `7 - 3`  | `4`     |
| `*`      | Multiplication   | `7 * 3`  | `21`    |
| `/`      | Division (float) | `7 / 3`  | `2.333` |
| `//`     | Floor division   | `7 // 3` | `2`     |
| `%`      | Modulus          | `7 % 3`  | `1`     |
| `**`     | Exponentiation   | `2 ** 3` | `8`     |

### Comparison (Relational) Operators

Return `True` or `False`.

| Operator | Meaning               | Example           |
| -------- | --------------------- | ----------------- |
| `==`     | Equal to              | `5 == 5` → `True` |
| `!=`     | Not equal to          | `5 != 3` → `True` |
| `>`      | Greater than          | `5 > 3` → `True`  |
| `<`      | Less than             | `3 < 5` → `True`  |
| `>=`     | Greater than or equal | `5 >= 5` → `True` |
| `<=`     | Less than or equal    | `3 <= 5` → `True` |

### Logical Operators

| Operator | Description                          | Example                    |
| -------- | ------------------------------------ | -------------------------- |
| `and`    | True if both operands are true       | `True and False` → `False` |
| `or`     | True if at least one operand is true | `True or False` → `True`   |
| `not`    | Reverses the boolean value           | `not True` → `False`       |

### Bitwise Operators

Operate on integers at the binary level.

| Operator | Description | Example         |
| -------- | ----------- | --------------- |
| `&`      | AND         | `5 & 3` → `1`   |
| `\|`     | OR          | `5 \| 3` → `7`  |
| `^`      | XOR         | `5 ^ 3` → `6`   |
| `~`      | NOT         | `~5` → `-6`     |
| `<<`     | Left shift  | `5 << 1` → `10` |
| `>>`     | Right shift | `5 >> 1` → `2`  |

### Assignment Operators

| Operator | Equivalent   | Example   |
| -------- | ------------ | --------- |
| `=`      | Assign       | `x = 5`   |
| `+=`     | `x = x + y`  | `x += 3`  |
| `-=`     | `x = x - y`  | `x -= 3`  |
| `*=`     | `x = x * y`  | `x *= 3`  |
| `/=`     | `x = x / y`  | `x /= 3`  |
| `//=`    | `x = x // y` | `x //= 3` |
| `%=`     | `x = x % y`  | `x %= 3`  |
| `**=`    | `x = x ** y` | `x **= 3` |

### Identity Operators

Compare memory locations (whether two variables reference the **same object**).

- `is`: Returns `True` if both point to the same object. Example: `x is y`
- `is not`: Returns `True` if they point to different objects. Example: `x is not y`

```python
a = [1, 2]
b = a          # b references same object
c = [1, 2]     # c is a different object with same value
print(a is b)      # True
print(a is c)      # False
print(a == c)      # True (values are equal)
```

### Membership Operators

Test if a value exists in a sequence (string, list, tuple, set, dict).

- `in`: Returns `True` if value is found. Example: `3 in [1, 2, 3]` → `True`
- `not in`: Returns `True` if value is not found. Example: `4 not in [1, 2, 3]` → `True`

### Operator Precedence (highest to lowest)

`**` → `~, +, -` (unary) → `*, /, //, %` → `+, -` → `<<, >>` → `&` → `^` → `|` → `==, !=, <, >, <=, >=, is, is not, in, not in` → `not` → `and` → `or`

## 3.5 Conditional Statements

Conditional statements control the flow of execution based on boolean conditions.

### `if` Statement

```python
x = 10
if x > 0:
    print("Positive")
```

### `if-else` Statement

```python
x = -5
if x >= 0:
    print("Non-negative")
else:
    print("Negative")
```

### `if-elif-else` Statement

```python
marks = 75
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("F")
```

### Nested `if`

```python
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
```

### Ternary (Conditional) Expression

```python
result = "Even" if x % 2 == 0 else "Odd"
```

**Example: Positive, Negative or Zero check:**

> **Write a program that takes a number from the user and checks whether it is positive, negative, or zero using conditional statements.**

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

**Example: Simple calculator using conditionals:**

> **Write a program that reads two numbers and an operator (+, -, \*, /) from the user and performs the corresponding arithmetic operation. Handle division by zero.**

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b == 0:
        print("Error: Division by zero!")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")
```

## 3.6 Loops

Loops execute a block of code repeatedly until a condition is met.

### `for` Loop

Iterates over a sequence (list, tuple, string, range, etc.).

```python
for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for char in "Python":
    print(char)

for item in [10, 20, 30]:
    print(item)
```

**`range()` function:** `range(start, stop, step)` generates a sequence of integers from `start` (inclusive) to `stop` (exclusive) with a given `step`.

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 8)     # 2, 3, 4, 5, 6, 7
range(0, 10, 2) # 0, 2, 4, 6, 8
range(5, 0, -1) # 5, 4, 3, 2, 1
```

### `while` Loop

Repeats as long as the condition is `True`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Loop Control Statements

- **`break`**: Exits the loop immediately.
- **`continue`**: Skips the rest of the current iteration and moves to the next.
- **`pass`**: Does nothing. It acts as a placeholder.

```python
for i in range(10):
    if i == 5:
        break          # loop stops at i=5
    if i % 2 == 0:
        continue       # skip even numbers
    print(i)           # prints 1, 3
```

### `else` Clause with Loops

The `else` block executes only if the loop completes without encountering `break`.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")  # This executes
```

### Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

**Example: Multiplication table:**

> **Write a program using a `for` loop to print the multiplication table of a given number.**

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

**Example: Factorial using both iterative and recursive approaches:**

> **Write a program to find the factorial of a number using both iterative (loop) and recursive approaches. [3.6 Loop, 3.8 Recursion function call]**

```python
# Iterative approach
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

num = int(input("Enter a number: "))
print(f"Iterative: {factorial_iter(num)}")
print(f"Recursive: {factorial_rec(num)}")
```

## 3.7 Functions

A function is a reusable block of code that performs a specific task. Functions promote modularity, code reuse, and readability.

### Defining and Calling a Function

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet("Alice")    # Output: Hello, Alice!
```

### Function with Return Value

```python
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8
```

A function without a `return` statement returns `None` by default.

### Types of Arguments

**Positional arguments** are matched by position:

```python
def power(base, exp):
    return base ** exp

power(2, 3)    # base=2, exp=3 → 8
```

**Default arguments** have a default value, making them optional:

```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Bob")              # Hello, Bob!
greet("Bob", "Welcome")   # Welcome, Bob!
```

**Keyword arguments** are passed by name, allowing any order:

```python
greet(msg="Hi", name="Bob")   # Hi, Bob!
```

**Arbitrary positional arguments (`*args`)** collects extra positional arguments into a tuple:

```python
def total(*args):
    return sum(args)

total(1, 2, 3, 4)   # 10
```

**Arbitrary keyword arguments (`**kwargs`)\*\* collects extra keyword arguments into a dictionary:

```python
def info(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

info(name="Alice", age=25)
```

### Variable Scope

- **Local scope**: Variables defined inside a function. Accessible only within that function.
- **Global scope**: Variables defined at the module level. Accessible from anywhere in the file.
- **LEGB rule**: Python resolves names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = 10    # global

def func():
    x = 5     # local (shadows global x)
    print(x)  # 5

func()
print(x)      # 10 (global unchanged)
```

Use the `global` keyword to modify a global variable inside a function:

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)   # 1
```

**Example: Prime check function:**

> **Write a function `is_prime(n)` that returns `True` if it is a prime number, else `False`. Use this function to display all prime numbers between 1 and 100.**

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

## 3.8 Recursion Function Call

> **Define recursive function. Write a program to find the nth term of Fibonacci series using recursive function. [2+4 marks] (2082 Baishakh - IOE)**

Recursion is a technique where a function calls itself to solve a problem by breaking it into smaller, self-similar sub-problems. Every recursive function must have:

- **Base case**: A condition that stops the recursion and returns a value directly.
- **Recursive case**: The function calls itself with modified arguments, moving toward the base case.

Without a proper base case, the function will call itself infinitely and raise a `RecursionError` (Python's default recursion limit is 1000).

### Factorial Using Recursion

Mathematical definition: `n! = n × (n-1)!`, with base case `0! = 1`.

```python
def factorial(n):
    if n <= 1:        # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120
```

**Execution trace for `factorial(4)`:**

```
factorial(4) → 4 * factorial(3)
                   → 3 * factorial(2)
                              → 2 * factorial(1)
                                         → 1 (base case)
                              → 2 * 1 = 2
                   → 3 * 2 = 6
             → 4 * 6 = 24
```

### Fibonacci Using Recursion

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
Definition: `F(n) = F(n-1) + F(n-2)`, with base cases `F(0) = 0`, `F(1) = 1`.

```python
def fibonacci(n):
    if n <= 0:
        return 0        # base case
    elif n == 1:
        return 1        # base case
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case

n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {fibonacci(n)}")
```

### Recursion vs Iteration

- **Recursion** uses function call stack, making code elegant and closer to mathematical definitions, but can be slower and uses more memory due to stack frames.
- **Iteration** uses loops, is generally faster and more memory-efficient, but can be less intuitive for problems with a naturally recursive structure (e.g., tree traversal, Tower of Hanoi).
- The naive recursive Fibonacci has exponential time complexity O(2ⁿ) because it recalculates the same values repeatedly. The iterative version runs in O(n).

**Factorial: iterative vs recursive comparison:**

```python
# Iterative
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)
```
