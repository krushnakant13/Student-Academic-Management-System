# Pseudocode

## Main Program

START
    LOAD student records
    REPEAT
        DISPLAY menu
        INPUT choice

        IF choice = 1
            Add Student
        ELSE IF choice = 2
            Search Student
        ELSE IF choice = 3
            Update Student
        ELSE IF choice = 4
            Delete Student
        ELSE IF choice = 5
            Display All Students
        ELSE IF choice = 6
            Find Highest Scorer
        ELSE IF choice = 7
            List Students by Department
        ELSE IF choice = 8
            Generate Attendance Report
        ELSE IF choice = 9
            Generate Department Statistics
        ELSE IF choice = 10
            Save Records
        ELSE IF choice = 11
            SAVE records
            EXIT
        ELSE
            DISPLAY invalid choice
        END IF
    UNTIL choice = 11
STOP

## Average Marks

START
    SET total = 0
    FOR each mark in marks
        total = total + mark
    END FOR
    average = total / number of marks
    RETURN average
STOP
