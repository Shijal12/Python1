#this is a comment
print("Hello, World!")

#variables
x = 5
y = "John"
print(x)
print(y)

#Casting
a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0

print(a)
print(b)
print(c)

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Global
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
