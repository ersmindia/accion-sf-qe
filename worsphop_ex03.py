'''
Write a program to sort the list without using predefined functions
   ['APPLE', 'FOX', 'ANT', 'BAT', 'BALL']
'''

alpList = ['APPLE', 'FOX', 'ANT', 'BAT', 'BALL']

alpLength = len(alpList)
for j in range(alpLength, 0, -1):
    for i in range(j-1):
        if(alpList[i]>alpList[i+1]):
            temp = alpList[i]
            alpList[i] = alpList[i+1]
            alpList[i+1] = temp

print alpList
