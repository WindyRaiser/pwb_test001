
name = input("What is Your Name : ")
print("Welcome to CS101 course" + name)

raw_n = input("Enter your age, so I will print out your age as star number : ")
number = int(raw_n)

print(type(number))

for i in range(number):
    print("*"*(i+1))
  
