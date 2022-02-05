import logging

class UltraControl(object):
    def __init__(self, car, speed=10):
        try:
            self.car = car
            self.speed = speed
        # self.car.set_dir_servo_angle(int(-offset*turn_angle))
        except:
            logging.info("help !! not on the pi ")
            self.car = car
            self.speed = speed

    def control (self, status):
        
        try:
            if status==0:
                self.car.stop()
            else:
                self.car.forward(self.speed)
        except:
            logging.info(f"not on the pi: {status}")