import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
    # move car forward (a)
    px.set_dir_servo_angle(0)
    px.forward(20)
    time.sleep(3)
    px.set_dir_servo_angle(30)
    time.sleep(3)
    px.backward(20)
    time.sleep(3)

    px.stop()
