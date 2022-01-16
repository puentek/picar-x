import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
    # move car forward (a)
    
    px.backward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)

    px.set_dir_servo_angle(-30)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.5)
    px.stop()
    time.sleep(.5)

    px.forward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(-25)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(-25)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.25)
    px.stop()

    px.set_dir_servo_angle(0)
    time.sleep(2)
    px.stop()

    px.backward(50)
    time.sleep(.25)
    px.stop()
    time.sleep(.1)
