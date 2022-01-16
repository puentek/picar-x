import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
    # move car forward (a)
    for angle in range(0,10):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
    # for angle in range(35,-35,-1):
    #     px.set_dir_servo_angle(angle)
    #     time.sleep(0.01)        
    # for angle in range(-35,0):
    #     px.set_dir_servo_angle(angle)
    #     time.sleep(0.01)
    px.forward(0)
    time.sleep(1)
    
