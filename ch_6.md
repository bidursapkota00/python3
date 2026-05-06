# Chapter 6: Exceptions and File Handling in Python

## 6.1 Types of Errors

> 📝 **Explain different types of errors in python program. [2 marks] (2081 Ashwin - IOE)**

Errors in Python fall into three categories:

**Syntax errors** occur when code violates Python's grammar rules. The interpreter cannot parse the code, so it does not execute at all. Common causes include missing colons, unmatched parentheses, incorrect indentation, and misspelled keywords.

```python
if x == 10        # SyntaxError: expected ':'
    print("ten")
```

**Runtime errors (exceptions)** occur during execution. The code is syntactically correct, but an illegal operation is attempted at runtime.

```python
print(10 / 0)         # ZeroDivisionError
print(int("abc"))     # ValueError
print(my_var)         # NameError (undefined variable)
```

**Logical (semantic) errors** produce no error message — the program runs but gives incorrect results. These are caused by flawed algorithm logic and are the hardest to detect.

```python
# Intended: area = length * width
area = length + width    # Wrong operator — logical error
```

## 6.2 Types of Exceptions

An **exception** is a runtime error that disrupts the normal flow of program execution. Python has a hierarchy of built-in exceptions, all inheriting from `BaseException`. The most commonly caught exceptions inherit from `Exception`.

**Common built-in exceptions:**

- `ZeroDivisionError` — Division or modulo by zero.
- `ValueError` — Function receives argument of correct type but inappropriate value.
- `TypeError` — Operation applied to an object of inappropriate type.
- `IndexError` — Sequence index out of range.
- `KeyError` — Dictionary key not found.
- `NameError` — Name (variable/function) not found in scope.
- `AttributeError` — Attribute reference or assignment fails.
- `FileNotFoundError` — Specified file does not exist.
- `IOError` / `OSError` — Input/output operation fails.
- `ImportError` — Module import fails.
- `StopIteration` — `next()` called on exhausted iterator.
- `RecursionError` — Maximum recursion depth exceeded.
- `OverflowError` — Arithmetic result too large to represent.

You can view the exception hierarchy using:

```python
print(ZeroDivisionError.__mro__)
# (<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>,
#  <class 'BaseException'>, <class 'object'>)
```

## 6.3 Catching and Handling Exceptions

> 📝 **Define exception. You cannot divide a given number by zero. Based on given statement, write python code to handle the given exception. [2+4 marks] (2082 Baishakh - IOE)**

Exceptions are handled using the `try`-`except`-`else`-`finally` block:

- **`try`** — Contains code that might raise an exception.
- **`except`** — Executes if a specific exception occurs in the `try` block.
- **`else`** — Executes only if no exception was raised in the `try` block.
- **`finally`** — Executes always, regardless of whether an exception occurred. Used for cleanup (closing files, releasing resources).

```python
try:
    risky_code()
except SomeException as e:
    handle_error(e)
else:
    no_error_occurred()
finally:
    always_runs()
```

**Example — Handling division by zero:**

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
```

**Catching multiple exceptions:**

```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

**Catching all exceptions** (use sparingly):

```python
try:
    risky()
except Exception as e:
    print(f"Something went wrong: {e}")
```

**The `raise` keyword** explicitly raises an exception:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

**Re-raising an exception:**

```python
try:
    process()
except ValueError:
    print("Logging the error...")
    raise       # re-raises the caught exception
```

## 6.4 User-Defined Exceptions

> 📝 **Write a program that defines a user-defined exception `InvalidAgeError`. Ask the user for their age; if the age is less than 0 or greater than 150, raise the custom exception with an appropriate message.**

Custom exceptions are created by inheriting from the `Exception` class (or any subclass of it). This allows you to define application-specific error types with custom messages.

```python
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Got: {self.age}"

try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    print(f"Your age is {age}")
except InvalidAgeError as e:
    print(f"Invalid Age Error: {e}")
except ValueError:
    print("Please enter a valid integer!")
```

**Output (if age = -5):**

```
Invalid Age Error: Age must be between 0 and 150. Got: -5
```

Best practice is to create a base exception for your application and derive specific exceptions from it:

```python
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

class ValidationError(AppError):
    pass
```

## 6.5 Debugging Programs with the Assert Statement

