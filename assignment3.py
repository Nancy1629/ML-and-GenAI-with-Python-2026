def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()


def sum_n_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    print("Sum =", total)

n = int(input("Enter N: "))
sum_n_numbers(n)


def reverse_number():
    num = input("Enter a number: ")
    print("Reversed number =", num[::-1])

reverse_number()


def count_digits():
    num = input("Enter a number: ")
    print("Number of digits =", len(num))

count_digits()


def palindrome():
    num = input("Enter a number: ")

    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()


def fibonacci():
    a = 0
    b = 1

    for i in range(10):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci()


def add(a, b):
    print("Addition =", a + b)

def subtract(a, b):
    print("Subtraction =", a - b)

def multiply(a, b):
    print("Multiplication =", a * b)

def divide(a, b):
    print("Division =", a / b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add(num1, num2)
subtract(num1, num2)
multiply(num1, num2)
divide(num1, num2)


file = open("student.txt", "w")

file.write("Name: Nancy\n")
file.write("Marks: 90")

file.close()

print("Data Saved")


file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Answer =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Nancy", 90)

print("Name =", s1.name)
print("Marks =", s1.marks)