
from cs1robots import *
##load_world("../worlds/harvest2.wld")

load_world("D:\\0.수첩\\Study\\Python\\4.매개 변수와 반환값을 가진 함수\\예제4-2\\worlds\\harvest2.wld")


def turn_right(robot):
    for i in range(3):
        robot.turn_left()


def goto_stair(robot):
    for i in range(5):
        hubo.move()
    hubo.turn_left()
    hubo.move()

def stair(robot,n):
    for i in range(n):
        robot.pick_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()

def diamond(robot,n):
    for i in range(4):
        stair(robot,n)
        robot.turn_left()

def harvest_all(robot):
    for i in range(3):
        n = 5-2*i
        diamond(robot,n)
        hubo.move()
        hubo.move()

hubo=Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)



goto_stair(hubo)
harvest_all(hubo)


