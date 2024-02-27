"""
GE 120: Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz 
2023-03941
"""

print('Enter decimal here: ')
decimal = input()

# degrees
deg = (int(float(decimal)//1))

# minutes
min = (int(((float(decimal)-float(deg))*60)//1))
min2 = ((float(decimal)-float(deg))*60)

#seconds
sec = (round((float(min2)-float(min))*60,2))

print( deg, "-", min, "-" , sec, "-") 

#NEXT

print('For DMS, Enter deg here:  ')
deg1 = input()

print('For DMS, Enter min here:  ')
min1 = input()

print('For DMS, Enter sec here:  ')
sec1 = input()

print(round((float(deg1) + (float(min1)/ 60) + (float(sec1)/3600)),3))
