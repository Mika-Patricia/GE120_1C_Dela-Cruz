from tabulate import tabulate #for the table
import math 

#variables
i=0
dist = 0
azi = 0
yesorno = ("y", "n")
table_data = []
Lat = []
Dep = []
distance =[]

def getLat(dist,azi):
  lat = (-dist* math.cos(math.radians(DMS(azi))))
  return  lat

def getDep(dist,azi):
  dep = (-dist*math.sin(math.radians(DMS(azi))))
  return dep

def DMS(azi): #DMS to DECIMAL
  
  if "-" in azi:
    azi = azi.split("-")  #split
    DMS = {"deg1": float(azi[0]),   "min1" : float(azi[1]),  "sec1" : float(azi[2])} #make dictionary
    azi1 = (((DMS["deg1"]) + ((DMS["min1"])/ 60) + ((DMS["sec1"])/3600))) # formula
    return azi1 
  
  else:
    azi2 = (float(azi) % 360)
    return azi2
  
def bearingDEC(azi):

   if DMS(azi) == 0:
     dueSouth = ("", 0, "due south")
     return dueSouth

   elif DMS(azi)>270 and DMS(azi) <360:
     SE = ("S", 360-DMS(azi), "E")
     return SE

   elif DMS(azi) == 270:
     dueEast = ("", 0, " due East")
     return dueEast

   elif DMS(azi) > 180 and DMS(azi) <270 :
     NE = ("N ", DMS(azi)-180," E")
     return NE

   elif DMS(azi) == 180:
     dueNorth = ("", 0, " due North")
     return dueNorth

   elif DMS(azi) > 90 and DMS(azi)<180:
     NW = ("N ", 180-DMS(azi), " W")
     return NW

   elif DMS(azi) == 90:
     dueWest = ("", 0, "due West")
     return dueWest


   elif DMS(azi) > 0 and DMS(azi)<90:
     SW = ("S ", DMS(azi), " W")
     return SW

   else :
     return False

def AzimuthToBearing(bearingDEC):
  

  deg = (int((bearingDEC(azi)[1]))//1)
  min = (int((float(bearingDEC(azi)[1])-float(deg))*60)//1) #minutes (formula); this is without the decimals
  min2 = ((float(bearingDEC(azi)[1])-float(deg))*60) #this is with the decimals which will be used in computing for seconds
  sec = (round((float(min2)-float(min))*60,2)) #seconds (formula)
  bearing = (str(deg)+ "-"+ str(min)+ "-"+ str(sec)) #without direction

  bearing2 = (bearingDEC(azi)[0]+ str(bearing)+ bearingDEC(azi)[2])

  return bearing2

def LEC(Lat,Dep):
  LEC = math.sqrt((sum(Lat)**2)+(sum(Dep)**2))
  return LEC
  
def REC(Lat,Dep):
  REC_denom = sum(distance)/LEC(Lat,Dep)
  return REC_denom



#loop
while True:

  #Outputs Line from startingg number to end number.
  i= i+1
  print("\n LINE",i, "-", i+1 )
  line = ("LINE"+ str(i)+ "-"+ str(i+1))  
  dist = (float(input("Enter Distance in meters (XXX.xxx): "))) #Gets the distance from the user
  azi = (input("Enter Azimuth from South (XXX.xxx): "))  #Gets the azimuth from south from the user
  
  Lat.append(getLat(dist,azi))
  Dep.append(getDep(dist,azi))
  distance.append(dist)

  header = ["Line", "Distance", "Bearing", "Latitude", "Departure"] #name of table header
  table_data.append([line, dist, AzimuthToBearing(bearingDEC), getLat(dist,azi), getDep(dist,azi)]) #to add new lines to the data


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

print("The LEC is ",round(LEC(Lat,Dep),3))
print("The REC is 1:",round(REC(Lat,Dep),-3))

