# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Function
no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))

add = no1+no2
print("Addition is: ",add)

def addition(): #function definition
    add = no1+no2
    print("Addition is: ",add)
    
no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))
addition() #function calling
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to display output for all arithmetic operation by 4 different function (+,-,*,/).
def addition(): #function without parameter
    add = no1+no2
    print("Addition is: ",add)

def substraction(no1,no2): #function with parameter
    sub = no1-no2
    print("Substraction is: ",sub)

def multiple(a,b):
    mul = a*b
    print("Multiplication is: ",mul)

def division(x,y): #value return function
    div = x/y
    return div
    
no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))
addition(no1,no2)
substraction(no1,no2)
multiple(no1,no2)
result = divison(no1,no2)
print("Division is: ",result)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

def addition():
    add = no1+no2
    print("Addition is: ",add)

def substraction(no1,no2):
    sub = no1-no2
    print("Substraction is: ",sub)

def multiplication(a,b):
    mul = a*b
    print("Multiplication is: ",mul)

def division(p,q):
    div = p/q
    return div

choice = str(input("Enter any key to continue and '1' to terminate: "))
while(choice !='1'):
    no1=int(input("Enter 1st value: "))
    no2=int(input("Enter 2nd value: "))

    print("Arithmetical operations are:\n1. Add\n2. Sub\n3. Mult\n4. Div")
    opt=int(input("Select your choice: "))
    if(opt==1):
        addition()
    elif(opt==2):
        substraction(no1,no2)
    elif(opt==3):
        multiplication(no1,no2)
    elif(opt==4):
        result=division(no1,no2)
        print("Division is: ",result)
    else:
        print("Wrong option. Good Bye.")
    choice = str(input("Enter any key to continue and '1' to terminate: "))
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021