---
title: Lab 10 Object Oriented Programming
permalink: /docs/lab10/
---

## Logistics
**Due**: Wednesday, June 14th no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, renamed to **YourFirstName-YourLastName-Lab10.py** to the BrightSpace **Lab 10** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcome
- Gain more experience with object oriented programming.

## Assignment
In this assignment, you will use object-oriented programming to implement a data structure called a **queue**. An example of a queue is a concert line for tickets (with no cutting allowed): the first person to arrive goes first, the second person to arrive goes second, etc. The line can grow and shrink dynamically over time.

Download [lab10.py](../lessons/code/lab10.py), rename it according to the instructions above, and make sure you understand it.

Take the program above and modify it by adding the missing Queue class such that when the program is run, it produces [this output](../lessons/code/lab10_output.txt).

## Grading - 10 points
1 points - The constructor of the Queue class is correct.

1 points - The `enqueue` method of the Queue class is correct. The method adds an item to the queue.

1 points - The `dequeue` method of the Queue class is correct. The method removes and returns the item that has been in the queue the longest.

1 points - The `is_empty` method of the Queue class is correct. A queue is empty when it contains no items.

2 points - The `__str__` method of the Queue class is correct.

3 points - In the main function, the statement number `+= 15` is implemented correctly using the appropriate [magic method](https://python-course.eu/oop/magic-methods.php) in the Queue class.