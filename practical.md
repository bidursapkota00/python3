# Code Questions (Chapter 3–7)

## 3 Basic Programming Concept in Python (5 hours)

1. Write a program that takes a number from the user and checks whether it is positive, negative, or zero using conditional statements. [3.5 Conditional statement]

2. Write a program using a `for` loop to print the multiplication table of a given number entered by the user. [3.6 Loop]

3. Write a function `is_prime(n)` that takes a number as argument and returns `True` if it is a prime number, else `False`. Use this function to display all prime numbers between 1 and 100. [3.7 Functions]

4. Write a program to find the factorial of a number using both iterative (loop) and recursive approaches. [3.6 Loop, 3.8 Recursion]

5. *(Past Question)* Define recursive function. Write a program to find the $n^{th}$ term of Fibonacci series using recursive function. [2+4 marks] (2082 Baishakh - IOE) [3.8 Recursion]

6. Write a program that reads two numbers and an operator (+, -, *, /) from the user and performs the corresponding arithmetic operation. Handle division by zero with an appropriate message. [3.4 Logic and comparison operations, 3.5 Conditional statement]

---

## 4 Advanced Data Types and Operation in Python (8 hours)

1. *(Past Question)* For the given list of dictionaries, find the TOTAL MARKS obtained: `d = [{"subject":"math","marks":80}, {"subject":"science","marks":90}, {"subject":"english","marks":80}]` [4 marks] (2082 Baishakh - IOE) [4.1 Mutable and immutable, 4.3 Dictionary]

2. *(Past Question)* Using two-dimensional list, write a program to add two matrices and create the third matrix and display it. [4 marks] (2081 Ashwin - IOE) [4.5 Two-dimensional lists]

3. Write a program that takes a list of numbers from the user and uses a lambda function with `filter()` to display only the even numbers, and another lambda with `map()` to display the square of each number. [4.7 Lambda]

4. Write a program to create a tuple of student names, convert it to a list, add a new name, sort the list, and convert it back to a tuple. Demonstrate the difference between mutable and immutable behavior. [4.1 Mutable and immutable, 4.2 List and tuple]

5. Write a program to count the frequency of each character in a given string using a dictionary. [4.3 Dictionary, 4.4 Sequence data types]

6. Write a program demonstrating set operations: create two sets of integers, then display their union, intersection, difference, and symmetric difference. [4.6 Set data types]

7. Write a program using list comprehension to generate a list of squares of all odd numbers from 1 to 20, and use a lambda function to sort a list of tuples `[(3,"c"), (1,"a"), (2,"b")]` by the second element. [4.7 Lambda, 4.8 Operations]

---

## 5 Object Oriented Programming (12 hours)

1. *(Past Question)* Write a python code to illustrate the concept of constructor. Define a class with `__init__()` and `__str__()` methods. [2+4 marks] (2081 Ashwin - IOE) [5.2 Classes and objects]

2. *(Past Question)* Write python code to explain the concept of Single, Hierarchical and Multi-level inheritance. [6 marks] (2081 Ashwin - IOE) [5.4 Inheritance]

3. *(Past Question)* Using concept of binary operator overloading, find the sum of complex numbers. Use a class called `Complex`, with two attributes: `real` and `imaginary`. [6 marks] (2082 Baishakh - IOE) [5.6 Operator overloading]

4. *(Past Question)* Write a program to create a class called **Time** with attributes (**hour, minute and second**) to represent time and add time objects and return the result. [6 marks] (2081 Ashwin - IOE) [5.6 Operator overloading]

5. *(Past Question)* Write python code to illustrate the concept of abstract class using the `abc` module. [4 marks] (2082 Baishakh - IOE) [5.5 Polymorphism and dynamic binding]

6. Write a class `Student` with attributes `name` and `marks`. Implement an iterator in the class that iterates over the marks list. [5.2.4 Iterator in a class]

7. Write a program demonstrating **aggregation and composition**. Create a class `Engine` and a class `Car` that contains an `Engine` object. Show how the lifetime of `Engine` depends on `Car` (composition) vs. exists independently (aggregation). [5.3 Aggregation and composition]

8. Write a program that creates a class `Vector` with attributes `x` and `y`. Overload the `+` operator to add two vectors, the `==` operator to compare two vectors, and the `-` (unary) operator to negate a vector. [5.6.1 Arithmetic, 5.6.3 Comparison, 5.6.5 Unary operators]

---

## 6 Exceptions and File Handling in Python (5 hours)

1. *(Past Question)* You cannot divide a given number by zero. Based on given statement, write python code to handle the given exception using try-except. [2+4 marks] (2082 Baishakh - IOE) [6.2, 6.3 Exceptions]

2. *(Past Question)* Write a python program to create a file called "record.txt" and use it to store the information of two students [Name, Roll No and College Name]. Ask user to enter the information. [4 marks] (2081 Ashwin - IOE) [6.7, 6.8 File handling]

3. Write a program that defines a **user-defined exception** `InvalidAgeError`. Ask the user for their age; if the age is less than 0 or greater than 150, raise the custom exception with an appropriate message. [6.4 User-defined exceptions]

4. Write a program that uses the `assert` statement to verify that a function `calculate_area(radius)` receives a positive radius. If assertion fails, catch the `AssertionError` and print a debug message using the `logging` module. [6.5 Debugging with assert, 6.6 Logging]

5. Write a program to read a text file, count the number of words and lines, and write the result to a new file. Handle the case where the input file does not exist using exception handling. [6.7–6.9 File handling, 6.3 Exceptions]

6. Write a program that writes a list of student records (name, roll, marks) to a **binary file** using the `pickle` module, then reads and displays them. [6.9 Working with binary files]

---

## 7 Python Libraries and Maths (10 hours)

1. *(Past Question)* Write a python program to create two 2×2 NumPy arrays and perform matrix addition, subtraction and element-wise multiplication and display the result. [9 marks] (2081 Ashwin - IOE) [7.9 Arithmetic operations with NumPy]

2. *(Past Question)* Write a program to solve the following system of linear equations using NumPy: [4 marks] (2082 Baishakh - IOE) [7.14 NumPy linear algebra]
   $$2x + 3y = 12$$
   $$4x - 5y = -2$$

3. Write a program to create a NumPy array of 20 random integers between 1 and 100, then find and display the mean, median, standard deviation, and variance using NumPy functions. [7.12 Random number generation, 7.13 NumPy statistics]

4. Write a program to create a 1D NumPy array of 12 elements, reshape it into a 3×4 matrix, then vertically stack it with its transpose (after reshaping). Display the original and resulting arrays. [7.8 Stacking and restructuring]

5. Write a Python program that creates a custom module `mathutils.py` with functions `factorial(n)`, `is_even(n)`, and `gcd(a, b)`. Import and use this module in another script using different import methods (`import`, `from...import`, `import...as`). [7.1 Modules, packages and libraries]

6. Write a program to create a NumPy array, demonstrate indexing, slicing, and copying (shallow vs deep copy). Modify the copy and show that the original array remains unchanged. [7.6 Indexing and slicing, 7.7 Copying and editing]

7. Write a program using NumPy to create two arrays of different shapes and demonstrate **broadcasting** by performing addition between them. [7.10 Operations with arrays of different shapes]
