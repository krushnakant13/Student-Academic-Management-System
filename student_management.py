import json
from pathlib import Path

DATA_FILE = Path("students.json")


def load_students():
    """Load student records from JSON. Return an empty list if no file exists."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read students.json. Starting with empty records.")
        return []


def save_students(students):
    """Save all student records to JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        print("Records saved successfully.")
    except OSError as error:
        print(f"Error while saving records: {error}")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Enter a value >= {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value <= {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Enter a value >= {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value <= {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def find_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def add_student(students):
    print("\n--- ADD STUDENT ---")
    roll_no = get_integer("Roll number: ", 1)

    if find_student(students, roll_no):
        print("A student with this roll number already exists.")
        return

    registration_no = get_non_empty("Registration number: ")
    name = get_non_empty("Name: ")
    department = get_non_empty("Department: ")
    dob = get_non_empty("Date of birth (DD-MM-YYYY): ")
    email = get_non_empty("Email: ")
    phone = get_non_empty("Phone: ")
    address = get_non_empty("Address: ")

    subject_count = get_integer("Number of subjects: ", 1, 10)
    subjects = []
    marks = []
    attendance = []

    for index in range(subject_count):
        print(f"\nSubject {index + 1}")
        subject = get_non_empty("Subject name: ")

        if subject.lower() in [item.lower() for item in subjects]:
            print("Duplicate subject name. Please enter it again.")
            subject = get_non_empty("Subject name: ")

        mark = get_float("Marks (0-100): ", 0, 100)
        attend = get_float("Attendance percentage (0-100): ", 0, 100)

        subjects.append(subject)
        marks.append(mark)
        attendance.append(attend)

    club_input = input("Clubs (comma-separated, leave blank if none): ").strip()
    clubs = set()
    if club_input:
        for club in club_input.split(","):
            club = club.strip()
            if club:
                clubs.add(club)

    # Tuple stores fixed identification information together.
    fixed_details = (registration_no, dob)

    student = {
        "roll_no": roll_no,
        "registration_no": fixed_details[0],
        "name": name,
        "department": department,
        "dob": dob,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "contact": {
            "email": email,
            "phone": phone,
            "address": address
        },
        "clubs": sorted(clubs)
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def display_student(student):
    average = calculate_average(student["marks"])
    grade = calculate_grade(average)

    print("\n" + "=" * 55)
    print(f"Roll Number       : {student['roll_no']}")
    fixed_details = (student["registration_no"], student["dob"])
    print(f"Registration No.  : {fixed_details[0]}")
    print(f"Name              : {student['name']}")
    print(f"Department        : {student['department']}")
    print(f"Date of Birth     : {student['dob']}")
    print(f"Email             : {student['contact']['email']}")
    print(f"Phone             : {student['contact']['phone']}")
    print(f"Address           : {student['contact']['address']}")
    print(f"Clubs             : {', '.join(student['clubs']) if student['clubs'] else 'None'}")

    print("\nAcademic Details")
    print("-" * 55)
    for subject, mark, attend in zip(
        student["subjects"], student["marks"], student["attendance"]
    ):
        print(f"{subject:<20} Marks: {mark:<6} Attendance: {attend}%")

    print("-" * 55)
    print(f"Average Marks     : {average:.2f}")
    print(f"Grade             : {grade}")
    print("=" * 55)


def search_student(students):
    print("\n--- SEARCH STUDENT ---")
    roll_no = get_integer("Enter roll number: ", 1)
    student = find_student(students, roll_no)

    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student(students):
    print("\n--- UPDATE STUDENT ---")
    roll_no = get_integer("Enter roll number: ", 1)
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    department = input(f"Department [{student['department']}]: ").strip()
    email = input(f"Email [{student['contact']['email']}]: ").strip()
    phone = input(f"Phone [{student['contact']['phone']}]: ").strip()
    address = input(f"Address [{student['contact']['address']}]: ").strip()

    if name:
        student["name"] = name
    if department:
        student["department"] = department
    if email:
        student["contact"]["email"] = email
    if phone:
        student["contact"]["phone"] = phone
    if address:
        student["contact"]["address"] = address

    save_students(students)
    print("Student record updated successfully.")


def delete_student(students):
    print("\n--- DELETE STUDENT ---")
    roll_no = get_integer("Enter roll number: ", 1)
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    display_student(student)
    confirm = input("Delete this record? (y/n): ").strip().lower()

    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def display_all(students):
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No student records available.")
        return

    for student in students:
        average = calculate_average(student["marks"])
        print(
            f"Roll: {student['roll_no']} | "
            f"Name: {student['name']} | "
            f"Department: {student['department']} | "
            f"Average: {average:.2f} | "
            f"Grade: {calculate_grade(average)}"
        )


def highest_scorer(students):
    print("\n--- HIGHEST SCORER ---")

    if not students:
        print("No student records available.")
        return

    top_student = max(
        students,
        key=lambda student: calculate_average(student["marks"])
    )
    display_student(top_student)


def students_by_department(students):
    print("\n--- STUDENTS BY DEPARTMENT ---")

    if not students:
        print("No student records available.")
        return

    departments = set(student["department"] for student in students)

    print("Available departments:")
    for department in sorted(departments):
        print(f"- {department}")

    department = get_non_empty("Enter department: ")

    matches = [
        student for student in students
        if student["department"].lower() == department.lower()
    ]

    if not matches:
        print("No students found in this department.")
        return

    for student in matches:
        print(f"{student['roll_no']} - {student['name']}")


def attendance_report(students):
    print("\n--- ATTENDANCE REPORT ---")

    if not students:
        print("No student records available.")
        return

    threshold = get_float("Enter attendance warning threshold: ", 0, 100)

    for student in students:
        average_attendance = (
            sum(student["attendance"]) / len(student["attendance"])
            if student["attendance"]
            else 0
        )

        status = "WARNING" if average_attendance < threshold else "OK"

        print(
            f"Roll: {student['roll_no']} | "
            f"Name: {student['name']} | "
            f"Average Attendance: {average_attendance:.2f}% | {status}"
        )


def department_statistics(students):
    print("\n--- DEPARTMENT STATISTICS ---")

    if not students:
        print("No student records available.")
        return

    departments = {}

    for student in students:
        department = student["department"]
        departments[department] = departments.get(department, 0) + 1

    print(f"Total Students: {len(students)}")
    print(f"Total Departments: {len(departments)}")

    for department, count in sorted(departments.items()):
        print(f"{department}: {count} student(s)")


def show_menu():
    print("\n" + "=" * 55)
    print("       STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Calculate Average / View Highest Scorer")
    print("7. List Students by Department")
    print("8. Attendance Report")
    print("9. Department Statistics")
    print("10. Save Records")
    print("11. Exit")
    print("=" * 55)


def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            display_all(students)
        elif choice == "6":
            highest_scorer(students)
        elif choice == "7":
            students_by_department(students)
        elif choice == "8":
            attendance_report(students)
        elif choice == "9":
            department_statistics(students)
        elif choice == "10":
            save_students(students)
        elif choice == "11":
            save_students(students)
            print("Thank you for using the Student Academic Management System.")
            break
        else:
            print("Invalid choice. Please select 1-11.")


if __name__ == "__main__":
    main()
