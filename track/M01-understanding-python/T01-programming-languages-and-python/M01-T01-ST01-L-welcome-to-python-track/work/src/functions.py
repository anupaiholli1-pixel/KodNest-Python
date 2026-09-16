#no arguments + no return value
def add():
    a,b = 10,10
    c = a + b
    print(c)
add()

#wap to write square of num
def multiply():
    a,b = 2,2
    c = a ** b
    print(c)
multiply()

#no arguments + return value
def add1():
    a,b = 10,20
    c = a + b
    return c
print(add1())

#arguments + no return value
def add2(a,b):
    c = a + b
    print(c)
print(add2(10,20)) 

#arguments + return value
def add3(a,b):
    c = a + b
    return c
print(add3(100,200)) 


#return type
def cal(a,b):
    return a + b, a - b

sum, diff = cal(10,20)
print("sum:", sum) 
print("diff:", diff)
