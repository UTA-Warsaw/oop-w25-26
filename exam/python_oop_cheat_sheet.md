# 🐍 Python Object-Oriented Programming (OOP) Cheat Sheet

A concise reference for Object-Oriented Programming concepts in Python.

---

## 1. Class & Object

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def bark(self):
        return "Woof!"

dog = Dog("Rex", 3)
dog.bark()
```

- **Class** → blueprint
- **Object** → instance of a class
- `self` → reference to the current object

---

## 2. `__init__` (Constructor)

```python
def __init__(self, x, y):
    self.x = x
    self.y = y
```

- Runs automatically when an object is created
- Used to initialize attributes

---

## 3. Instance vs Class Variables

```python
class Car:
    wheels = 4          # class variable (shared)

    def __init__(self, brand):
        self.brand = brand  # instance variable
```

```python
Car.wheels        # 4
car1.wheels       # 4
```

---

## 4. Instance, Class & Static Methods

```python
class Math:
    pi = 3.14

    def square(self, x):          # instance method
        return x * x

    @classmethod
    def circle_area(cls, r):      # class method
        return cls.pi * r * r

    @staticmethod
    def add(a, b):                # static method
        return a + b
```

| Method Type | Uses | Decorator |
|-----------|------|----------|
| Instance | Object data | none |
| Class | Class data | `@classmethod` |
| Static | Utility logic | `@staticmethod` |

---

## 5. Inheritance

```python
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "Meow"
```

```python
cat = Cat()
cat.speak()
```

---

## 6. `super()`

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
```

---

## 7. Encapsulation

```python
class Bank:
    def __init__(self):
        self.balance = 0
        self._rate = 0.05
        self.__pin = 1234
```

---

## 8. Getters & Setters (`@property`)

```python
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value
```

---

## 9. Polymorphism

```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        return "Can't fly"
```

---

## 10. Magic (Dunder) Methods

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"{self.pages} pages"

    def __len__(self):
        return self.pages
```

---

## 11. Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 12. Composition (HAS-A)

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## 13. Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## 14. OOP Principles (SOLID)

- **S**ingle Responsibility
- **O**pen / Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion
