# phython-began
this is my first ever repo in accordance of skill development for further
i only use python language for my codes
Python Learning Journal
This repository contains my daily learning progress as I go through Python fundamentals and descriptive statistics — part of my M.Sc. job-ready skill-building plan.

✅ Day 1: Python Setup & Syntax
Practiced: print(), input(), type(), type conversions (int, float, complex, str)
Learned how to:
Use .split() with input()
Convert between data types
Use comments for documentation
✅ Day 2: Data Structures – Lists, Tuples, Sets, Dictionaries
Practiced:
List operations (append, pop, sort, slicing)
Tuple immutability
Set properties (no duplicates, basic set operations)
Dictionary creation, key-value pairs, get(), update(), keys(), values()
Learned differences between these structures and where to use them
✅ Day 3: Conditional Statements
Practiced:
if, elif, else statements
Nested conditions
Logical operators: and, or, not
Built small programs using conditional logic (e.g., grading system, eligibility check)
✅ Day 4: Loops – for and while
Practiced:
for loop with range()
Iterating over strings and lists
while loop with exit conditions
Control statements: break, continue, pass
Wrote mini-examples like printing patterns, list search, sum calculator
✅ Day 5: Functions
Practiced:

Creating and calling functions using def
Using parameters and return values
Wrote modular functions for repeated tasks

✅ Day 6: Random ,Math & Statistics Modules (Additional)
Practiced:
math module: sqrt, floor, ceil, pow, factorial, pi
statistics module: mean, median, mode, variance, stdev, pvariance, pstdev
Used both modules in practice scripts to perform calculations and summaries
✅ Day 7: Mini Project1 – Descriptive Statistics Tool
This project analyzes a list of numbers entered by the user and outputs key descriptive statistics using only built-in modules (statistics, math).

🧠 Features:
Count, Mean, Median, Mode(s)
Min, Max, Range
Population & Sample Variance and Standard Deviation
Quartiles (Q1, Q2, Q3), IQR
Outlier detection using 1.5×IQR rule
📦 Python Concepts Used:
input(), lists, loops, conditionals, and custom functions
Built-in modules: math, statistics
📂 File:
Week1_Python/mini_proj1.py ---- in python Week1_Python/mini_proj1.ipynb ---- in jupyter notebook

SAMPLE OUTPUT
Enter your data with space between each data points= 2 4 2 79 173 182 2 3 4 44 5 3 22 Entered data is= [2.0, 4.0, 2.0, 79.0, 173.0, 182.0, 2.0, 3.0, 4.0, 44.0, 5.0, 3.0, 22.0] -----For The Given Data The Following Statistics Are Calculated And Are Listed Below----

ABOUT THE DATA , [2.0, 4.0, 2.0, 79.0, 173.0, 182.0, 2.0, 3.0, 4.0, 44.0, 5.0, 3.0, 22.0] NO OF ELEMENTS IN DATA SET IS : 13 DATA HAS ODD NO OF ELEMENTS

SECTION-1 "MEASURE OF CENTRAL TENDANCIES"

MEAN: 40.38461538461539 MEDIAN: 4.0 UNIQUE MODE: [2.0]

SECTION-2 "MEASURE OF DISPERSION"

POPULATION VARIANCE: 3892.24 SAMPLE VARIANCE: 4216.59 POPULATION STANDARD DEVIATION: 62.39 SAMPLE STANDARD DEVIATION: 64.94

SECTION-3 "__MEASURE OF RANGE __"

MAXIMUM VALUE OF THE DATA SET: 182.0 MINIMUM VALUE OF THE DATA SET: 2.0 RANGE OF THE DATA SET: 180.0

SECTION-4 "MEASURE OF POSITION"

QUARTILE 1: 2.5 QUARTILE 2: 4.0 QUARTILE 3: 61.5 INTER QUARTILE RANGE: 59.0 OUTLIARS: [173.0, 182.0]

Do you want to do it for another data set ?(y/n)

✅ Week 1 Mini Project 2: Height Analysis Tool
This project collects heights (in cm) of multiple individuals and returns a detailed statistical summary. It also converts each height into meters and inches, and classifies the person as Short, Average, or Tall.

🧠 Features:
Count, Mean, Median, Mode
Standard Deviation, Min, Max
Unit conversion (cm → m and inches)
Height classification:
< 150 cm → Short
150–170 cm → Average
> 170 cm → Tall
📦 Python Concepts Used:
input(), lists, loops, conditionals, custom functions
Built-in modules: math, statistics
📂 File:
Week1_Python/mini_proj2.ipynb

🧪 Sample Output:
WELCOME TO THE HEIGHT ANALYSIS TOOL The Entered Dataset Is : [123.98, 145.78, 144.89, 164.89, 175.8, 179.0] ---------HEIGHTS ANALYSIS---------
Numbers Of Individuals: 6 Mean: 155.72 Median: 155.33 Mode: No Mode Standard Deviation: 21.23 Minimum Height: 123.98 Maximum Height: 179.0 Short: 3 Average: 1 Tall: 2

NOTE---'SHORT' is defined as set of individuals with height less than 150 c.m. 'AVERAGE' os defined as the set of individuals with height between 150 annd 170 c.m. 'TALL' is defined as the set of individuals with height greater than 170 c.m.

--------CONVERSION OF HEIGHTS IN METERS AND INCHES-------- ht. in c.m. | ht. in meters | ht. in inches 123.98 | 1.24 | 48.72 145.78 | 1.46 | 57.29 144.89 | 1.45 | 56.94 164.89 | 1.65 | 64.80 175.80 | 1.76 | 69.09 ... With Median Height 155.33 C.M. The Standard Deviation Of Heights From The Mean Is 21.23 C.M. . From This Data It Has Bbeen Also Found That The Tallest Individual From This Data Has Height 179.0 C.M. And The Shortest Individual Has Height 123.98 C.M. Output is truncated. View as a scrollable element or open in a text editor
📌 Built using only Week 1 concepts + math and statistics modules. ✅ What to Do Now: Paste this block below your Day 7 project section in README.md

Create the Python file (if not done already): Week1_Python/height_analysis_tool.py

Push it to GitHub

Let me know if you want me to generate this entire README.md in PDF or Markdown file format for download.



