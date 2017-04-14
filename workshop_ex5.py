''''
Exercise 3:
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

'''

dict = {'a':1, 'b':2, 'c':3}
dict1 = dict.copy()

print dict1

newDict1 = {'a':4, 'b':5}

dict1.update(newDict1)


print "dict", dict
print "dict1", dict1