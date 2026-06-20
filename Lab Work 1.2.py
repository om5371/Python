#Lab Work 1.2
#Q1

#Normal
print("apple","banana","kivi","mango")

#Using sep
print("apple","banana","kivi","mango",sep = " ** ")

#Normal
print("apple","banana","kivi","mango")

#Using end
print("apple","banana","kivi",end = "  ** ""mango")

#Q2

name =input(" Enter name ")
age = input("Enter age ")
fh = input("Enter Favorite Hobbey ")

print("Helo",(name),"At",(age),"Enjoying",(fh),"sounds fun!")


#Q3
a = int(input("Enter number One "))
b = int(input("Enter number Two "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)



#Q4
a = "Hello"
b = 45
c = 4.5
d = True
e = 5j

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))




#Q5

H = int(input("Enter height "))
W = int(input("Enter Weight "))

print("your height is",(H),"cm")
print("your Weight is",(W),"kg")




#Q6

a = input("Enter boolean value (True/False) : ") == "True"

b = input("Enter boolean value (True/False) : ") == "True"

print("AND:",a and b)
print("OR:",a or b)
print("NOT:",not b)





#Q7

x = 10
print("initial value: ",x)

x += 5
print("After += 5: ",x)

x -= 3
print("After -= 3: ",x)

x *= 2
print("After *= 2: ",x)

x /= 10
print("After /= 4: ",x)