# STUDENTS MARKS & GRADE MANAGEMENT
Design a student academic management system to record marks,compute grades,generate report cards, and manage pass/fail results.

#### Actors: Teacher, Student, Admin
#### Classes: Student, Teacher, Mark, Grade
pre-conditions:
    -Students are enrolled insubjects.Grading policy configured
Trigger:
    -Teacher enters marks for students after an examination
Main flow:
    1. Teacher selects class and subject
    2. Teacher enter marks for each student
    3. System validates marks
    4. calculates grades and grade points to determine pass or fail
    5.generate report and made available to students

Exceptions:
    -E1:Invalid marks error
    -E2:Record Already exist error
    -E3:Student ID not found error

Grading table:
    (90-100) O  - Outstanding  - 10
    (80-89)  A+ -Excellent     - 9
    (70-79)  A  -Very Good     - 8
    (60-69)  B+ -Good          - 7
    (50-59)  B  -Above Average -6 
    (40-49)  C  -Average       - 5
    (0-39)   F  -Fail          - 0

