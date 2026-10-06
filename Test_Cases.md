# Test Cases

| Test | Input/Action | Expected Result |
|---|---|---|
| 1 | Add valid student | Student is added |
| 2 | Add duplicate roll number | Duplicate warning is shown |
| 3 | Search existing roll number | Student profile is displayed |
| 4 | Search unknown roll number | Student not found |
| 5 | Enter empty required field | Program asks again |
| 6 | Enter marks above 100 | Program rejects input |
| 7 | Enter negative attendance | Program rejects input |
| 8 | Update existing student | Record is updated |
| 9 | Delete and confirm | Record is removed |
| 10 | Delete and cancel | Record remains |
| 11 | Display with no records | Empty-record message |
| 12 | Highest scorer | Student with highest average displayed |
| 13 | Department report | Matching students displayed |
| 14 | Attendance below threshold | WARNING displayed |
| 15 | Invalid menu option | Invalid-choice message |

## Boundary Testing

- Marks = 0
- Marks = 100
- Attendance = 0
- Attendance = 100
- One subject
- Ten subjects
- Empty student list
