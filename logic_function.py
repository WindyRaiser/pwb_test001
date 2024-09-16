#is integer a divisible by b?

# def is_divisible(a,b):
#     if a%b == 0:
#         return True
#     else:
#         return False

def is_divisible(a,b):
    # # return a%b == 0
    result = bool( a%b == 0) 
    print(" the bool result is ",result)
    return bool(a%b == 0)



# if is_visible(x,y):
#     print('x is divisible by y')

int_first = int(input("what is your first number : "))
int_second = int(input("what is your second number : "))

if is_divisible(int_first,int_second) == True:
    # print(str(int_first)," divid " , str(int_second) , " is " , is_divisible(int_first,int_second))
    print(str(int_first)," divid " , str(int_second) , " is dividable" )
else:
    print(str(int_first)," divid " , str(int_second) , " is none dividable" )


