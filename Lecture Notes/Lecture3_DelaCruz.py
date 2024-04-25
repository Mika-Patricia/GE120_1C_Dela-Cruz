#Lecture 3 notes

#lists
listahan = ["mafe ", "justin", "mika", "uste" ]
print(listahan[2])

print(listahan [0,2])

print(listahan)

#tuples

# Lecture 3Notes

# LISTS
listahan = ["mafe", "justin", "mika", "uste"]
# print(listahan)

# gusto si mika makuha (position)
# print(listahan[2])

# subset of the list, mafe and si justin
# print(listahan[0:2])

# print(listahan[1:3])

# nagstastart sa simula
# print(listahan[:3])

# start from index, end sa dulo
# print(listahan[2:])

# print(listahan[-1])
# print(listahan[-2])

# gets first item, last item, then those in between
# print(listahan[-3:3])

# Addition of Lists
# print(listahan[0:2]+listahan[2:4])
# print(listahan[0:4])

listahan[0] = "chelzy"
# print(listahan)

# TUPLES
tuple_1 = ("maja", "gianna", "jewel")
# print(tuple_1)

# tuples are immutable
# tuple_1[0] = "quinmar"

# print(tuple_1)

# NESTED LISTS
list_1 = [ ["apple", "bola", "carton"] , ["apricot", "banana", "cow"]  ]
# print(list_1[0][2])

# NESTED TUPLES
tuple_2 = ((12.1244, -12.12414),(35.46261,-67.1231),(123.124, 56.232))
# print(tuple_2[2][0])

# DICTIONARIES - key value pairs
dog = {
        "name": "Bogart",
        "age": 2,
        "color": "white",
        "favorite_num": 3.14,
        1.113: 45  #pwede si number as key (float or int)
       }

# print(dog[1.113])
# print(dog.values())  #returns a list of values
# print(dog.keys())  #returns a list of keys

dog["favorite_num"] = 39

# print(dog["favorite_num"])


# LOOPS AND BREAK CONTINUE AND PASS

# for number in range(10):
#     if number == 5:
#         pass

rec = 0
while rec <= 5000:
    rec = int(input("enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        pass
        print("onti nalang kulang, kaya mo yan")
    print("kulang ka ng REC na", kulang)

print("PASOK NA REC")
print("-------END-----")