from cs1robots import *

load_world("../worlds/harvest2.wld")

def turn_right(robot):
   for i in range(3):
      robot.turn_left()
  
def go_to_beepers_first_pick(robot):
    for i in range(5):
      robot.move()
    robot.turn_left()
    robot.move()

def pick_and_stair(robot,n):    # 줍고 대각선 위치로 이동후 다시 주을 자세취함
    for i in range(n):
      robot.pick_beeper()
      robot.move()
      turn_right(robot)
      robot.move()
      robot.turn_left()

def diamond_harvest(robot,k):
    for i in range(4): #여기에서 i는 다이아몬드 4각 한 모서리의 beeper를 줍는 행위의 수
      pick_and_stair(robot,k)
      robot.turn_left()
    robot.move()
    robot.move()

def harvest_all(robot):
      for i in range(3):
        m = 5 - 2*i
        diamond_harvest(robot,m)

def dance_robot(robot):
   for i in range(102):
      robot.turn_left()

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.05)

go_to_beepers_first_pick(hubo)
harvest_all(hubo)
dance_robot(hubo)


          