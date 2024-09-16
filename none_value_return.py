from cs1robots import *
##load_world("../worlds/harvest2.wld")

load_world("D:\\0.수첩\\Study\\Python\\4.매개 변수와 반환값을 가진 함수\\예제4-2\\worlds\\harvest2.wld")

hubo=Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()

s = turn_right()
print("the s is ",s)
