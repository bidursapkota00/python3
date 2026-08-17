## Advanced Computer Programming

**Name: .....................................**

**Roll: ........................................**

1. Consider a class `BankAccount` with an attribute `__balance`. If an object `acc` is instantiated, how can a programmer access this attribute from outside the class, and what does this imply about Python's encapsulation?
   A) By accessing `acc.__balance`, proving Python has strict data hiding.
   B) By accessing `acc._BankAccount__balance`, proving Python uses name mangling rather than strict access control.
   C) By accessing `acc._balance`, as Python implicitly changes double underscores to single underscores.
   D) It cannot be accessed in any way, ensuring complete memory security.

2. In the context of object relationships, how does composition differ from aggregation in Python, specifically regarding the garbage collection of contained objects?
   A) In composition, the contained object's lifecycle is independent of the container, while in aggregation, they share the same lifecycle.
   B) In composition, destroying the container implies the destruction of the contained object, whereas in aggregation, the contained object outlives the container.
   C) Composition uses the `super()` function, while aggregation relies on multiple inheritance.
   D) There is no difference; both are simply variations of the 'is-a' relationship.

3. An abstract class `Shape` defines an abstract method `area()`. A child class `Circle` inherits from `Shape` but forgets to implement the `area()` method. What occurs when you try to instantiate `Circle`?
   A) An instance is created, but calling `area()` raises a `NotImplementedError`.
   B) A `TypeError` is raised at the time of instantiation, stating that it cannot instantiate an abstract class.
   C) The instance is created successfully, and `area()` returns `None` by default.
   D) A `SyntaxError` occurs during the class definition of `Circle`.

4. You want to create a custom iterable class. Which two dunder methods must be implemented to fully satisfy the Python iterator protocol?
   A) `__iter__()` and `__len__()`
   B) `__iter__()` and `__next__()`
   C) `__next__()` and `__str__()`
   D) `__getitem__()` and `__iter__()`

5. In Python, operator overloading is used to define custom behaviors for operators. If you want an object `obj` to support the unary negation operator (`-obj`), which method must you implement?  
   A) `__minus__()`
   B) `__sub__()`
   C) `__neg__()`
   D) `__invert__()`

6. Consider a class hierarchy where `Dog` inherits from `Animal`. `Animal` has an `eat()` method, and `Dog` overrides it. If you want `Dog`'s `eat()` method to execute its own logic but also extend `Animal`'s `eat()` logic, what is the best practice?
   A) Call `Animal.eat(self)` inside `Dog`'s `eat()` method.
   B) Call `super().eat()` inside `Dog`'s `eat()` method.
   C) Copy the code from `Animal`'s `eat()` method into `Dog`'s `eat()` method.
   D) Redefine the method as `__eat__()` in the child class.

7. Consider a `try-except-else-finally` block. If the code inside the `try` block executes without raising any exceptions, what is the sequence of execution?
   A) `try` -> `except` -> `finally`
   B) `try` -> `else` -> `finally`
   C) `try` -> `finally`
   D) `try` -> `else` (the `finally` block is skipped if no error occurs)

8. A programmer writes a block of code to catch exceptions. They use `except Exception as e:` at the top. Why is catching all exceptions with the base `Exception` class generally considered poor practice?
   A) It prevents the `finally` block from executing.
   B) It masks unexpected errors.
   C) It automatically raises a `SystemExit` exception.
   D) It converts all runtime errors into syntax errors.

9. A developer needs to open a file, write new logs to the end without overwriting existing data, and be able to read the entire file. Which file mode should they use in the `open()` function?
   A) `w+`
   B) `r+`
   C) `a+`
   D) `w`

10. Using random file access in Python, a file is opened in text mode (`'r+'`). The developer attempts to seek backwards from the end of the file using `f.seek(-5, 2)`. What is the expected outcome and why?
    A) The pointer successfully moves 5 bytes backwards from the end of the file.
    B) Python raises an error.
    C) The pointer moves to the beginning of the file.
    D) It raises a `ValueError` because negative offsets are never allowed in Python.
