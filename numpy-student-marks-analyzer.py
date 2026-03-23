import numpy as np

'''Project 1 — Student Marks Analyzer
Goal: Practice arrays, filtering, and statistics.'''

marks = np.array([78, 45, 89, 92, 55, 61, 73, 84, 33, 67])

print(f"Mean: {np.mean(marks)}")    #mean
print(f"Highest Mark: {np.max(marks)}") #highest mark
print(f"Lowest Mark: {np.min(marks)}")    #lowest mark
marks[marks < 50] = 0
print(f"Mark below 50 replaced: {marks}")   #Replace marks below 50 with 0
print(f"Passed Students: {len(marks[marks > 50])}") #Count how many students passed (>50)
print(f"New Bonus Marks: {marks * 1.1}")    #Create a new array with marks * 1.1 (bonus marks)
























'''
Here’s a clean GitHub description and a README you can use for your first project using NumPy.

GitHub Repository Description

Student Marks Analyzer built with Python and NumPy. The project performs statistical analysis on student marks including averages, pass counts, and bonus mark calculations.

README.md
# Student Marks Analyzer

## Overview
This project analyzes a dataset of student marks using Python and NumPy.  
It demonstrates basic data analysis operations such as calculating averages, identifying highest and lowest marks, filtering data, and applying bonus marks.

The goal of the project is to practice working with arrays, filtering conditions, and aggregate functions.

---

## Technologies Used
- Python
- NumPy

---

## Dataset
The dataset is a simple NumPy array representing marks obtained by students.

Example dataset:

[78, 45, 89, 92, 55, 61, 73, 84, 33, 67]

---

## Features
The program performs the following analysis:

- Calculates the **average mark**
- Finds the **highest mark**
- Finds the **lowest mark**
- Replaces marks **below 50 with 0**
- Counts the number of **students who passed**
- Generates **bonus marks by increasing marks by 10%**

---

## Example Output

Mean: 67.7
Highest Mark: 92
Lowest Mark: 33
Marks below 50 replaced: [78 0 89 92 55 61 73 84 0 67]
Passed Students: 8
New Bonus Marks: [85.8 0. 97.9 101.2 60.5 67.1 80.3 92.4 0. 73.7]


---

## How to Run the Project

1. Install NumPy


pip install numpy


2. Run the Python script


python student_marks_analyzer.py


---

## Learning Objectives
This project demonstrates how to:

- Create and manipulate arrays using NumPy
- Apply filtering conditions
- Use aggregate functions like mean, min, and max
- Perform vectorized mathematical operations

---

## Author
Judge Tshwarelo

💡 Small GitHub tip:
Name the repository something clear like:

numpy-student-marks-analyzer

If you want, I can also show you how to make your GitHub README look much more professional with badges, images, and formatting (most beginners don't know this trick).
'''