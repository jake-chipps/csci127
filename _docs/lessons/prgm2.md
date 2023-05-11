---
title: Program 2 Poker Hand Evaluation
permalink: /docs/prgm2/
---

## Logistics
**Due Date**: Friday, June 2nd no later than 11:58 p.m.

**Partner Information**: You may complete this assignment individually or with exactly one partner. If you work with a partner, you must both be enrolled in the same lab section or you will both lose 10 points.

**Submission Instructions (working alone)**: Upload your solution, entitled **YourFirstName-YourLastName-Program2.py** to the BrightSpace **Program 2** Dropbox.

**Submission Instructions (working with one lab mate)**: Upload your solution, entitled **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program2.py** to the BrightSpace **Program 2** Dropbox. Note: If you work with a partner, only one person needs to submit a solution. If you both submit a solution, the submission that will be graded is the one from the partner whose last name comes alphabetically first.

**Deadline Reminder**: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes
- To solve this problem, you need to understand the following Python concepts: lists, functions, loops and if statements.

## Poker Hand Representation
A hand consists of five different cards drawn from a 52-card deck. Each card contains a rank (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 or 14) and a suit ("clubs", "diamonds", "hearts" or "spades"). For the ranks, an 11 represents a jack, a 12 represents a queen, a 13 represents a king and a 14 represents an ace.

## Poker Hand Evaluation - From Best to Worst
Note: Cards can appear in any order.

- **Royal Flush**: Contains a 10, jack, queen, king and ace, all of the same suit. For example: king clubs, jack clubs, ace clubs, 10 clubs, queen clubs.
- **Straight Flush**: Contains five consecutive cards that share the same suit. A straight flush does not contain an ace. For example: 3 clubs, 7 clubs, 6 clubs, 4 clubs, 5 clubs.
- **Four of a Kind**: Contains four cards that share the same rank. For example: 4 clubs, 10 diamonds, 4 hearts, 4 spades, 4 diamonds.
- **Full House**: Contains three cards that share the same rank and two cards that share a different rank. For example: jack hearts, king hearts, king clubs, jack clubs, jack diamonds.
- **Straight**: Contains five consecutive cards that do not all share the same suit. For example: 3 clubs, 7 diamonds, 6 hearts, 5 hearts, 4 clubs.
- **Three of a Kind**: Contains three cards that share the same rank and two cards that have unique ranks. For example: 6 clubs, 7 clubs, 8 clubs, 7 diamonds, 7 hearts.
- **Two Pair**: Contains two cards that share the same rank, two cards that share a different rank, and one card that has a unique rank. For example: six diamonds, six hearts, queen spades, ace clubs, queen diamonds.
- **Pair**: Contains two cards that share the same rank and three cards that have unique ranks. For example: king hearts, queen hearts, 9 diamonds, 9 hearts, ace spades.
- **Nothing**: All other hands of five cards. For example: 9 hearts, 6 diamonds, 3 diamonds, 10 spades, queen clubs.

## Assignment
Download [poker.py](../lessons/code/poker.py), make sure that you fully understand it, and then modify it so that it evaluates poker hands correctly. When it is run using the hands provided, it should produce [this output](../lessons/code/poker_output.txt).

The evaluate function is correct - do not modify it.

If it is helpful to do so, you are welcome to introduce other functions into your solution.

## Grading - 100 points
Note: Your program will be tested on a different set of poker hands than the ones that appear in the main() function of poker.py. Thus, it is important that you test your program on different inputs and identify the different types of poker hands in a general fashion.

10 points - Every **royal flush** is identified correctly. (All or nothing.)

5 points - Every **straight flush** is identified correctly. (All or nothing.)

10 points - Every **four of a kind** is identified correctly. (All or nothing.)

10 points - Every **full house** is identified correctly. (All or nothing.)

10 points - Every **straight** is identified correctly. (All or nothing.)

10 points - Every **three of a kind** is identified correctly. (All or nothing.)

10 points - Every **two pair** is identified correctly. (All or nothing.)

10 points - Every **pair** is identified correctly. (All or nothing.)

10 points - Every **nothing** is identified correctly. (All or nothing.)

15 points - The Python solution is properly commented, easy to understand, high quality and does not contain unnecessary code. (3 points for each type of improvement up to 15 points.)

## Test Data
```
def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")

    evaluate([[14, "spades"], [10, "spades"], [8, "spades"], [2, "hearts"], [5, "spades"]])     # nothing
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [5, "spades"]])      # 1 pair
    evaluate([[14, "spades"], [6, "spades"], [14, "clubs"], [6, "hearts"], [5, "spades"]])      # 2 pair
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [6, "clubs"]])       # 3 of a kind
    evaluate([[3, "spades"], [5, "spades"], [6, "spades"], [4, "hearts"], [2, "spades"]])       # straight
    evaluate([[4, "spades"], [6, "spades"], [4, "diamonds"], [6, "hearts"], [6, "clubs"]])      # full house
    evaluate([[14, "spades"], [6, "spades"], [6, "diamonds"], [6, "hearts"], [6, "clubs"]])     # 4 of a kind
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [9, "spades"], [10, "spades"]])   # straight flush
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [14, "spades"], [10, "spades"]])  # royal flush
```