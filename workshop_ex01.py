# Write a program to find aliquot of a number? 

def aliquotSequence(n):
    sequence = []
    for i in range(1,n+1):
        if(n%i== 0):
            sequence.append(i)
    return sequence

print aliquotSequence(10)

print "My name is Khan"

print "I am from India"