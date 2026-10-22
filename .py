name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0

for i in range(1, n + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = total / n

if percentage >= 90:
  grade = "A+"
  performance = "Distinction"
elif percentage >= 80:
  grade = "A"
  performance = "First Class"
elif percentage >= 75:
  grade = "B+"
  performance = "Second Class"
elif percentage >= 60:
  grade = "B"
  performance = "Third Class"
elif percentage >= 50:
  grade = "C"
  performance = "Needs Improvement"
else:
  grade = "F"
  performance = "Fail"

print("\n--- Academic Report ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Performance:", performance)
