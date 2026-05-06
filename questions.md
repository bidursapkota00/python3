# Python Programming Questions

## 1 Programming Paradigms (2 hours)

### 1.2 Different programming paradigms

- Explain different programming paradigm with example for each. [4 marks] (2081 Ashwin - IOE)

### 1.3 Advantages, disadvantages of different paradigms and examples

- Discuss about the different programming paradigms with their advantage and disadvantage. [4 marks] (2082 Baishakh - IOE)

---

## 2 Introduction to Python Programming (3 hours)

### 2.3 Features and limitations of Python

- Briefly explain different application areas of python programming. [4 marks] (2082 Baishakh - IOE)
- List out the features and limitations of python. [2+2 marks] (2081 Ashwin - IOE)

---

## 3 Basic Programming Concept in Python (5 hours)

### 3.4 Logic and comparison operations

- What do you mean by operators? Explain different types of operators available in python with example. [2+4 marks] (2081 Ashwin - IOE)
- Write a program that reads two numbers and an operator (+, -, \*, /) from the user and performs the corresponding arithmetic operation. Handle division by zero with an appropriate message. [3.4 Logic and comparison operations, 3.5 Conditional statement]

### 3.5 Conditional statement

- Write a program that takes a number from the user and checks whether it is positive, negative, or zero using conditional statements. [3.5 Conditional statement]

### 3.6 Loop

- Write a program using a `for` loop to print the multiplication table of a given number entered by the user. [3.6 Loop]
- Write a program to find the factorial of a number using both iterative (loop) and recursive approaches. [3.6 Loop, 3.8 Recursion function call]

### 3.7 Functions

- Write a function `is_prime(n)` that takes a number as argument and returns `True` if it is a prime number, else `False`. Use this function to display all prime numbers between 1 and 100. [3.7 Functions]

### 3.8 Recursion function call

- Define recursive function. Write a program to find the $n^{th}$ - term of Fibonacci series using recursive function. [2+4 marks] (2082 Baishakh - IOE)

---

## 4 Advanced Data Types and Operation in Python (8 hours)

### 4.1 Mutable and immutable data types

- Explain the concept of mutable and immutable data type in python. For the given list of dictionaries, find the TOTAL MARKS obtained: `d = [{"subject":"math","marks":80}, {"subject":"science","marks":90}, {"subject":"english","marks":80}]` [4+4 marks] (2082 Baishakh - IOE)

### 4.2 List and tuple data types

- Write a program to create a tuple of student names, convert it to a list, add a new name, sort the list, and convert it back to a tuple. Demonstrate the difference between mutable and immutable behavior. [4.1 Mutable and immutable data types, 4.2 List and tuple data types]

### 4.2 List and tuple data types & 4.3 Dictionary data types

- With example, explain following data structures in python: a) List b) Tuple c) Dictionary. [6 marks] (2081 Ashwin - IOE)

### 4.3 Dictionary data types

- Write a program to count the frequency of each character in a given string using a dictionary. [4.3 Dictionary data types, 4.4 Sequence data types]

### 4.5 Two-dimensional lists

- Using two-dimensional list, write a program to add two matrices and create the third matrix and display it. [4 marks] (2081 Ashwin - IOE)

### 4.6 Set data types

- Write a program demonstrating set operations: create two sets of integers, then display their union, intersection, difference, and symmetric difference. [4.6 Set data types]

### 4.7 Lambda

- Explain the significance of lambda function with an example. [2 marks] (2082 Baishakh - IOE)
- Write a program that takes a list of numbers from the user and uses a lambda function with `filter()` to display only the even numbers, and another lambda with `map()` to display the square of each number. [4.7 Lambda]
- Write a program using list comprehension to generate a list of squares of all odd numbers from 1 to 20, and use a lambda function to sort a list of tuples `[(3,"c"), (1,"a"), (2,"b")]` by the second element. [4.7 Lambda, 4.8 Operation of mutable and immutable data types]

---

## 5 Object Oriented Programming (12 hours)

### 5.1 Concepts of object-oriented programming

- Explain the benefits of object-oriented programming over procedural programming. [6 marks] (2082 Baishakh - IOE)

### 5.2 Classes and objects

- In object-oriented programming, explain the concept of constructor. Write a python code to illustrate the concept of constructor. Define a class with `__init__()` and `__str__()` methods. [2+4 marks] (2081 Ashwin - IOE)
- Write a class `Student` with attributes `name` and `marks`. Implement an iterator in the class that iterates over the marks list. [5.2.4 Iterator in a class]

### 5.3 Aggregation and composition

- Write a program demonstrating **aggregation and composition**. Create a class `Engine` and a class `Car` that contains an `Engine` object. Show how the lifetime of `Engine` depends on `Car` (composition) vs. exists independently (aggregation). [5.3 Aggregation and composition]

### 5.4 Inheritance

