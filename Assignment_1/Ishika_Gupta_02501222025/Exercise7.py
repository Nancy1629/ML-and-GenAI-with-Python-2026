# Aim-Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
#Student details
print("Enter Student Details ")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks of Student
print("Enter marks (out of 100) ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Calculating total and percentage
TotalMarks = m1 + m2 + m3
MaxMarks=300
percentage = (TotalMarks / MaxMarks) * 100

# Displaying report
print("\n----- Student Report -----")
print("Name:", name)
print("\nSubject Scores")
print("Subject 1: ",m1)
print("Subject 2: ",m2)
print("Subject 3: ",m3)
print("Roll No:", roll_no)
print("Total Marks:",TotalMarks ,"/",MaxMarks)
print("Percentage:", percentage, "%")