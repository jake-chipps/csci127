---
title: Lab 2 Functions and Selection Statements
permalink: /docs/lab2/
---

## Logistics
**Due**: Tuesday, May 23rd no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, renamed to **YourFirstName-YourLastName-Lab2.py** to the BrightSpace **Lab 2** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Gain experience writing a Python function.
- Gain experience writing Python selection statements.

## Assignment
Download [lab2.py](../lessons/code/lab2.py) and rename it according to the instructions above.

Modify the program by adding the missing function. The missing function will use Python selection statements to calculate the amount of tax that a single (unmarried) taxpayer owes using the table below. If the missing function is implemented correctly, this output will appear.

[2022 Federal Tax Bracket](https://taxfoundation.org/2022-tax-brackets/)

Note: the federal tax is progressive. For example, a person with a taxable income of $90,000 is taxed at a rate of 10% for the first $10,275:

```
current_tax = .1 * 10275
remaining_income = income - 10275
```

Then $41,775 of the remaining $79,725.00 is taxed at a rate of 12%:

```
current_tax = current_tax + .12 * 41775
remaining_income = remaining_income - 41775
```

Since the remaining income ($37,950.00) is less than the value of the next bracket ($89,075), the rest is taxed at 22%:

```
current_tax = current_tax + .22 * remaining_income
```


| Rate | For Unmarried Individuals, Taxable Income Over | 
| --- | --- |
| 10% |	$0 |
| 12% | $10,275 |
| 22% | $41,775 |
| 24% | $89,075 |
| 32% | $170,050 |
| 35% | $215,950 |
| 37% | $539,900 |

## Grading - 10 points
7 points - Your program calculates the income tax for each of the seven test cases correctly (1 point each).

3 points - A function with the correct name (1 point), correct parameters (1 point) and correct return value (1 point) is used in the solution.

## If Time Remains
If you want to work with a partner on Program 1 (due May 29th), use this time to identify a partner or ask your lab TA to help you find someone. Note: For the vast majority of computing jobs and internships, the ability to work with one or more teammates is a crucial skill!