- Write python code to explain the concept of Single, Hierarchical and multi-level inheritance. [6 marks] (2081 Ashwin - IOE)

### 5.5 Polymorphism and dynamic binding

- Explain the concept of dynamic binding. Write python code to illustrate concept of abstract class. [2+4 marks] (2082 Baishakh - IOE)

### 5.6 Operator overloading in Python

- Using concept of binary operator overloading, find the sum of complex numbers. Use class called as complex, with two attributes: [real and imaginary]. [6 marks] (2082 Baishakh - IOE)
- Write a program to create a class called **Time** with attributes (**hour, minute and second**) to represent time and add time objects and return the result. [6 marks] (2081 Ashwin - IOE)
- Write a program that creates a class `Vector` with attributes `x` and `y`. Overload the `+` operator to add two vectors, the `==` operator to compare two vectors, and the `-` (unary) operator to negate a vector. [5.6.1 Arithmetic operators, 5.6.3 Comparison operators, 5.6.5 Unary operators]

---

## 6 Exceptions and File Handling in Python (5 hours)

### 6.1 Types of errors & 6.7 Introduction to file handling

- Explain different types of errors in python program. Write a python program to create a file called "record.txt" and use it to store the information of two students [Name, Roll No and college Name]. Ask user to enter the information. [2+4 marks] (2081 Ashwin - IOE)

### 6.2 Types of exceptions & 6.3 Catching and handling exceptions

- Define exception. You cannot divide a given number by zero. Based on given statement, write python code to handle the given exception. [2+4 marks] (2082 Baishakh - IOE)

### 6.4 User-defined exceptions

- Write a program that defines a **user-defined exception** `InvalidAgeError`. Ask the user for their age; if the age is less than 0 or greater than 150, raise the custom exception with an appropriate message. [6.4 User-defined exceptions]

### 6.5 Debugging programs with the assert statement & 6.6 Logging the exceptions

- Write a program that uses the `assert` statement to verify that a function `calculate_area(radius)` receives a positive radius. If assertion fails, catch the `AssertionError` and print a debug message using the `logging` module. [6.5 Debugging programs with the assert statement, 6.6 Logging the exceptions]

### 6.8 Opening and closing a file & 6.9 Working with text and binary files

- Write a program to read a text file, count the number of words and lines, and write the result to a new file. Handle the case where the input file does not exist using exception handling. [6.7 Introduction to file handling, 6.8 Opening and closing a file, 6.9 Working with text and binary files]
- Write a program that writes a list of student records (name, roll, marks) to a **binary file** using the `pickle` module, then reads and displays them. [6.9 Working with text and binary files]

---

## 7 Python Libraries and Maths (10 hours)

### 7.1 Modules, packages and libraries

- Discuss the difference between a Python module, package, and library. What are the different ways to import modules? [3+3 marks] (2082 Baishakh - IOE)
- Write a Python program that creates a custom module `mathutils.py` with functions `factorial(n)`, `is_even(n)`, and `gcd(a, b)`. Import and use this module in another script using different import methods (`import`, `from...import`, `import...as`). [7.1 Modules, packages and libraries]

### 7.5 Introduction to the numPy library

- Explain the advantages of using NumPy array over python sequences with an example. [3 marks] (2081 Ashwin - IOE)

### 7.6 Creating, indexing and slicing numPy arrays & 7.7 Copying and editing numPy arrays

- Write a program to create a NumPy array, demonstrate indexing, slicing, and copying (shallow vs deep copy). Modify the copy and show that the original array remains unchanged. [7.6 Creating, indexing and slicing numPy arrays, 7.7 Copying and editing numPy arrays]

### 7.8 Stacking and restructuring numPy arrays & 7.14 Applications of numPy linear algebra

- How do you reshape a NumPy array? Write a program to solve following system of linear equations using NumPy: [2+4 marks] (2082 Baishakh - IOE)
  $$2x + 3y = 12$$
  $$4x - 5y = -2$$
- Write a program to create a 1D NumPy array of 12 elements, reshape it into a 3×4 matrix, then vertically stack it with its transpose (after reshaping). Display the original and resulting arrays. [7.8 Stacking and restructuring numPy arrays]

### 7.9 Arithmetic operations with numPy arrays

- Write a python program to create two 2X2 NumPy arrays and performs matrix addition, subtraction and element-wise multiplication and display the result. [9 marks] (2081 Ashwin - IOE)

### 7.10 Operations with numPy arrays of different shapes

- Write a program using NumPy to create two arrays of different shapes and demonstrate **broadcasting** by performing addition between them. [7.10 Operations with numPy arrays of different shapes]

### 7.12 Applications of numPy random number generation & 7.13 Applications of numPy statistics

- Write a program to create a NumPy array of 20 random integers between 1 and 100, then find and display the mean, median, standard deviation, and variance using NumPy functions. [7.12 Applications of numPy random number generation, 7.13 Applications of numPy statistics]
