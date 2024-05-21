
owner = input("Owner:")
area = input("Area:")
owner2 = input("Other Owner: ")
area2 = input("Other Owner's Area: ")

class Parcel: 
#initialize Parcel with parameters owner, the name of the owner in strings and parameter area, the size of the lot area in sq m in integer
    def __init__(self, owner, area):
        self.owner = str(owner)
        self.area = int(area)
        
#method for the Parcel Object. When called, will return a string based on the following rules for classification
    def getClassification(self):

       if area < 10000: 
            Classification = "residential"
       elif area > 10000 and area < 120000:
            Classification = "Private agricultural"
       elif area > 120000 :
            Classification = "Public Agricultural"
       else:
            Classification = "EWAN KO"

       return Classification

class Riparian(Parcel): 
 # Riparian object wih parameter owner, name of the owner in string, parameter area, size of the lot area in sq m in integer, and parameter type that indictes the type of land in int
 def __init__(self, owner2, area2, type):
        self.owner2 = str(owner2)
        self.area2 = int(area2)
        self.type = str(type)

 def getAdjoiningWaterbody(self): #Once called, will return meaning based from type according to rules set
    
   if type == 1:
     meaning = "Adjacent to River - can be subject to titling"
   elif type == 2:
     meaning = "Adjacent to Ocean (Littoral) - cannot be subject to titling"
   else:
    meaning = "Invalid Riparian Parcel"
     
   return meaning




print("A Parcel of Land Owned by" , Parcel(owner) , "with an area of", Parcel(area), "square meters") 

SUM = Parcel(area) + Riparian (area2) #Get sum
print("Consolidation lot of" , Parcel(owner) , "and"+ Riparian(owner) , " with  a total area of", SUM , " square meters")


