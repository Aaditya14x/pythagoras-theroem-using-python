#Pythagoras theorem Program in python
from math import sqrt
B = int(input("Enter the base of triangle : ")) #Let Base be represented by "B"
P = int(input("Enter the perpendicular distance of triangle :")) #Let Perpendicular be represented by "P"
H= sqrt(P**2+B**2) #Let Hypotenous be represented by "H" and H = square root of ((P^2)+(B^2))
print(int(H))
