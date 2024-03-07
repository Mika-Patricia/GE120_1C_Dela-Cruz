"""
GE 120: Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz 
2023-03941
"""

from tabulate import tabulate #for the table

#variables
i=0
dist = 0
azi = 0
yesorno = ("y", "n")
table_data = []


#loop
while True: 
  
  #Outputs Line from startingg number to end number.
  i= i+1
  print("\n LINE",i, "-", i+1 )
  line = ("LINE"+ str(i)+ "-"+ str(i+1))

  #Gets the distance from the user
  print("Enter Distance in meters (XXX.xxx): ")
  dist = (float(input()))

  #Gets the azimuth from south from the user
  print("Enter Azimuth from South (XXX.xxx): ")
  azi = (input())
  

  if "-" in azi:
   #DMS to DECIMAL

    #split
    azi = azi.split("-")

    #assign variables
    deg1 = float(azi[0])
    min1 = float(azi[1])
    sec1 = float(azi[2])

    #output (and formula)
    azi = (((deg1) + ((min1)/ 60) + ((sec1)/3600)))
    

  else:
    azi = (float(azi) % 360) 

  
  #converts dec(az_s) to bearing
  if azi == 360 or azi == 0:
    direction = (" ", " due South")
    decimal = 0
  elif azi>270 and azi <360:
   direction = ("S "," E")
   decimal = 360-azi
  elif azi == 270:
   direction = (" ", " due East")
   decimal = 0
  elif azi > 180 and azi <270 :
    direction = ("N ", " E")
    decimal = azi-180
  elif azi == 180:
    direction = ("", " due North")
    decimal = 0
  elif azi > 90 and azi<180:
   direction = ("N ", " W")
   decimal = 180-azi
  elif azi == 90:
   direction = ("", "due West")
   decimal = 0
  elif azi > 0 and azi<90:
    direction = ("S ", " W")
    decimal = azi
  else :
    direction = ("invalid","input")
    decimal = 0
    
 
  #decimal to DMS
  deg = (int(float(decimal)//1))
  min = (int(((float(decimal)-float(deg))*60)//1)) #minutes (formula); this is without the decimals
  min2 = ((float(decimal)-float(deg))*60) #this is with the decimals which will be used in computing for seconds
  sec = (round((float(min2)-float(min))*60,2)) #seconds (formula)
  bearing = (str(deg)+ "-"+ str(min)+ "-"+ str(sec)) #without direction
  #bearing
  bearing2 = (direction[0]+ str(bearing)+ direction[1])

 
  header = ["Line", "Distance", "Bearing"] #name of table header
  table_data.append([line, dist, bearing2]) #to add new lines to the data


  print("Add a new LINE? [y/n]"); choice = str(input())
  if choice.lower() == yesorno [0]: #if "y",line will continue
    continue
  elif choice.lower() == yesorno[1]: #if "n", line will end
    break
  elif choice.lower() != yesorno : #if neither "n" or "y", invalid. line will end.
    print("answer not yes[y] or no[n]. Line will end.")
    break

#output
print("---------------------------------")
print("Summary")

#prints the table
table = tabulate(table_data, header, tablefmt="fancy_grid")  
print(table)
  