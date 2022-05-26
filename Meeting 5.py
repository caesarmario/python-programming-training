# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to print Hello 10 times.
cnt = 1
while(cnt <= 10):
    print("Hello")
    cnt = cnt + 1 #cnt += 1

for cnt in range(10):
    print(cnt,"1st for Hello")

for cnt in range(1,11):
    print(cnt,"2nd for Hello")

for cnt in range(1,11,2):
    print(cnt,"3rd for Hello")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to print numbers from 1 to 20 and also display addition of all numbers.
cnt = 1
add = 0
while(cnt <= 20):
    print(cnt)
    add = add + cnt
    cnt = cnt + 1 #cnt += 1
print("Addition is: ",add)

add1=0
for cnt in range(1,21):
    print(cnt)
    add1 = add1 + cnt
print("For addition is: ",add1)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program a program to accept number from user and print Time Table or given number in
following format
(eg.
Enter your number: 5
Time table of 5 is:
5 x 1 = 5
5 x 2 = 10
-
-
5 x 10 = 50)

no = int(input("Enter your number: "))
cnt = 1
print("Time Table for ",no," is: ")
while(cnt<=10):
    mult = no * cnt
    print (no," X ",cnt," = ",mult)
    cnt=cnt+1
    
no=in(input("\nEnter your number: "))
print("For loop Time Table for ",no," is: ")
for cnt in range (1,11):
    mult = no * cnt
    print(no," X ",cnt," = ",mult)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to display all even numbers between 1 to 25.
cnt = 1
while (cnt<=25)
    if(cnt%2==0)
        print(cnt)
    cnt=cnt+1

for cnt in range(1,25)
    if(cnt%2==0)
        print(cnt)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#Write a program to print all EVEN number and ODD number between 1 to 25
#Also display addition of all even numbers and odd numbers at the end
cnt = 1
evensum = 0
oddsum = 0
print("\nWhile loop OUTPUT\nEVEN\tODD")
while(cnt<=25):
    if(cnt%2==0):
        print(cnt)
        evensum=evensum+cnt
    else:
        print("\t",cnt)
        oddsum=oddsum+cnt
    cnt=cnt+1
print("Addition of all EVEN numbers: ",evensum,
      "\nAddition of all ODD numbers: ",oddsum)

evensum1 = oddsum1 = 0
print("\nFor Loop OUTPUT \nEVEN\tODD")
for cnt in range(1,26):
    if(cnt%2==0):
        print(cnt)
        evensum1=evensum1+cnt
    else:
        print("\t",cnt)
        oddsum1=oddsum1+cnt
print("Addition of all EVEN numbers: ",evensum1,
      "\nAddition of all ODD numbers: ",oddsum1)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

'''
Write a program to print the Total, Percentage (average) and Grade of a student by
accepting student name, tpnumber, and 5 subjects marks.
(Note:   A+   100-80   A    80-75     B+   75-70
         B    70-65    C+   65-60     C    60-55
         C-   55-50    D    50-Below
'''
name=str(input("Enter your name: "))
tpnum=input("Enter TP Number of "+name+" : ")
print("Enter 5 subject marks here: ")
no1=int(input("Enter 1st subject marks: "))
while (no1>100 or no1<0):
    print("\nWrong input!, it must be less than 100 or greater than 0.")
    no1=int(input("Kindly enter your 1st subject marks again: "))
no2=int(input("Enter 2nd subject marks: "))
while (no2>100 or no2<0):
    print("\nWrong input!, it must be less than 100 or greater than 0.")
    no2=int(input("Kindly enter your 2nd subject marks again: "))    
no3=int(input("Enter 3rd subject marks: "))  
while (no3>100 or no3<0):
    print("\nWrong input!, it must be less than 100 or greater than 0.")
    no3=int(input("Kindly enter your 3rd subject marks again: "))
no4=int(input("Enter 4th subject marks: "))
while (no4>100 or no4<0):
    print("\nWrong input!, it must be less than 100 or greater than 0.")
    no4=int(input("Kindly enter your 4th subject marks again: "))
no5=int(input("Enter 5th subject marks: "))
while (no5>100 or no5<0):
    print("\nWrong input!, it must be less than 100 or greater than 0.")
    no5=int(input("Kindly enter your 5th subject marks again: "))
total = no1+no2+no3+no4+no5
avg = total/5
print("\n\n\t ***** WELCOME TO APU *****")
print("\t ***** RESULT IS HERE *****")
print("Name\t\t : ",name)
print("TPNumber\t : ",tpnum)
print("Subject Marks\t : ",no1,no2,no3,no4,no5)
print("Total is\t : ",total)
print("Average is\t : ",avg)
if(avg<=100 and avg>=80):
    print("Grade is\t :  A+")
elif(avg<80 and avg>=75):
    print("Grade is\t :  A")
elif(avg<75 and avg>=70):
    print("Grade is\t :  B+")
elif(avg<70 and avg>=65):
    print("Grade is\t :  B")
elif(avg<65 and avg>=60):
    print("Grade is\t :  C+")
elif(avg<60 and avg>=55):
    print("\nGrade is\t :  C")
elif(avg<55 and avg>=50):
    print("Grade is\t :  C-")
else:
    print("Grade is\t :  Fail/D")
print("\t ***** END OF RESULT  *****")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021