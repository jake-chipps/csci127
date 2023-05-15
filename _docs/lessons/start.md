---
title: Getting Started
permalink: /docs/start/
---

## Create a Class Folder for Python
Create a folder entitled "CSCI 127" on your device. Make sure you can easily access the folder while the course is in session. We will store all of our Python files in this folder.

## Download and Install Python
We will initially be using **IDLE**, which is Python's Integrated Development and Learning Envrironment. 

You can download IDLE [here](https://www.python.org/downloads/).

After downloading, install the software. When you install IDLE, both the Python Shell as well as everything you need to run Python will be set up for you. 

## Write Your First Python Program
Open IDLE. 

### Shell Window
The first window that opens is called the **Shell Window**. The shell starts the Python interpreter so that we can tell Python to do things, and our computer will understand what we are saying. In the shell, we can run simple programs as well as write some very short code. 

<span class="task-header">Write a program in the shell</span>

<span class="task">Copy the following line of code in the shell and press enter.</span>

`print('hello world')`

<span class="think">What happened when you pressed enter?</span>

<span class="solution">The words "Hello World" appear below the line of code we wrote.</span>

### Editor Window
Now let's do the same thing but in the **Editor Window**. From the shell window, go to *File* and click *New File*. Copy and paste the same line of code: `print('Hello World')`. Try pressing enter. You will notice that you go to a new line. Due to the ability to easily write multiple lines of code, we will usually use the editor for longer programs. If you want to test something quickly, the shell works great.

<span class="task-header">Write a Multi-Line Program</span>

<span class="task">Add a second line of code after `print('hello world')` that prints out your name.</span>

To run the code, we first need to save the file. Go to *File* and *Save*, and save the file in your CSCI 127 folder. Call the file `hello_world`. After saving the file, you will notice that the editor window is now called **hello_world.py**. Files with the `.py` extention are Python files. The easiest way to run the code is to click the *Run* menu, and then *Run Module*. Go back to the shell window, and your code should have ran.

<span class="important">When writing programs, we will mostly be using the editor window. But the program will compile and run in the shell window. For this reason, you will want to have both windows open side by side.</span>