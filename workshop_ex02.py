# -*- coding: utf-8 -*-
'''
2. Write a program that return the type of the triangle based on the 
    A. 3 sides given as arguments to the method.
    B. 3 angles given as arguments to the method.


Equilateral triangle "The Equilateral triangle shown on the left has three equal sides and three equal angles."
Isosceles triangle "The Isosceles triangle shown on the left has two equal sides and two equal angles."
Scalene Triangle "The Scalene Triangle has no congruent sides (each side must have a different length..)"

Acute Triangle "The Acute Triangle has three acute angles. an acute angle measures less than 90°"
Obtuse Triangle "an obtuse angle has more than 90"
Right Triangles "A right triangle has one 90°"

'''
def getTringletypeBasedonSides(s1,s2,s3):
    if(s1==s2==s3):
        return "Equilateral triangle"
    elif(s1==s2 or s2==s3 or s1==s3):
        return "Isosceles triangle"
    else:
        return "Scalene Triangle"
    
def getTringletypeBasedonAngles(a1,a2,a3):
    if(a1==a2==a3):
        return "Equilateral triangle"
    elif(a1<90 and a2<90 and a3<90):
        return "Acute Triangle"
    elif(a1>90 or a2>90 or a3>90):
        return "Obtuse Triangle"
    elif(a1==90 or a2==90 or a3==90):
        return "Right Triangles"
        
    

side1 =  int(raw_input("Enter the length of First side"))
side2 =  int(raw_input("Enter the length of Second side"))
side3 =  int(raw_input("Enter the length of Third side"))

print getTringletypeBasedonSides(side1, side2, side3)

angle1 = int(raw_input("Enter the angle of First corner"))
angle2 = int(raw_input("Enter the angle of Second corner"))
angle3 = int(raw_input("Enter the angle of Third corner"))

print getTringletypeBasedonAngles(angle1, angle2, angle3)


