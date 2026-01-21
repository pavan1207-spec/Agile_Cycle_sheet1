def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0–100): "))

    grade = calculate_grade(marks)
    students.append((name, marks, grade))


print("\n--- Student Marks & Grades ---")


print(f"{'Name':<20}{'Marks':<10}{'Grade':<10}")
print("-" * 45)


for name, marks, grade in students:
    print(f"{name:<20}{marks:<10}{grade:<10}")
