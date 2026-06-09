def get_mark(subject):
    while True:
        try:
            value = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= value <= 100:
                return value
            print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def main():
    print("=== Marksheet Generator ===")
    student_name = input("Student name: ").strip()
    roll_number = input("Roll number: ").strip()

    subjects = ["Math", "Science", "English", "History", "Computer"]
    marks = {subject: get_mark(subject) for subject in subjects}

    total_marks = sum(marks.values())
    maximum_total = len(subjects) * 100
    percentage = (total_marks / maximum_total) * 100
    grade = calculate_grade(percentage)

    print("\n=== Marksheet ===")
    print(f"Name      : {student_name}")
    print(f"Roll No.  : {roll_number}")
    print("------------------------------")
    for subject, mark in marks.items():
        print(f"{subject:<10}: {mark:.2f}")
    print("------------------------------")
    print(f"Total     : {total_marks:.2f} / {maximum_total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade     : {grade}")


if __name__ == "__main__":
    main()
