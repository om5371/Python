#Lab Work 1.3
#Q1

user_input = input("Enter value: ")

int_value = int(user_input)
float_value = float(user_input)
bool_value = bool(user_input)

print(int_value,type(int_value))
print(float_value,type(float_value))
print(bool_value,type(bool_value))
print(str(user_input),type(str(user_input)))


#Q2

float_num = float(input(" Enter the value: "))
int_num = int(float_num)

print("Original float num",float_num)
print("Converted float num",int_num)


#Q3

bool_input = input("Enter True or False: ")

bool_value = bool_input.lower() == "true"

int_value = int(bool_value)
str_value = str(bool_value)

print("Boolean value:", bool_value)
print("Integer value:", int_value)
print("String value:", str_value)



#Q4

a = "Hello"
b = 45
c = 3.14
d = True
e = [3,2,1]
f = (12,14,17)
g = {"Hello",468,"friends",5}

print(type(a), id(a))
print(type(b), id(b))
print(type(c), id(c))
print(type(d), id(d))
print(type(e), id(e))
print(type(f), id(f))
print(type(g), id(g))


#Q5

a = 30
b = 30

print(id(a))
print(id(b))

b = 50

print("After cheking B")
print(id(a))
print(id(b))


