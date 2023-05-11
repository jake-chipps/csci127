---
title: Lab 12 matplotlib
permalink: /docs/lab12/
---

## Logistics
**Due**: Monday, June 19th no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, named **YourFirstName-YourLastName-Lab12.py** to the BrightSpace **Lab 12** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Gain experience with matplotlib to display information.
- Continue to gain experience with numpy.

## Background
The Registrars Office at Montana State University makes various [enrollment statistics](https://www.montana.edu/opa/enrollment/199970/index.html) available.

The file, [fall-2019.csv](../lessons/code/fall-2019.csv) captures some of the information that is available in the Fall 2019 Report G - Part A: Headcount Enrollment, All Students by Primary Major. The first line contains how many lines of data follow. Each subsequent line contains the name of one of MSU's colleges (such as CLS for the College of Letters & Science) followed by the Fall 2019 enrollment for that college.

Use [lab12.py](../lessons/code/lab12.py), renamed according to the instructions above, as a starting point.

The `read_file` function should return:
1. a numpy array that contains each college name and
2. a corresponding numpy array that contains each college's enrollment.

The `main` function should produce the desired bar graph using the information contained in the numpy arrays named `college_names` and `college_enrollments`.

## Assignment
Write a program that matches [this graph](../lessons/code/graph.png) as closely as possibly.

## Grading - 10 points
Each of the following categories are all or nothing:

1 point - The upper gray bar contains the words *Montana State University Fall 2019 Enrollments*.

1 point - The x-axis is labeled *College Name* and the y-axis is labeled *College Enrollment*.

1 point - The y-axis goes from 0 to 4400 in increments of 400.

1 point - The x-axis contains the same college names that appear in the input file.

2 points - The bar graph reflects the data in the file accurately.

1 point - The colors of the bars in the bar graph alternate between "blue" and "gold".

2 points - The function `read_file` returns:
1. one numpy array that contains the names of the colleges and
2. a second numpy array that contains the enrollments of the colleges.

1 point - The bar graph is created and plotted entirely in the `main` function.

## If Time Remains
Work on Program 5, seeking feedback from your lab assistant if desired.