---
title: Lab 6 Files
permalink: /docs/lab6/
---

## Logistics
**Due**: Sunday, June 4th no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, renamed to **YourFirstName-YourLastName-Lab6.py** to the BrightSpace **Lab 6** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Gain experience with files.

## Assignment
Download the file [earthquakes.csv](../lessons/code/earthquakes.csv). This input file is described in detail [here](https://think.cs.vt.edu/corgis/csv/earthquakes/).

Download [lab6.py](../lessons/code/lab6.py) into the same directory where the earthquakes.csv file is located and rename it according to the instructions in the Logistics section.

Implement the `average_magnitude` function such that it calculates and returns the average magnitude of the recorded earthquakes.

Implement the `earthquake_locations` function such that it identifies every unique location (use the name field in the file) and prints them in alphabetical order.

Implement the `count_earthquakes` function. The function should calculate the number of recorded earthquakes that have a magnitude greater than or equal to the low bound and less than or equal to the high bound. The user will specify the bounds and you may assume that the user will enter valid numbers.

## Sample Run
In this [sample run](../lessons/code/lab6_output.txt), the user inputs 5.0 for the lower bound and 6.0 for the upper bound.

## Grading - 10 points
2 points - The `average_magnitude` function is correct.

3 points - The `earthquake_locations` function finds all of the unique locations (2 points) and prints each unique location once in sorted order (1 point).

3 points - The `count_earthquakes` function is correct. The function will be tested on a different case that will be revealed after the lab is submitted.

2 points - The format of the output matches exactly the format of the output transcript. For each type of difference, 1 point will be deducted.