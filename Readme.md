# ICT111 LAB 2: Student Grading System

## Task 1: Plan the grading rules (IPO Plan)

Input:
* User menu choice (1-4).
* Student details: Student Number (string), Name (string), and Mark (numeric, 0-100).

Process
* Validate inputs to ensure they are not blank and marks are numeric/within range.
* Use `if/elif/else` structures to assign a grade (A, B, C, D, F) and decision (Excellent, Very good, Good, Pass, Fail) based on the mark.
* Store the combined data as a dictionary and append it to a main list.
* Iterate through the list of dictionaries to display records and calculate statistics (sum, average, max, min, passes, fails).

Output
* Confirmation messages upon successful data entry.
* A formatted list displaying all stored student records.
* A statistical summary report of the class performance.

Why use a list of dictionaries?
A dictionary allows us to group related attributes for a single entity using readable keys (e.g., `student['name']` and `student['mark']`). A list allows us to keep an ordered collection of these student dictionaries. Together, a list of dictionaries acts like a database table, making it very straightforward to iterate over all records using a `for` loop while easily accessing individual data points.

---

## Task 4: Verify the program with evidence


| T1| Add mark 79, then 80 | Grade assigned: B then A; decision: both pass. | Passed (B/Very good, A/Excellent). |
| T2| Add mark 49, then 50 | Grade assigned: F then D; fail then pass. | Passed (F/Fail, D/Pass). |
| T3| Enter -1, 101, or "abc" as mark | Reject input; ask again; program does not crash. | Passed (Handled via try-except/bounds checks). |
| T4| Display summary before adding students | Prevent division by zero; informative empty message. | Passed (Prints "Cannot generate summary..."). |
| T5| Choose an invalid menu option (e.g., 9) | Display warning; return to menu. | Passed (Displays "Warning: Invalid option"). |

*(Note for submission: Add screenshots of your terminal running these tests alongside this file.)*

---

## Task 5: Reflection

1. Why does the order of if/elif conditions matter at grade boundaries?
Conditions are evaluated from top to bottom. If we check `mark >= 50` before checking `mark >= 80`, a student with a score of 85 will trigger the first condition (`>= 50`) and incorrectly receive a 'D' instead of an 'A'. Properly ordered conditions ensure the logic catches the highest bracket first before falling through to the lower ones.

2. What error could arise when calculating the average of an empty list?
A `ZeroDivisionError` occurs. The mathematical formula for an average is the sum of items divided by the total number of items. If the list is empty, the length (the denominator) is 0, which causes the program to crash unless handled with a check (`if not students:`).

3. How would you adapt the program to handle two courses per student?
I would change the `mark`, `grade`, and `decision` dictionary keys to hold nested data structures. For example, instead of a single integer for `mark`, I would use a nested dictionary: `marks: {"Course1": 85, "Course2": 72}`. The logic for grading, displaying, and generating statistics would then require nested loops to process the data for each course individually.