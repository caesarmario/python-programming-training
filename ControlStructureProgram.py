# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to check given number is positive.
no = int(input("Enter your value: "))
if(no > 0):
    print("no is Positive.")
print("Done")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to check given number is positive or negative.
no = int(input("Enter value here: "))
if(no > 0):
    print("no is positive.")
else:
    print("no is negative.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to check given number is zero, positive or negative.
no = int(input("Enter value here: "))
if(no == 0):
    print("no is zero")
elif(no > 0):
    print("no is positive.")
else:
    print("no is negative")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Q.1. Write a program to check given number is EVEN or ODD.
print("Even odd example: ")
no = int(input("Enter your value here:"))
if(no%2==0):
    print("no is EVEN.")
else:
    print("no is ODD.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Q.2. Write a program to find the largest number between 2 numbers.
print("\nlargest between 2 numbers: ")
no1 = int(input("Enter 1st value: "))
no2 = int(input("Enter 2nd value: "))
if(no1 == 0 and no2 == 0):
    print("All Zero.")
elif(no1 == no2):
    print("All Equal.")
elif(no1 > no2):
    print("no1 is largest.")
else:
    print("no2 is largest.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021
  
#Q.3. Write a program to find largest number between 3 numbers.
print("\nlargest between 3 numbers: ")
no1 = int (input("Enter your 1st value : "))
no2 = int (input("Enter your 2nd value : "))
no3 = int (input("Enter your 3rd value : "))
if (no1 == 0 and no2 == 0 and no3 == 0):
    print("No comparison all 0.")
elif (no1 == no2 and no2 == no3):
    print("The numbers are all equal")
elif (no1 == no2 and no1 > no3):
    print("no1 & no2 are larger than n03.")
elif (no1 == no3 and no1 > no2):
    print("no1 & no3 are larger than no2.")
elif (no2 == no3 and no2 > no1):
    print("no2 & no3 are larger than no1.")
elif (no1 > no2 and no1 > no3):
    print ("no1 is the largest.")
elif (no2 > no3):
    print ("no2 is the largest.")
else:
    print ("no3 is the largest.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

'''Q.4. Write a program to read customer’s name, purchase amount and tax code. The tax code has
been validated and will be one of the following:
0 	tax exempt (0%)
1 	state sales tax only (3%)
2 	federal and state sales tax (5%)
3 	special sales tax (7%)
The program must then compute the sales tax and the total amount due, and
print the customer’s name, purchase amount, sales tax and total amount due.
'''
print("\nQ.4. Tax Code Question") 
name = input("Enter customer name: ")
PA = float(input("Enter purchase amount: "))
tax_code = int(input("Enter tax code from 0/1/2/3: "))

if(tax_code == 0):
    ST = 0
    FB = PA + ST
    print("\n\t*****Welcome to STAR MALL*****\n\tYou Final Bill is Here\n\nCustomer Name\t: ",name,
          "\nPurchase Amount\t: ",PA,"\nSales Tax\t: ",ST,"\nFinal Bill\t: ",FB)
elif(tax_code == 1):
    ST = PA * 0.03
    FB = PA + ST
    print("\n\t*****Welcome to STAR MALL*****\n\tYou Final Bill is Here\n\nCustomer Name\t: ",name,
          "\nPurchase Amount\t: ",PA,"\nSales Tax\t: ",ST,"\nFinal Bill\t: ",FB)
elif(tax_code == 2):
    ST = PA * 0.05
    FB = PA + ST
    print("\n\t*****Welcome to STAR MALL*****\n\tYou Final Bill is Here\n\nCustomer Name\t: ",name,
          "\nPurchase Amount\t: ",PA,"\nSales Tax\t: ",ST,"\nFinal Bill\t: ",FB)
elif(tax_code == 3):
    ST = PA * 0.07
    FB = PA + ST
    print("\n\t*****Welcome to STAR MALL*****\n\tYou Final Bill is Here\n\nCustomer Name\t: ",name,
          "\nPurchase Amount\t: ",PA,"\nSales Tax\t: ",ST,"\nFinal Bill\t: ",FB)
else:
    print("Wrong Tax code.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Q.5. Design an algorithm using pseudo code or flowchart to identify a person is healthy
#or sick based on his / her body temperature.
#Print appropriate message to indicate the health status. 
#(Note: The normal human body temperature range is typically stated as 36.5–37.5 °C.)

print("\nQ.5. Body Temperature Question") 
temp = float(input("Kindly enter your body temperature: "))
if(temp <= 37.5 and temp >= 36.5):
    print("\n\tVERY VERY GOOD!!!\n\tYou are Healthy.")
else:
    print("\n\tOHHH MY GOD!!!\n\tYou are Sick.")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021
    
'''Q.6. Design an algorithm using pseudo code or flowchart to read customer’s name,
purchase amount and compute the final bill amount after applying the discount.
A shopping mall offers a discount to its customers as stated below. 
	      Purchase Amount	Discount 
                  -----------------------	------------
0     - 100 		      2%
101 - 200 		      3%
201 - 300		      4%
>300			    10%
'''
print("\nQ.6. Discount Question") 
name = input("Enter customer name: ")
PA = float(input("Enter purchase amount: "))

if(PA >= 0 and PA <= 100):
    disc = PA * 0.02
elif(PA >= 101 and PA <= 200):
    disc = PA * 0.03
elif(PA >= 201 and PA <= 300):
    disc = PA * 0.04
else:
    disc = PA * 0.1

FB = PA - disc
print("\n\t*****Welcome to STAR MALL*****\n\tYou Final Bill is Here\n\nCustomer Name\t: ",name,
      "\nPurchase Amount\t: ",PA,"\nDiscount Amount\t: ",disc,"\nFinal Bill\t: ",FB)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021