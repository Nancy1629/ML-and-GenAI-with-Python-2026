l = int(input("length:"))
b = int(input("breadth:"))

print(l * b)


p = int(input("priciple:"))
r = int(input("rate:"))
t = int(input("time:"))
print(p*r*t/100)

c = int(input("celsius:"))
print((c*9/5)+32)

a = int(input())
b = int(input())
c = int(input())
print((a+b+c)/3)

a = int(input("number:"))
print(a*a)
print(a*a*a)

a = int(input())
b = int(input())
a,b = b,a
print(a)
print(b)


#student report program 
name = input("Enter name:")
rollno = input("Enter roll no:")
m1 = int(input("enter marks 1:"))
m2 = int(input("enter marks 2:"))
m3 = int(input("enter marks 3:"))

#calculate total 
total = m1 + m2 + m3

#calculate percentage
percentage = (total/300)*100

#Display report
print("Name=" ,name)
print("Roll no=" ,rollno)
print("Total=" ,total)
print("Perentage=" ,percentage)