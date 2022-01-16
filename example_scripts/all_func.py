import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 


def move_straight():
    px = Picarx()
  
    px.forward(30)
    time.sleep(1)
    px.backward(30)
    time.sleep(1)


def parallel_left():
    px = Picarx()
    # move car forward (a)
    
    px.forward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)

    px.set_dir_servo_angle(30)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.5)
    px.stop()
    time.sleep(.5)

    px.backward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(25)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(25)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(0)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)

def parallel_right():
    px = Picarx()
    # move car forward (a)
    
    px.forward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)

    px.set_dir_servo_angle(-30)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.75)
    px.stop()
    time.sleep(.1)

    px.set_dir_servo_angle(-35)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)

    px.set_dir_servo_angle(-25)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.55)
    px.stop()
    time.sleep(.1)

def k_turn():
    px = Picarx()
    
    px.forward(50)
    time.sleep(.50)
    px.stop()
    time.sleep(.1)

    #turn right
    px.set_dir_servo_angle(-45)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(1.5)
    px.stop()
    time.sleep(.1)

    # go back  
    px.set_dir_servo_angle(45)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(1.2)
    px.stop()
    time.sleep(.1)

    # turn and go forward
    px.set_dir_servo_angle(0)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(1)
    px.stop()
    time.sleep(.1)

if __name__ == "__main__":
    while(1):
        keyboard_num = int(input("1: move straight \n 2: parallel right \n 3: parallel left \n 4:k-turn  \n 5: exit enter number:"))
        print(keyboard_num)
        if keyboard_num == 1:
            move_straight()  
        elif keyboard_num == 2:
            parallel_right()
        elif keyboard_num == 3:
            parallel_left()
        
        elif keyboard_num == 4:
            k_turn()
            
        elif keyboard_num==5:
            break
        else:
            print("You have entered invalid number. ")


