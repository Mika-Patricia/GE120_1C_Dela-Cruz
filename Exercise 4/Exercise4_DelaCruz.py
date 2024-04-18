
""""
GE120 Intro to OOP Geomatic Application
Mika Patricia G. Dela Cruz
2023-03941
"""


import math

class Line:

    def __init__(self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth

    def latitude(self):
        '''
        Compute for the latitude of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        latitude - float
        '''

        latitude = -float(self.distance) * math.cos(math.radians(self.azimuth))

        return latitude
    
    def departure(self):
        '''
        Compute for the departure of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        departure - float
        '''

        departure = -float(self.distance) * math.sin(math.radians(self.azimuth))

        return departure
    
    def bearing(self):
        '''
        Compute for the DMS bearing of a given angle.

        Input:
        azimuth - float

        Output:
        bearing - string
        '''
        
        if azimuth > 0 and azimuth < 90:
            bearing = 'S {: ^5} W' .format (round(azimuth,3))
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {: ^5} W' .format (round(180 - azimuth,3))
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {: ^5} E' .format (round(azimuth - 180,3))
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {: ^5} E' .format (round(360 - azimuth,3))
        else:
            bearing = "UNKNOWN"

        return bearing
    
class Cardinal(Line):

    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)
    
    def bearing(self):
        if azimuth == 0:
            bearing = "Due South"
        elif azimuth == 90:
            bearing = "Due West"
        elif azimuth == 180:
            bearing = "Due North"
        elif azimuth == 270:
            bearing = "Due East"
        else:
            bearing = "UNKNOWN"
        return bearing
    
# CREATE A SENTINEL CONTROL GROUP
counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("LINE NO.", counter)

    bobo_magtype = False
    while not(bobo_magtype):
        distance = input("Distance: ")
        if bobo_magtype:
            print("WHY SO BOBO MAGTYPE?")
            continue
        if not(bobo_magtype):
            break
    azimuth = input("Azimuth from South: ")

    if "-" in str(azimuth): #if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))
    else: #if user gives DD
        azimuth = float(azimuth)%360

    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else:
        line = Line(distance, azimuth)

    sumLat += line.latitude()
    # same as sumLat = sumLat + lat 
    sumDep += line.departure()
    sumDist += float(line.distance)

    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

    # ASK FOR INPUT 
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break
        
# print(lines) 
print("\n\n")
print('{:^10} {:^10} {:^10} {:^10} {:^10}'.format("LINE NO. ", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print('{:^10} {:^10} {:^10} {:^10} {:^10}'.format(line[0], line[1], line[2], round(line[3],3), round(line[4],3)))

print("SUMMATION OF LAT: ", sumLat)
print("SUMMATION OF DEP: ", sumDep)
print("SUMMATION OF DIST: ", sumDist)

lec = math.sqrt(sumLat**2 + sumDep**2)

print("LEC: ", lec)
rec = sumDist/lec

print("1: ", round(rec, -3))