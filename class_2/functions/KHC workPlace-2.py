from cs1robots import *

load_world("../worlds/harvest2.wld")

def turn_right():
    for i in range(3):
        khc.turn_left()
        
# approch to beeper of robot
def move_to_beep(khc):
    for i in range(5):
        khc.move()
    khc.turn_left()
    khc.move()

def khc_stair(khc,n):
    for i in range(n):
        khc.pick_beeper()
        khc.move()
        turn_right()
        khc.move()
        khc.turn_left()    

def diamond(khc,n):
    for i in range(4):      # Diamond이니 4번 돌아야쥐 
        khc_stair(khc,n)
        khc.turn_left()    #여기서 한번 왼쪽으로 돌아줘 

# this khc_harvest(khc) part are main logic part        
def khc_harvest(khc):
    for i in range(3):
        n = 5 - 2*i
        diamond(khc,n)
        khc.move()
        khc.move()

##hubo=Robot()
khc=Robot()

khc.set_trace("blue")
khc.set_pause(0.7)

move_to_beep(khc)
khc_harvest(khc)



