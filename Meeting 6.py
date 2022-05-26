# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

# Python List
mylist = [11,12,13,14,15]
print(mylist)
print(mylist[0])
print(mylist[2])
print(mylist[4])
print(mylist[5])
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#WAP to accept 5 different value from user and store it in list. Display list elements.
mylist=[]
print("Enter 5 values here: ")
for cnt in range(5):
    no=int(input("Enter value here: "))
    mylist.append(no)

print(mylist)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#WAP to accept size of list elements from user.
#Accept values from user as per defined size. Store it in list.
#Display list. Also display addition of all list elements at the end.
mylist = []
add = 0
add1 = 0
size = int(input("Enter size of list element: "))
for cnt in range(size):
    element = int(input("Enter "+str(cnt+1)+" value here: "))
    mylist.append(element)

print("List elements are: ",mylist)

for cnt in range(size):
    add = add + mylist[cnt]
print("Addition of list elements with range function: ",add)

for cnt in mylist:
    add1 = add1 + cnt
print("Addition of list elements without range function: ",add1)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#WAP to accept size of list from user and as per size enter elements in list.
#Print all EVEN elements of list elements.
mylist = []
size = int(input("Enter size of list element: "))
print("Enter ",size," values in list: ")
for cnt in range(size):
    no = int(input("Enter "+str(cnt+1)+" value: "))
    mylist.append(no)

print(mylist)

print("All EVEN Numbers of list elements with range are: ")
for cnt in range(size):
    if(mylist[cnt]%2 == 0):
        print(mylist[cnt])

print("All EVEN Numbers of list elements without range are: ")
for cnt in mylist:
    if(cnt%2 == 0):
        print(cnt)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021