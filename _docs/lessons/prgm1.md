---
title: Program 1 Liberty Bell Slot Machine Simulation
permalink: /docs/prgm1/
---

## Logistics
**Due Date**: Monday, May 29th no later than 11:58 p.m.

**Partner Information**: You may complete this assignment individually or with exactly one partner. If you work with a partner, you must both be enrolled in the same lab section or you will both lose 10 points.

**Submission Instructions (working alone)**: Upload your solution, entitled **YourFirstName-YourLastName-Program1.py** to the BrightSpace **Program 1** Dropbox.

**Submission Instructions (working with one lab mate)**: Upload your solution, entitled **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program1.py** to the BrightSpace **Program 1** Dropbox. Note: If you work with a partner, only one person needs to submit a solution. If you both submit a solution, the submission that will be graded is the one from the partner whose last name comes alphabetically first.

**Deadline Reminder**: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- To solve this problem, you need to understand the following Python concepts: data types, functions, selection statements and iteration.

## Background Information
Charles Fey constructed the first slot machine in 1895. The original machine consisted of three spinning reels containing a total of five symbols: horseshoes, diamonds, spades, hearts and a bell (the Liberty Bell), from which this machine took its name. It cost 5 cents to play and the payouts worked as follows:
- three Liberty Bells: 50 cents
- three hearts: 40 cents
- three diamonds: 30 cents
- three spades: 20 cents
- three horseshoes: 10 cents
- two horseshoes and any other one symbol: 5 cents
- all other combinations: nothing

To learn more about a subsequent, six-symbol Liberty Bell slot machine, check out this [wikipedia article](https://en.wikipedia.org/wiki/Liberty_Bell_(game)).

## Assignment
Download [Program1.py](../lessons/code/Program1.py), rename it according to the instructions above, and make sure you fully understand it.

Write the missing `spin_payout` function such that it returns the correct payout for any spin.

Write the missing `simulate` function such that it simulates the handle of the slot machine being pulled the specified number of times. The simulation may assume that for each reel, the probability of generating any of the five symbols is the same. Once the simulation is finished, the function should print a message stating how much money can be expected to be won for each $1 spent.

Here is a [sample transcript](../lessons/code/program1_trascript.txt) of the program running. Your solution should match the output format exactly. However, because of randomness, the expected winnings per dollar spent might vary each time the program is run.

## Grading - 100 points
50 points - Each of the ten test spins is calculated correctly in a general fashion. (5 points each - all or nothing.)

20 points - The `spin_payout` function conforms to its comment (5 points), uses meaningful user chosen names (5 points), uses if constructs effectively (5 points) and is as simple as possible (5 points).

15 points - The `simulate` function conforms to its comment (5 points), uses meaningful user chosen names (5 points), and is as simple as possible (5 points).

5 points - With the exception of the expected winnings, the output format matches the output format of the transcript exactly. All or nothing.

5 points - The expected winning is displayed with two digits to the right of the decimal. All or nothing.

5 points - The submitted file is named correctly. All or nothing.