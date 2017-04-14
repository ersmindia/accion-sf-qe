'''Exercise 2:
A) Ask the user for a number. print a message if the number is odd or even.
B) If the number is a multiple of 4, print out a message "The number is multiple of 4".
'''

num = raw_input("Enter the Number: ")

try:
    num = int(num)
    if(num%2 == 0):
        print "Even"
    else:
        print "Odd"
    
    if(num%4 == 0):
        print "Yes, this Number is multiple by 4"
    else:
        print "No, this Number is not multiple by 4"
except ValueError:
   print "Enter a valid Number"

    
