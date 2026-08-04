# Project 03 — Student Grade Analyzer

A beginner-friendly Python project that calculates a student's total marks, percentage, grade, and pass/fail status using conditional logic.

## Project Objective
Build a program that accepts a student's name, roll number, and marks for 5 subjects, then evaluates performance using grades and pass/fail rules.

## Concepts Covered
- `if`, `elif`, `else`
- Comparison operators
- Logical operators
- Variables
- User input
- Arithmetic calculations
- Output formatting

## Features
- Takes student name and roll number.
- Accepts marks for 5 subjects.
- Validates that marks are between 0 and 100.
- Calculates total marks and percentage.
- Assigns a grade based on percentage.
- Displays pass/fail status.
- Shows remarks based on performance.
- Fails the student if any subject is below 40.

## Grade Criteria
- 90–100: A+
- 80–89: A
- 70–79: B
- 60–69: C
- 50–59: D
- Below 50: F

## How to Run
1. Make sure Python is installed.
2. Run the program:

```bash
python main.py
```

3. Enter the student details and marks when prompted.

## Sample Output
```txt
========== Student Grade Analyzer ==========

Enter Student Name: Momina
Enter Roll Number: 41

Enter marks for English: 88
Enter marks for Math: 91
Enter marks for Physics: 85
Enter marks for Chemistry: 79
Enter marks for Computer: 95

--------------------------------------------

Student Name : Momina
Roll Number  : 41

Total Marks  : 438 / 500
Percentage   : 87.6%

Grade         : A
Status        : PASS
Remarks       : Excellent 🎉

Congratulations! 🎉
```

## Future Improvements
- Add input validation for non-numeric values.
- Store student results in a file.
- Support multiple students.
- Generate a marksheet automatically.
- Add a simple GUI.

## Learning Outcome
By completing this project, you will understand:
- How to use conditional logic in Python.
- How to compare values and make decisions.
- How to combine arithmetic and logic in one program.
- How grading systems can relate to real-world classification tasks.