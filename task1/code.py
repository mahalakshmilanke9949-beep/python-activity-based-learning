# University Scholarship Allocation System

# Scholarship Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

eligible_students = []
not_eligible_students = []

# Input number of students
n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate marks (%): "))

    # Subject-wise marks
    subjects = []
    num_subjects = int(input("Enter number of subjects: "))

    for j in range(num_subjects):
        marks = float(input(
            f"Enter marks for subject {j + 1}: "
        ))
        subjects.append(marks)

    attendance = float(
        input("Enter attendance percentage: ")
    )

    income = float(
        input("Enter annual family income: ")
    )

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(m >= MIN_SUBJECT for m in subjects) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        not_eligible_students.append(name)


# Sort eligible students
# Priority:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income

eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"].lower()
    )
)


# Display eligible students
print("\n========== SCHOLARSHIP RANK LIST ==========")

if eligible_students:

    for rank, student in enumerate(
        eligible_students, start=1
    ):

        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate Marks:", student["aggregate"])
        print("Attendance:", student["attendance"])
        print("Annual Income: Rs.", student["income"])
        print("Status: ELIGIBLE")

else:
    print("No students are eligible for scholarship.")


# Display not eligible students
print("\n========== NOT ELIGIBLE STUDENTS ==========")

if not_eligible_students:

    for name in not_eligible_students:
        print(name, "- NOT ELIGIBLE")

else:
    print("All students are eligible.")


print("\nScholarship Allocation Process Completed.")
Here you to write the code
