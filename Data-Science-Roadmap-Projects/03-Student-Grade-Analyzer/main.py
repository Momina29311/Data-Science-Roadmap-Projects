print("========== Student Grade Analyzer ==========")

name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

subjects = ["English", "Math", "Physics", "Chemistry", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    if mark < 0 or mark > 100:
        print("Invalid marks! Please enter values between 0 and 100.")
        exit()
    marks.append(mark)

print("\n--------------------------------------------\n")

total = sum(marks)
percentage = (total / 500) * 100

if any(mark < 40 for mark in marks):
    grade = "F"
    status = "FAIL"
elif percentage >= 90:
    grade = "A+"
    status = "PASS"
elif percentage >= 80:
    grade = "A"
    status = "PASS"
elif percentage >= 70:
    grade = "B"
    status = "PASS"
elif percentage >= 60:
    grade = "C"
    status = "PASS"
elif percentage >= 50:
    grade = "D"
    status = "PASS"
else:
    grade = "F"
    status = "FAIL"

if percentage >= 90:
    remark = "Outstanding 🌟"
elif percentage >= 80:
    remark = "Excellent 🎉"
elif percentage >= 70:
    remark = "Good 👍"
elif percentage >= 50:
    remark = "Average 🙂"
else:
    remark = "Needs Improvement 📚"

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_number}")
print()
print(f"Total Marks  : {total:.0f} / 500")
print(f"Percentage   : {percentage:.1f}%")
print()
print(f"Grade         : {grade}")
print(f"Status        : {status}")
print(f"Remarks       : {remark}")

if status == "PASS":
    print("\nCongratulations! 🎉")