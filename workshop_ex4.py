''''
Exercise 4:
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list without any duplicates(donot use any predefined function).

'''

def removeListDuplicates(lis):
    results = []
    for i in lis:
        if (i not in results):
            results.append(i)
    return results

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print removeListDuplicates(a)