> 📝 **Write a program that uses the `assert` statement to verify that a function `calculate_area(radius)` receives a positive radius. If assertion fails, catch the `AssertionError` and print a debug message using the `logging` module.**

The `assert` statement is a debugging tool that tests a condition. If the condition is `True`, execution continues normally. If `False`, an `AssertionError` is raised.

**Syntax:** `assert condition, "optional error message"`

```python
def calculate_area(radius):
    assert radius > 0, "Radius must be positive"
    return 3.14 * radius ** 2

print(calculate_area(5))     # 78.5
# print(calculate_area(-3))  # AssertionError: Radius must be positive
```

**Important:** Assertions can be disabled by running Python with the `-O` (optimize) flag (`python -O script.py`). Therefore, assertions should only be used for internal sanity checks during development, **not** for validating user input or handling expected errors.

## 6.6 Logging the Exceptions

The `logging` module provides a flexible framework for recording diagnostic messages, far superior to `print()` for debugging and monitoring.

**Logging levels** (in order of increasing severity):

- `DEBUG` (10) — Detailed diagnostic information.
- `INFO` (20) — Confirmation that things are working.
- `WARNING` (30) — Something unexpected but not critical (default level).
- `ERROR` (40) — A serious problem.
- `CRITICAL` (50) — The program may not be able to continue.

**Basic usage:**

```python
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("Warning message")
logging.error("Error occurred")
logging.critical("Critical failure")
```

**Logging to a file:**

```python
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

**Example — Assert with logging:**

```python
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

def calculate_area(radius):
    assert radius > 0, "Radius must be positive"
    return 3.14 * radius ** 2

try:
    r = float(input("Enter radius: "))
    area = calculate_area(r)
    logging.info(f"Area calculated: {area}")
    print(f"Area: {area}")
except AssertionError as e:
    logging.error(f"Assertion failed: {e}")
    print(f"Debug Error: {e}")
except ValueError:
    logging.error("Invalid input received")
    print("Please enter a valid number")
```

## 6.7 Introduction to File Handling

> 📝 **Write a python program to create a file called "record.txt" and use it to store the information of two students [Name, Roll No and college Name]. Ask user to enter the information. [4 marks] (2081 Ashwin - IOE)**

**File handling** allows programs to read from and write to files, enabling persistent data storage beyond program execution. Python uses the built-in `open()` function for all file operations.

**Types of files:**

- **Text files** — Store data as human-readable characters (`.txt`, `.csv`, `.html`). Each line ends with a newline character (`\n`).
- **Binary files** — Store data in binary format (`.bin`, `.pkl`, `.jpg`, `.exe`). Not human-readable.

## 6.8 Opening and Closing a File

**The `open()` function:** `open(filename, mode)`

| Mode   | Description                                            |
| ------ | ------------------------------------------------------ |
| `'r'`  | Read (default). File must exist.                       |
| `'w'`  | Write. Creates new file or truncates existing file.    |
| `'a'`  | Append. Adds to end. Creates file if it doesn't exist. |
| `'x'`  | Exclusive creation. Fails if file already exists.      |
| `'r+'` | Read and write. File must exist.                       |
| `'w+'` | Write and read. Creates or truncates.                  |
| `'a+'` | Append and read. Creates if doesn't exist.             |
| `'b'`  | Binary mode (added to other modes: `'rb'`, `'wb'`).    |
| `'t'`  | Text mode (default, added to modes: `'rt'`, `'wt'`).   |

**Opening and closing manually:**

```python
f = open("data.txt", "w")
f.write("Hello, World!")
f.close()                     # must close manually
```

**Using `with` statement (recommended):** Automatically closes the file when the block exits, even if an error occurs.

```python
with open("data.txt", "w") as f:
    f.write("Hello, World!")
# file is automatically closed here
```

**Example — Store student records in a file:**

```python
with open("record.txt", "w") as f:
    for i in range(2):
        print(f"\nStudent {i + 1}:")
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        college = input("Enter College Name: ")
        f.write(f"Name: {name}, Roll: {roll}, College: {college}\n")

print("\nData written to record.txt")

# Reading back
with open("record.txt", "r") as f:
    print(f.read())
