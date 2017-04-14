'''Exercise 1:
A) Create a program that asks the user to enter their name and their age. Print out a message that tells them the year that they will turn 50 and 100 years old.
B)Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
'''
from datetime import datetime
name = raw_input("Enter your name: ")
age = int(raw_input("Enter your Age: "))
thisYear = datetime.today().year

result =  "You will turn 50 @ " + str(thisYear - age + 50) + " and you will turn 100 @ " + str(thisYear - age + 100)
print result
numbersToPrint = int(raw_input("Number of copies to print: "))

for i in range(numbersToPrint):
    print result
