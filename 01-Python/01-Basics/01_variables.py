# Nov 9th 2025 Variables, Data types, Operators

#Variables
x = 10
y = "Sai"
print(x)
print(y)

print(str(x) + y)
print(str(x) + " " + y)

print("Hello", "World")
print("Hello" + "World")


#Variable will get override
m = 10
m = "Sai"
print(m)

#To check variable data type
m = 10
n = "Sai"
print(type(m))
print(type(n))

#We can declare string variables either double quotes "" or single quotes ''
m = "Sai"
n = 'Sai'
print(m)
print(n)

#Declare same variables with case-sensitive, it will take as different variable
a = 10
A = "Sai"
print(a)
print(A)



#Assign multiple variables
x,y,z = 10,"Banana",20.08
print(x)
print(y)
print(z)

x=y=z="Orange"
print(x)
print(y)
print(z)


#Collection
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)



#Advanced Concept - Global Variables
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()


#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)