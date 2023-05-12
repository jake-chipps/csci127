---
title: Lab 11 NumPy arrays
permalink: /docs/lab11/
---

## Logistics
**Due**: Friday, June 16th no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, named **YourFirstName-YourLastName-Lab11.py** to the BrightSpace **Lab 11** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Gain experience using NumPy arrays to solve problems.

## Background
In a modified game of Yahtzee, five eight-sided dice are rolled once.

For this assignment, you will simulate this modified game of Yahtzee to determine how likely certain outcomes are.

In this modified version of Yahtzee, a **Low Roll** occurs when each of the five dice is either a 1 or an 2. For example, 1-1-1-1-1 or 2-2-1-2-1.

In this modified version of Yahtzee, a **Three of a Kind** occurs when three of the dice show the same number. The other two dice must not show this number and must also be different from one another. For example, 4-7-4-4-2 but not 4-7-4-4-7.

In this modified version of Yahtzee, a **large straight** occurs when the five numbers can be arranged consecutively (for example, 1-3-4-2-5 or 5-7-4-6-3). Hint: the numpy library contains a sort function.

## Assignment
Download [lab11.py](../lessons/code/lab11.py), rename it according to the instructions above, and make sure you understand it.

Take the program above and modify it by adding the missing methods such that when the program is run, it might produce [this output](../lessons/code/lab11_output.txt). Do not change any of the existing Python code.

## Grading - 10 points
3 points - Low Rolls are identified correctly.

3 points - Three of a Kinds are identified correctly.

4 points - Large straights are identified correctly.