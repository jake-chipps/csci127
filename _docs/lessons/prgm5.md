---
title: Program 5 Wacky Packages
permalink: /docs/prgm5/
---

## Logistics
**Due Date**: Tuesday, June 20th no later than 11:58 p.m.

**Partner Information**: You may complete this assignment individually or with exactly one partner. If you work with a partner, you must both be enrolled in the same lab section. (Otherwise, you and your partner will receive no credit.)

**Submission Instructions (working alone)**: Upload your solution, entitled **YourFirstName-YourLastName-Program5.py** to the BrightSpace **Program 5** Dropbox.

**Submission Instructions (working with one lab mate)**: Upload your solution, renamed to **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program5.py** to the BrightSpace **Program 5** Dropbox. Note: If you work with a partner, only one person needs to submit a solution. If you both submit a solution, the submission that will be graded is the one from the partner whose last name comes alphabetically first.

**Deadline Reminder**: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- Utilize NumPy arrays to solve a problem.
- Utilize object-oriented programming to solve a problem.

## Wacky Packages Background
Wacky Packages were issued by the Topps Chewing Gum Company to spoof well-known brands.

[This page](https://wackypacks.com/stickers/1st_series/whitebacks/album_smaller_images.html) shows the the fronts of 30 cards that were issued in 1973.

For this assignment, you are going to write a program that keeps track of a Wacky Packages collection.

The values of the cards are taken from the NM-MT 8 (near mint 8) condition category on [this page](https://www.psacard.com/priceguide/non-sports-tcg-card-values/1973-wacky-packages-series-1/1003).

## Assignment
Using [program5.py](../lessons/code/program5.py) as a starting point, supply the missing **WackyPackageSeries** methods such that [this output](../lessons/code/program5_output.txt) is produced when the program is run using input files [series1.csv](../lessons/code/series1.csv) and [mycards.csv](../lessons/code/mycards.csv).

## Grading - 100 points
20 points. The **WackyPackageSeries** methods use object-oriented programming properly. In particular, these methods should not access individual fields of **WackyPackageCard** instances directly - instead, they should access these fields through the methods that are provided by the **WackyPackageCard** class. (5 points for each improper access up to 20 points.)

20 points. The `read_series_information` method results in the correct output being produced. (10 points for each type of error up to 20 points.)

20 points. The `read_collection_information` method results in the correct output being produced. (10 points for each type of error up to 20 points.)

10 points. The `__str__` method is correct. (5 points for each type of formatting difference up to 10 points.)

10 points. The `collection_value` method is correct. (All or nothing.)

10 points. The `determine_missing_information` method is correct. (All or nothing.)

10 points - The methods you write are properly commented, easy to understand and do not contain unnecessary code. (3 points for each type of improvement up to 10 points.)