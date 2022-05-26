# Simple Calculator Program
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

def addition(a, b):
   return a + b
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

def substract(a, b):
   return a - b
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

def multiply(a, b):
   return a * b
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

def division(a, b):
   return a / b
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

print("!! Welcome to CALCULATOR !!")
print("===========================")
print("1. Addition (+)")
print("2. Substract (-)")
print("3. Multiply (*)")
print("4. Division (/)")
print("---------------------------")
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

menu = input("Enter Menu (1/2/3/4): \n")
# Mario Caesar
# linktr.ee/caesarmario_
# 2019

if menu == '1':
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1,"+",num2,"=", addition(num1,num2))
    # Mario Caesar
    # linktr.ee/caesarmario_
    # 2019
elif menu == '2':
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1,"-",num2,"=", substract(num1,num2))
    # Mario Caesar
    # linktr.ee/caesarmario_
    # 2019
elif menu == '3':
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1,"*",num2,"=", multiply(num1,num2))
    # Mario Caesar
    # linktr.ee/caesarmario_
    # 2019
elif menu == '4':
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1,"/",num2,"=", division(num1,num2))
    # Mario Caesar
    # linktr.ee/caesarmario_
    # 2019
else:
   print("WRONG INPUT MENU!")
# Mario Caesar
# linktr.ee/caesarmario_
# 2019