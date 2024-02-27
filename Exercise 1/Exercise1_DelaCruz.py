"""
GE 120: Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz 
2023-03941
"""

print('Enter here: ')
decimal = input()
print(decimal)

# degrees
print(int(float(decimal)//1))

deg = (int(float(decimal)//1))

# minutes
min = (int(((float(decimal)-float(deg))*60)//1))

print(min)

min2 = ((float(decimal)-float(deg))*60)

#seconds

sec = (round(float(min2)-float(min))*60)

print(round(sec,2))

