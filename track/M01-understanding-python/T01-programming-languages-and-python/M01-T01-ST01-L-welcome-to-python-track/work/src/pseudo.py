print("Hello world \nThank you for learning python")
print("Hello world", end= " \t ")
print("Thank you for learning python")

n = int(input("enter a number:"))
if (n > 0):
    print("positive number")
elif(n < 0):
    print("negative number")
else:
    print("zero") 
 
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
if (a >= b and a >= c):
    print("largest number is", a)
elif (b >= a and b >= c):
    print("largest number is", b)
else:
    print("largest number is", c) 
 
