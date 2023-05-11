---
title: Lab 13 pandas
permalink: /docs/lab13/
---

## Logistics
**Due**: Wednesday, June 21st no later than 11:58 p.m.

**Partner Information**: Complete this assignment individually.

**Submission Instructions**: Upload your solution, named **YourFirstName-YourLastName-Lab13.py** to the BrightSpace **Lab 13** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Gain experience creating bar charts with pandas.

## Assignment
Download [lab13.py](../lessons/code/lab13.py), rename it according to the instructions above, and make sure you understand it.

Download [MSU College Enrollments.csv](../lessons/code/msu_college_enrollments.csv) and [CS Faculty](../lessons/code/cs_faculty.csv).csv into the same directory as the above file.
Modify the program so that when it runs, Figure 1 looks [like this](../lessons/code/figure1.png) and Figure 2 looks [like this](../lessons/code/figure2.png). Note: To see the xlabel after the figure is displayed, select the "Configure subplots" button at the bottom of the displayed graph and then increase the "bottom" slider manually.

## Grading - 10 points
2 points - A dataframe is created using the `read_csv` method.

1 points - The labels for the x-axis and y-axis are determined by information in the dataframe. Thus, any csv file that has the same format as the two files being used in lab would display correctly.

1 points - The title for the graph is determined by the information in the string parameter `file_name` that comes before the ".csv" file extension.

6 points - The dataframe plot method uses each of the following arguments correctly such that the sample graphs are matched exactly: title, legend, x, y, kind and color correctly. 1 point each.

## If Time Remains
Work on Program 6, seeking feedback if desired.