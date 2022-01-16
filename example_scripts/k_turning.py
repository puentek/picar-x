import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 


if __name__ == "__main__":
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


