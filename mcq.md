## Advanced Computer Programming

**Name: .....................................**

**Roll: ........................................**

1. How to access `acc.__balance` from outside `BankAccount`, and what does this imply?
   A) `acc.__balance`, proving strict data hiding.
   B) `acc._BankAccount__balance`, proving name mangling.
   C) `acc._balance`, double underscores become single.
   D) Inaccessible, ensuring complete memory security.

2. How does composition differ from aggregation regarding garbage collection?
   A) Composition: independent lifecycle; Aggregation: shared lifecycle.
   B) Composition: destroying container destroys object; Aggregation: object outlives container.
   C) Composition uses `super()`; Aggregation uses multiple inheritance.
   D) No difference; both are 'is-a' relationships.

3. `Shape` defines abstract `area()`. `Circle` inherits but forgets to implement `area()`. What happens when instantiating `Circle`?
   A) Instance created, calling `area()` raises `NotImplementedError`.
   B) `TypeError` on instantiation (cannot instantiate abstract class).
   C) Instance created, `area()` returns `None`.
   D) `SyntaxError` during class definition.

4. Which two dunder methods satisfy the Python iterator protocol?
   A) `__iter__()` and `__len__()`
   B) `__iter__()` and `__next__()`
   C) `__next__()` and `__str__()`
   D) `__getitem__()` and `__iter__()`

5. Which method implements the unary negation operator (`-obj`)?  
   A) `__minus__()`
   B) `__sub__()`
   C) `__neg__()`
   D) `__invert__()`

6. `Dog` overrides `Animal.eat()`. Best practice for `Dog.eat()` to extend `Animal.eat()`'s logic?
   A) Call `Animal.eat(self)`.
   B) Call `super().eat()`.
   C) Copy `Animal.eat()` code.
   D) Redefine as `__eat__()`.

7. Sequence of execution in `try-except-else-finally` if `try` executes without exceptions?
   A) `try` -> `except` -> `finally`
   B) `try` -> `else` -> `finally`
   C) `try` -> `finally`
   D) `try` -> `else` (no `finally`)

8. Why is catching all exceptions with the base `Exception` class considered poor practice?
   A) Prevents `finally` block execution.
   B) Masks unexpected errors.
   C) Automatically raises `SystemExit`.
   D) Converts runtime errors to syntax errors.

9. File mode to append new data to the end and read the entire file?
   A) `w+`
   B) `r+`
   C) `a+`
   D) `w`

10. Opened in text mode (`'r+'`), `f.seek(-5, 2)` is called. Expected outcome?
    A) Moves 5 bytes backward from the end.
    B) Python raises an error.
    C) Moves to the beginning.
    D) `ValueError` (negative offsets not allowed).
