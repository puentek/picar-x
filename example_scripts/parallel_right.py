import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
    # move car forward (a)
    
    px.forward(50)
    time.sleep(.5)
    px.stop()
    time.sleep(.1)
    px.set_dir_servo_angle(30)
    time.sleep(2)
    px.forward(50)
    time.sleep(.5)
    px.stop()

    
