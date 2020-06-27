#!/usr/bin/ python

#printing
print("Hello World")

#take user input
# input("How old are you?")

#variables
a = 10 + 10
print(a)

#if function
b = 1
c = 2
if (b == 1 and c == 3):
    print("it worked")
else:
    print("it failed")

#if and in functions
Hamad = "flag{cracked1281297387213}"
if "flag" in Hamad:
    print(Hamad)
else:
    print("Not found")

#string
string = "This data here is string, stored in a variable called hello"

#integer
integer = 66

#float
float = 9.3

#list
list = ["Hamad", "Abdulla", "Abualshook"]

#dictonary
First_Name = ""
Second_Name = ""
Last_Name = ""
dictionary = {First_Name: "Hamad", Second_Name: "Abdulla", Last_Name: "Abualshook"}

#global variable
global1 = "This is a global variable"

#local variable
def local_variable_function():
    local = "This is a local variable, can be accsssed in the same function ONLY"

#Take and store user input
Name = input("Type in your name: ")
print(Name)

#By default user input will be string, we can change it by adding the type we want and print the type
Age =  int(input("Enter your age: "))
type(a) #This will print only the data type to check the type
#add bool() for boolean, str() for string and float() for float


#function2
def UserName(): #Function or also known as defenition in Python
    Name = input("What is your name: ") #Takes user input and stores it in Variable called name, this variable is also called local variable (can be accssed only in the same function)
    return Name #to exit the fucntion
print(UserName())

#function3 with a parameter, it will take two parameters, creator and assignment
def TryHackMe(creator, assignment)
    print(creator, assignment)
    return
Creator = input("What is the name of the creator: ")
Assignment = int(input("Which number: "))
TryHackMe(Creator, Assignment)

#if statment
website = "tryhackme"
if website == "tryhackme":
    print("This is true")

#elif statment
website = "tryhackme"
if website == "tryhackme":
    print("This is true")
elif website == "google":
    print("wrong site")
else:
    print("none is true")

#if statment with operators
website = "tryhackme"
name = "i7md"
if website == "tryhackme" and name == "i7md":
    print("This is true")
elif website == "google" and name == "Hamad":
    print("wrong site")
else:
    print("none is true")

#Python got two loops: for loop and while loop:
#while loop
while True:
    print("Spam")

#Incrementation or number of looping time
# Note that doing i += 1 is the same as i = i + 1
i = 0
while i <= 10:
    print(i) #This will print numbers from 0 to 1
    i += 1

#For loop
People = ["Hamad", "Abdulla", "Ebrahim"]
for i in People:
    print(i) #This will print all the names

#Increment in loop
for i in range(0,10):
    print(i) #This will print 10 times, because first parameter is start point and second parameter is end point

#Size in loop
for i in range(0,10,2):
    print(i) #This will do the same as above, however it will be bigger in 2. Other words it will print even numbers

#We can also add an else at the end
for i in range(0,10,2):
    print(i)
else:
    print("Done") #This will print the word done after the end of the loop

#Opening files using Python
text = open("file_name", "mode")
#If the script is in the same directory just put the file name eg: hello.txt
#if not in the same directory, put the full path eg: /root/home/Desktop/hello.txt
#r: this mode will only read the file
#w: this mode will write data to file, the existing file will be deleted as this count as editing
#a: append content at end of the file
#r+: this is a special read, it will read and write the file

text = open("hello.txt", "r")
print(text.read()) #This will open the file and read it only (no modification)

#we can also print a line or lines, if we want to print just a line we add text.readline()
#for multiple lines or all lines we add, text.readlines()

text = open("hello.txt", "r")
for line in text: #this creates a variable called line and loops
    print(line, end='') #the loop will print each line and end with ''

#This is an example who we write data into a file
text = open("hello.txt", "w")
text.write("This is how we write into file !!!")
#However, this will overwrite our whole file, a better way is to use text.append() and
#when finished modifying we add text.close()

