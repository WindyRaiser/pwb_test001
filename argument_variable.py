import math

def print_twice(text):    # 여기서 text는 함수의 매개변수(parameter)
    print(text)
    print(text)

print_twice("hello this Python world")    # 여기서 "hello this Python world" 는 함수의 인자(argument)

print_twice(math.pi)

def student():
    name1 = " Samuel Adams "
    age1 = 41
    return name1,age1

name , age = student()
print(name,age)

def f():
    x=10
    y=20
    return x,y

print(f())

name = input("what is your name: ")
print("Welcome CS101 course, ",name)

raw_n = input("what is your number")
number = int(raw_n)

for i in range(number):
    print("*"*i)



