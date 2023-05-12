---
title: Review 2
permalink: /docs/review2/
---

**Second Practicum**: Tuesday, June 13th

**Time**: 50 minutes

**Location**: Barnard 126

The exam will emphasize (1) Dictionaries and (2) Object Oriented Programming. The assignments and active learning exercises should help reinforce your understanding.

To answer a question, you might need to build on knowledge that you learned previously.

You may bring one 8.5 inch by 11 inch sheet of double-sided notes.

You may use a computer to develop your answers. You may only use the internet to access the interactive python textbook, the online python documentation or previous python programs that you (or you and your partner) wrote for this course.

To be successful on the exam, strive to understand the Python material and be able to use it to solve small problems.

[Practice Practicum](../lessons/code/practice2.pdf)

## Object Oriented Terminology
- Class
- Object (or Instance)
- Method
- Special Methods: Constructor, Reader Method, Writer Method
- More Special Methods: `__str__`, `__add__`
- Instance Variable (or State Variable)
- Encapsulation
- Inheritance
- Polymorphism

## Object Oriented Problem Example
We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a **Rectangle** class using this idea. The following statement should create a Rectangle object at location (4,5) with width 6 and height 5:

```
r = Rectangle(Point(4, 5), 6, 5)
```

## Object Oriented Problem Example
Supply the missing class in [oop.py](../lessons/code/oop.py) such that the following output is produced when the program is run:
```
Montana State beat Idaho State on 3/11/2022: 62 to 56
Washington beat Montana State on 3/18/2023: 91 to 63
```