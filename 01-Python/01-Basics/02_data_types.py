# Nov 9th 2025 Variables, Data types, Operators

#Data Types
#In any programming language data types are very important, where it helps to define like what kind of data it is carrying.

#Text: str
x = "Sai"
print(type(x))

#Numeric: int, float, complex
x = 10
y = 10.2
z = 21j
print(type(x))
print(type(y))
print(type(z))

#Sequence: list, tuple, range
x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
z = range(6)
print(type(x))
print(type(y))
print(type(z))

#Mapping: dict
x = {"name": "Sai", "age": 25}
print(type(x))

#Set: set, frozensset
x = {"apple", "banana", "cherry"}
print(type(x))
y = frozenset({"apple", "banana", "cherry"})
print(type(y))

#Boolean: bool
x = True
print(type(x))
y = False
print(type(y))


#Below Dat Types are advanced where we won't use much
#Binary: bytes, bytearray, memoryview
x = b"Hello"
y = bytearray(5)
z = memoryview(bytes(5))
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#None: NoneType
x = None
print(x)
print(type(x))