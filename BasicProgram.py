# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

# Write a program to print 'Hello' to user
print("Hello")
print("Welcome to OPU.")
print("This is Python session.")
print("Hello\nWelcome to OPU.\n\tThis is Python session.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

# Write a program to accept value in program and display it.
no1 = 100
print(no1)
print("Your value of no1 is: ",no1)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to accept value from user and display it.
no1 = int(input("Enter your value here: "))
print("Your value is: ",no1)

no2 = float(input("Enter decimal value here: "))
print("Your decimal value is: ",no2)

name = str(input("Enter your name here: "))
print("Your name is: ",name)

last = input("Enter your last name: ")
print("Your last name is: ",last)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to accept 2 numbers from user and display addition of those numbers.
no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))

add = no1 + no2

print("Addition is: ",add)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to accept 2 numbers from user and do all arithmetical operations.
#Display its output. (+,-,*,/,%,//,**)

no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))

add = no1 + no2
sub = no1 - no2
mult = no1 * no2
div = no1 / no2
mod = no1 % no2
divint = no1 // no2
power = no1 ** no2

print("\nAll arithmetic outputs are\nAddition is\t\t: ",add,
      "\nSubtraction is\t\t: ",sub,"\nMultiplication is\t: ",mult,
      "\nDivision is\t\t: ",round(div,2),"\nModulus is\t\t: ",mod,
      "\nDivision with Integer is: ",divint,"\nPower is\t\t: ",power)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program Accept 2 numbers from user and print swapping of those number.
print("Q.6. Swapping")
no1 = int(input("Enter first value:"))
no2 = int(input("Enter second value:"))
print("\nBefore swapping values are:\tno1 is: ",no1,"\tno2 is: ",no2)
temp = no1
no1 = no2
no2 = temp
print("After swapping values are:\tno1 is: ",no1,"\tno2 is: ",no2)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#7.Write a program to Calculate the Area and the circumference for a circle.
#(Area of circle = π r2 circumference of circle = 2 π r)
print("\nQ.7 Area and Circumference")
r = float(input("Enter radius for a circle: "))
pi = 3.14
area = pi * r * r
cir = 2 * pi * r
print("Area of a circle is: ",area,"\nCircumference of a circle is: ",cir)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to Accept 5 subject marks from student and calculate the total and
#percentage(average) of a student for a semester and display it.
print("\nQ.8 Student Marks")
s1 = int(input("Enter 1st subject mark: "))
s2 = int(input("Enter 2nd subject mark: "))
s3 = int(input("Enter 3rd subject mark: "))
s4 = int(input("Enter 4th subject mark: "))
s5 = int(input("Enter 5th subject mark: "))

total = s1 + s2 + s3 + s4 + s5
avg = total/5

print("Total is: ",total,"\nAverage is: ",avg)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

'''
Write a program to Accept Basic from an employee and calculate salary of an employee
by considering following things.
(Grade_pay is double of Basic. DA is 70% of Basic. TA is RM 200.
HRA is 20% of Basic.)(Formula for salary = Grade_pay + DA + TA + HRA).
'''
print("\nQ.9 Salary of an Employee")
basic = float(input("Enter your basic: "))
TA = 200
GP = basic * 2
DA = basic * 0.7
HRA = basic * 0.2
salary = GP + DA + TA + HRA
print("Salary of an employee is: :",salary)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021
