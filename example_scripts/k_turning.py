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
    px.set_dir_servo_angle(-30)
    time.sleep(2)
    px.stop()

    px.forward(50)
    time.sleep(.70)
    px.stop()
    time.sleep(.1)
    