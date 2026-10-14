
import numpy as np

# 1. Create marks of 10 students across 5 subjects
marks = np.array([
    [85, 90, 78, 88, 92],
    [65, 70, 60, 75, 68],
    [45, 50, 55, 40, 48],
    [90, 95, 92, 88, 96],
    [30, 42, 35, 28, 40],
    [75, 80, 85, 70, 78],
    [55, 60, 58, 62, 65],
    [95, 98, 94, 96, 99],
    [40, 35, 45, 50, 38],
    [70, 75, 72, 68, 80]
])

students = np.arange(1, 11)

print("Student Marks:\n", marks)

# 2. Student-wise average
student_avg = np.mean(marks, axis=1)
print("\nStudent Averages:", student_avg)

# 3. Subject-wise average
subject_avg = np.mean(marks, axis=0)
print("\nSubject Averages:", subject_avg)

# 4. Highest and lowest marks
print("\nHighest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))

# 5. Total marks of each student
total_marks = np.sum(marks, axis=1)
print("\nTotal Marks:", total_marks)

# 6. Find student with highest total
top_student = np.argmax(total_marks)
print("\nTop Student:", students[top_student])

# 7. Pass/Fail status
# Minimum 40 marks required in every subject
passed = np.all(marks >= 40, axis=1)

status = np.where(passed, "Pass", "Fail")
print("\nStudent Status:", status)

# 8. Rank students by total marks
ranking = np.argsort(total_marks)[::-1]

print("\nStudent Rankings:")
for rank, index in enumerate(ranking, start=1):
    print("Rank:", rank, "Student:", students[index], "Total:", total_marks[index])

# 9. Students needing academic improvement
# Students with average below 50
needs_improvement = student_avg < 50

weak_students = students[needs_improvement]
print("\nStudents Needing Improvement:", weak_students)

# 10. Display final report
print("\n----- FINAL STUDENT REPORT -----")

for i in range(len(students)):
    print(
        "Student:", students[i],
        "| Total:", total_marks[i],
        "| Average:", round(student_avg[i], 2),
        "| Status:", status[i]
    )
