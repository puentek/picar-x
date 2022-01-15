import sys
sys.path.insert(1,'/home/pi/picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
    px.set_dir_servo_angle(0)
    px.forward(25)
    time.sleep(1)
    px.stop()
    
#     time.sleep(1)
#     px.self.set_motor_speed(1, 1)
#     px.self.set_motor_speed(2, 1)
#     px.camera_servo_pin.angle(0)
# set_camera_servo2_angle(cam_cal_value_2)
# set_dir_servo_angle(dir_cal_value)

# if __name__ == "__main__":
#     try:
#         # dir_servo_angle_calibration(0) 
#         while 1:
#             test()
#     finally: 
#         stop()

