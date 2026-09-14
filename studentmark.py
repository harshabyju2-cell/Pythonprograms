def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return sum(marks) / len(marks)
def find_highest(marks):
    return max(marks)
def find_lowest(marks):
    return min(marks)
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = assign_grade(average)
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    }
    students.append(student)
students_sorted = sorted(students, key=lambda x: x["total"], reverse=True)
print("\n--- Student Performance Analysis ---")
for s in students_sorted:
    print("\nName:", s["name"])
    print("Marks:", s["marks"])
    print("Total:", s["total"])
    print("Average:", round(s["average"], 2))
    print("Highest:", s["highest"])
    print("Lowest:", s["lowest"])
    print("Grade:", s["grade"])