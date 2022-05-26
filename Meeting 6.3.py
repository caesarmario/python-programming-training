# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

'''
File - store data permanently
file - create, write, read, modify, delete
mode - w, r, a    - w-write, r-read, a-append (write/read)
'''

#Create file
myfile = open("testing.txt","w")
print("file created successfully")
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#write data in file
myfile = open("testing.txt","w")
myfile.write("Tanveer")
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#will overwrite
myfile = open("testing.txt","w")
myfile.write("John")
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#will append data
myfile = open("testing.txt","a")
myfile.write("Hunt")
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021
name=input("Enter your name here: ")
myfile = open("testing.txt","a")
myfile.write("\n"+name)
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#read
myfile = open("testing.txt","r")
print(myfile.read())
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#write multiple value
myfile=open("data.txt","a")
tp = input("Enter your tp number: ")
name = input("Enter your name: ")
phone = input("Enter mobile number here: ")
myfile.write(tp)
myfile.write("\t"+name)
myfile.write("\t"+str(phone))
myfile.write("\n")
#myfile.write(tp+"\t"+name+"\t"+str(phone)+"\n")
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

myfile=open("data.txt","a")
size = int(input("How many record do you want to store: "))
for cnt in range(size):
    tp = input("Enter your tp number: ")
    name = input("Enter your name: ")
    phone = input("Enter mobile number here: ")
    myfile.write(tp+"\t"+name+"\t"+str(phone)+"\n")
myfile.close()

myfile=open("data.txt","a")
print(myfile.read())
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

myfile=open("data.txt","r")
print(myfile.read())
myfile.close()
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#search data
data = str(input("Enter what you want to search in file: "))
myfile = open("data.txt")
for line in myfile:
    if(line.startswith(data)):
        print(line)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021

#rstrip
data=input("Enter customer detail: ")
myfile = open("data.txt")
for line in myfile:
    line = line.rstrip()
    if data in line:
        print(line)
# Mario Caesar
# linktr.ee/caesarmario_
# 5 Feb 2021