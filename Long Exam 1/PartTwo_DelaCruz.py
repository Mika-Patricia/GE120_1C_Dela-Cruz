print("Direct Leveling Computations coded by Mika Patricia G. Dela Cruz.")
print("This will compute data on direct levelling")

from tabulate import tabulate #for the table

#variables
bs = () #for backsight
fs = () #for foresight
HI = () #for Instrument Height
tp_elev =() #turning point elevation

dist = 0 #for distance
distance = [] #list for the sum of distance

levelling_table =[] #list of levelling table
total_distance = sum(distance) #getting the total distance
tp_counter = 0 #start tp_counter to zero

run_elev = 0

prompt = 0
def floatInput(prompt):
    prompt = input()
    fl_output = (float(prompt))
    return fl_output

"""
Prameter prompt. This function contains the input function with prompt as its parameter. It makes sure that its output is converted to float data type.
"""

print("Initial elevation of BM0: ")
elev = floatInput(prompt)


run_elev += elev

distance.append(dist)


i=0
while True:
 i=i+1
 print("Sta.", i)
 sta = ("BM1", "TP"+ str(i-1), "TP"+ str(i-1),"TP"+ str(i-1),"TP"+ str(i-1),"TP"+ str(i-1)) 
 
 
 print("Backsight: ") 
 bs = floatInput(prompt) #gets bs

 print("Foresight: ") 
 fs = floatInput(prompt) #gets fs

 print("Distance: ") 
 distance = floatInput(prompt) #gets distance

 HI = run_elev + bs #formula for Instrument Height
 Elev1 = HI - fs #formula for Elevation



 levelling_table.append([sta[i-1],bs, HI,fs, Elev1]) #to add to the list
 header = ["Sta.", "BS", "HI", "FS", "Elev"] #headers to be used for columns
 
 print("Add a new measurement? [y/n] If last line type: L "); choice = str(input())
 if choice.lower() == "y" : #if "y", will continue
    continue
 elif choice.lower() == "n": #if "n", will end
    break
 elif choice == "L": #if last Line
    i = 0
    break
 else:
    break

print(tabulate(levelling_table, header, tablefmt="fancy_grid")) #will print the table