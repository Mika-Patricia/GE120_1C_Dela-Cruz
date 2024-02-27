#LECTURE 2: PROCEDURAL PROGRAMMING

#print hello world
print("Kumusta Mundo")

#type("Hello World") => str
print(type("Kumusta Mundo"))

# coverting number to a string
print(type(1))
print(type(str(1)))

# commenting using ctrl+/

# CONCATENATION - adding two strings together
print("Wazzup " + "GE 120 ")

"""
This is a multiline comment
This is a multiline comment
"""

# this is a single line comment

print("this is a comment") #this is an inline comment

#Different DATA TYPES
print(type("STRING")) #str
print(type(54)) #int
print(type(3.14159469)) #float
print(type(1+4j)) #complex

#Converting DATA TYPES
print(type(float(54)))#convert into float

#VARIABLES
x = 2
y = 13

#ARITHMETIC OPERATIONS
print("Sum of x and y:", x + y)
print("Difference of x and y:", x - y)
print("Product of x and y:", x * y)
print("Quotient of x and y:", x / y) 
print("Floor Quotient of x and y:", x // y)
print("Power of x and y:", x ** y)
print("Remainder of x and y:",x % y)
print("Absolute Value of x and y:",abs(y))
print("Float of x and y:",float(y))
print("Value of x and y:",complex(y))
print("Divmod  of x and y:",divmod(y,x))

#LISTS
dog = ["golden retriever", " husky"]
print(dog)