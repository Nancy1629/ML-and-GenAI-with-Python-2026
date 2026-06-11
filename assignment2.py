total = 0
for i in range(1,11):
    total = total + i
    print(total)


num = int(input("enter a number:"))
fact = 1
for i in range(1 , num+1):
    fact = fact*i
    print("factorial of " , num, "is")
    print(fact)


n = int(input("enter number of terms:"))
a = 0
b = 1
for i in range(n):
    print(a)

    c = a+b
    a = b 
    b = c


a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a > b and a > c:
    print("largest number is:" , a)
elif b > a and b > c:
    print("largest number is:" , b)
else:
    print("largest number is" , c)


name = input("enter student name:")
roll_no = input("enter roll number:")

#Marks input
m1 = int(input("enter makrs of sunject 1:"))
m2 = int(input("enter makrs of sunject 2:"))
m3 = int(input("enter makrs of sunject 3:"))
m4 = int(input("enter makrs of sunject 4:"))
m5 = int(input("enter makrs of sunject 5:"))

#Total marks
total = m1 + m2 + m3 + m4 + m5

#Percentage
percentage = (total/500)*100

#Grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

#Display result
print("Student result")
print("Name = ", name)
print("Roll number = ", roll_no)
print("Total marks =", total)
print("Percentage = ", percentage)
print("Grade =", grade)