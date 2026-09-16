print("--------------Identity Operators----------------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x  == y)
print(x is y)

print("-------------------Membership Operators---------------")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple","banana", "cherry"]
print("kiwi" not in fruits) 


print("-------------------Ternary operator in python------------------")
num = 15
res = "Even" if num % 2 == 0 else "Odd"
print(res)

#wap to find largest of 3 numbers
a = 20
b = 15
c = 25
greatest = a if a > b and  a > c else b if b > c else c
print(greatest)

#wap to find num is positive or negative
num = -5
result = "Positive" if num > 0 else "Negative"
print(result) 