```

## 6.9 Working with Text and Binary Files

### Text File Operations

**Writing to a text file:**

```python
with open("output.txt", "w") as f:
    f.write("First line\n")            # write a string
    f.write("Second line\n")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)                # write a list of strings
```

**Reading from a text file:**

```python
with open("output.txt", "r") as f:
    content = f.read()          # read entire file as one string
    print(content)

with open("output.txt", "r") as f:
    line = f.readline()         # read one line at a time
    print(line)

with open("output.txt", "r") as f:
    all_lines = f.readlines()   # read all lines into a list
    print(all_lines)            # ['Line 1\n', 'Line 2\n', 'Line 3\n']

# Iterating line by line (memory efficient)
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())
```

**Example — Count words and lines, write result to new file:**

> 📝 **Write a program to read a text file, count the number of words and lines, and write the result to a new file. Handle the case where the input file does not exist.**

```python
try:
    with open("input.txt", "r") as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)

    with open("result.txt", "w") as f:
        f.write(f"Lines: {num_lines}\n")
        f.write(f"Words: {num_words}\n")

    print(f"Lines: {num_lines}, Words: {num_words}")
    print("Result written to result.txt")
except FileNotFoundError:
    print("Error: input.txt not found!")
```

### Binary File Operations

Binary files store data in raw byte format. The `pickle` module is used to serialize (convert objects to bytes) and deserialize (convert bytes back to objects) Python objects.

**Writing and reading with `pickle`:**

> 📝 **Write a program that writes a list of student records (name, roll, marks) to a binary file using the `pickle` module, then reads and displays them.**

```python
import pickle

# Writing student records to binary file
students = [
    {"name": "Ram", "roll": 101, "marks": 85},
    {"name": "Sita", "roll": 102, "marks": 92},
    {"name": "Hari", "roll": 103, "marks": 78}
]

with open("students.pkl", "wb") as f:
    pickle.dump(students, f)

print("Data written to students.pkl")

# Reading from binary file
with open("students.pkl", "rb") as f:
    loaded = pickle.load(f)

for s in loaded:
    print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
```

**`pickle` key functions:**

- `pickle.dump(obj, file)` — Serialize `obj` and write to `file`.
- `pickle.load(file)` — Read from `file` and deserialize to a Python object.
- `pickle.dumps(obj)` — Serialize to bytes (not to file).
- `pickle.loads(bytes)` — Deserialize from bytes.

**Writing/reading raw bytes without pickle:**

```python
# Writing bytes
with open("data.bin", "wb") as f:
    f.write(b'\x48\x65\x6c\x6c\x6f')    # "Hello" in bytes

# Reading bytes
with open("data.bin", "rb") as f:
    data = f.read()
    print(data)           # b'Hello'
    print(data.decode())  # "Hello"
```

## 6.10 Random File Access

**Sequential access** reads a file from beginning to end. **Random access** allows reading from or writing to any position in the file using `seek()` and `tell()`.

- **`tell()`** — Returns the current position of the file pointer (in bytes from the beginning).
- **`seek(offset, whence)`** — Moves the file pointer to a specific position.
  - `offset` — Number of bytes to move.
  - `whence` — Reference point: `0` = beginning (default), `1` = current position, `2` = end of file.

In text mode, only `seek(0)`, `seek(offset, 0)` with offsets from `tell()`, and `seek(0, 2)` are reliable. Binary mode supports all `whence` values.

```python
with open("sample.txt", "w+") as f:
    f.write("Hello, Python!")

    print(f.tell())         # 14 (current position after writing)

    f.seek(0)               # move to beginning
    print(f.read(5))        # "Hello"
    print(f.tell())         # 5

    f.seek(7)               # move to position 7
    print(f.read())         # "Python!"

    f.seek(0, 2)            # move to end of file
    f.write(" Bye!")        # append at end

    f.seek(0)
    print(f.read())         # "Hello, Python! Bye!"
```

**Example — Random access in binary mode:**

```python
with open("data.bin", "wb") as f:
    f.write(b"ABCDEFGHIJ")

with open("data.bin", "rb") as f:
    f.seek(3)               # move to 4th byte
    print(f.read(4))        # b'DEFG'

    f.seek(-3, 2)           # 3 bytes before end
    print(f.read())         # b'HIJ'

    f.seek(0)               # back to start
    print(f.tell())         # 0
```
