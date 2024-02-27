"""
GE 120: Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz 
2023-03941
"""

print('Enter here: ')
decimal = input()

# degrees
deg = (int(float(decimal)//1))

# minutes
min = (int(((float(decimal)-float(deg))*60)//1))
min2 = ((float(decimal)-float(deg))*60)

#seconds
sec = (round((float(min2)-float(min))*60,2))

print( deg, "deg", min, "min" , sec, "sec") 

#NEXT