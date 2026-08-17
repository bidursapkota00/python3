## Advanced Computer Programming

**Name: .....................................**

**Roll: ........................................**

1. How to access `acc.__balance` from outside `BankAccount`, and what does this imply?
   A) `acc.__balance`, proving strict data hiding.
   B) Inaccessible, ensuring complete memory security.
   C) `acc._BankAccount__balance`, proving name mangling.
   D) `acc._balance`, double underscores become single.

2. How does composition differ from aggregation regarding garbage collection?
   A) Composition: destroying container destroys object; Aggregation: object outlives container.
   B) Composition uses `super()`; Aggregation uses multiple inheritance.
   C) No difference; both are 'is-a' relationships.
   D) Composition: independent lifecycle; Aggregation: shared lifecycle.

3. `Shape` defines abstract `area()`. `Circle` inherits but forgets to implement `area()`. What happens when instantiating `Circle`?
   A) Instance created, calling `area()` raises `NotImplementedError`.
   B) Instance created, `area()` returns `None`.
   C) `SyntaxError` during class definition.
   D) `TypeError` on instantiation (cannot instantiate abstract class).

4. Which two dunder methods satisfy the Python iterator protocol?
   A) `__iter__()` and `__len__()`
   B) `__getitem__()` and `__iter__()`
   C) `__iter__()` and `__next__()`
   D) `__next__()` and `__str__()`

5. Which method implements the unary negation operator (`-obj`)?  
   A) `__minus__()`
   B) `__neg__()`
   C) `__sub__()`
   D) `__invert__()`

6. `Dog` overrides `Animal.eat()`. Best practice for `Dog.eat()` to extend `Animal.eat()`'s logic?
   A) Call `Animal.eat(self)`.
   B) Copy `Animal.eat()` code.
   C) Redefine as `__eat__()`.
   D) Call `super().eat()`.

7. Sequence of execution in `try-except-else-finally` if `try` executes without exceptions?
   A) `try` -> `except` -> `finally`
   B) `try` -> `else` -> `finally`
   C) `try` -> `finally`
   D) `try` -> `else` (no `finally`)

8. Why is catching all exceptions with the base `Exception` class considered poor practice?
   A) Masks unexpected errors.
   B) Prevents `finally` block execution.
   C) Automatically raises `SystemExit`.
   D) Converts runtime errors to syntax errors.

9. File mode to append new data to the end and read the entire file?
   A) `w+`
   B) `r+`
   C) `w`
   D) `a+`

10. Opened in text mode (`'r+'`), `f.seek(-5, 2)` is called. Expected outcome?
    A) Moves 5 bytes backward from the end.
    B) Moves to the beginning.
    C) Python raises an error.
    D) `ValueError` (negative offsets not allowed).
