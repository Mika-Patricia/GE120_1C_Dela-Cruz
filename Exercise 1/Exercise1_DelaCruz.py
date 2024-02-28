"""
GE 120: Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz 
2023-03941
"""
print("Welcome! This is a Decimal to Degree-Minute-Second Converter and vise versa.")

#DECIMAL to DMS

#input
print('Enter decimal (XXX.xxx) here: ')
decimal = input()

#degrees (formula)
deg = (int(float(decimal)//1))

#minutes (formula)
min = (int(((float(decimal)-float(deg))*60)//1)) #this is without the decimals
min2 = ((float(decimal)-float(deg))*60) #this is with the decimals which will be used in computing for seconds

#seconds (formula)
sec = (round((float(min2)-float(min))*60,2))

#output
print("Here is ",decimal, "in DegMinSec: ")
print(deg,"-",min,"-",sec) 

#DMS to DECIMAL

#input
print('For Enter DMS (XX-XX-XX.xx) here:  ')
DMS = input()

#split
DMS1 = DMS.split("-")

#assign variables
deg1 = float(DMS1[0])
min1 = float(DMS1[1])
sec1 = float(DMS1[2])

#output (and formula)
print("Here is", DMS, "in DECIMAL:")
print(round(((deg1) + ((min1)/ 60) + ((sec1)/3600)),3))
