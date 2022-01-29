

# from sklearn.cluster import k_means
from adc import ADC
from sensor import Sensor
from interpreter import Interpreter
from picarx_improved import Picarx
import time 
import logging 
logging.basicConfig(level=logging.DEBUG)

class Controller(object): 
    '''
        The __init__ method should take in an argument (with a default value) for the scaling factor
        between the interpreted offset from the line and the angle by which to steer.
        '''  
    def __init__(self,car):
        #set self. cr ob
        self.car = car 
        # self.car.set_dir_servo_angle(int(-offset*turn_angle))
        
    
    def control(self, offset, steer_angle):
        steer_angle = int(-offset*steer_angle)    
        self.car.set_dir_servo_angle(steer_angle) 
        logging.debug(f"current stearing angle at : {steer_angle}") 
        return steer_angle
        '''
        The main control method should call the steering-servo method from your car class so that
        it turns the car toward the line. It should also return the commanded steering angle.'''
    

    def control_move(self, interp_bus, steer_angle, time_delay = 0.15):
        while True: 
            offset = interp_bus.read()
            self.control(offset, steer_angle)
            # self.car.forward(20)
            time.sleep(time_delay)
            logging.debug(f"control_move = {offset}")

# if __name__ == "__main__":
#     import time

#     sensor = Sensor()
#     sensitivity, polarity = sensor.calibrate()
#     interp = Interpreter(sensitivity,polarity)
#     car = Picarx()
#     robot_pos = interp.output(sensor.sensor_reading())
#     logging.debug(f"robot pos: {robot_pos}")
#     controller = Controller(car,robot_pos,30)

#     while(1):
#        sensor_vals = sensor.sensor_reading()
#        robot_pos = interp.output(sensor_vals)
#        controller.control(robot_pos, 20)
#        car.forward(15)

#     car.stop()
