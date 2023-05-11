---
title: Lab 7 Dictionaries
permalink: /docs/lab7/
---

## Logistics
**Due**: Tuesday, June 6th no later than 11:58 p.m..

**Partner Information**: Complete this assignment individually or with your Program 3 partner.

**Submission Instructions (Working Alone)**: Upload your solution, renamed to **YourFirstName-YourLastName-Lab7.py** to the BrightSpace **Lab 7** Dropbox.

**Submission Instructions (Working With Your Program 3 Partner)**: Upload your solution, renamed to **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Lab7.py** to the BrightSpace **Lab 7** Dropbox.

**Deadline Reminder**: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcome
- Gain experience with dictionaries.

## Preliminaries
ASCII (American Standard Code for Information Interchange) is an older code used by computers to represent characters (such as the character "X") with 8 binary digits (or bits). Here is an [ASCII table](https://www.sciencebuddies.org/science-fair-projects/references/ascii-table). Today, Unicode UTF-16, a 16 bit code is more commonly used.

Download [lab7.py](../lessons/code/lab7.py), rename it according to the instructions above, and make sure you understand it.

Download input file [ascii-codes.csv](../lessons/code/ascii-codes.csv) to the same directory where you downloaded lab7.py. Each line in ascii-codes.csv contains 8 bits (0s and 1s), followed by a comma, followed by the character that the 8 bits represents. In general, the character will be of length 1 such as the character X. However, there are two exceptions: `" "` is represented by space and `","` is represented by comma.

## Assignment
Take the program above and modify it by adding the `create_dictionary` function. The parameter `file_name` is the name of a csv file that contains an unknown number of lines that reflect ASCII encodings. The format of this file is described in the bullet above. The function should return a dictionary where the keys are characters and the values are the 8 bit representations. Note: use `" "` and `","` as keys instead of space and comma.

Take the program above and modify it by adding the `translate` function. The parameter sentence consists of an unknown number of characters. The parameter dictionary is the dictionary that was created by the `create_dictionary` function. The parameter `file_name` is the name of the output file where all output should be sent. In the output file, each character in sentence should appear on its own line, followed by a space, followed by its 8 bit representation. If a character does not appear in the dictionary, the word UNKNOWN should appear instead of an 8 bit representation.

When the program is run, it should produce the following three output files: [output-1.txt](../lessons/code/lab7_output-1.txt), [output-2.txt](../lessons/code/lab7_output-2.txt) and [output-3.txt](../lessons/code/lab7_output-3.txt).

## Grading - 10 points
2 points - The `create_dictionary` function returns a dictionary that contains the correct binary code for each character of length one.

1 point - The `create_dictionary` function returns a dictionary that contains the correct binary code for `" "` and `","`.

4 points - When your program is tested with different values for the variable sentence, characters that exist in the dictionary are translated correctly. For each different character that is translated incorrectly, one point will be deducted.

1 point - When your program is tested with different values for the variable sentence, characters that do NOT exist in the dictionary are translated correctly to UNKNOWN.

1 point - The format of any output files created match the format of the sample output files exactly.

1 point - In a comment at the top of the python file that you submit, explain why the comma character and the space character are treated differently in ascii-codes.csv.

## If Time Remains
Work on Program 3, seeking feedback as necessary.