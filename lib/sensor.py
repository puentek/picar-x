

from random import random
from re import L
from adc import ADC
import logging 
logging.basicConfig(level=logging.DEBUG)

class Sensor(object):
    def __init__(self):
        self.chn_0 = ADC("A0")
        self.chn_1 = ADC("A1")
        self.chn_2 = ADC("A2")

    def sensor_reading(self):
        adc_value_list = []
        adc_value_list.append(self.chn_0.read())
        adc_value_list.append(self.chn_1.read())
        adc_value_list.append(self.chn_2.read())
        return adc_value_list
    def calibrate(self):
        
        if abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_0.read()-self.chn_1.read()) and abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_1.read()-self.chn_2.read()):
            x = random(abs(self.chn_0.read()-self.chn_2.read()), abs(self.chn_0.read()-self.chn_1.read()))
            sensitivity = abs(self.chn_0.read() - self.chn_2.read()) + x
            return sensitivity
        # elif abs(self.chn_0.read() - self.chn_2.read()) > abs(self.chn_1.read()-self.chn_2.read()):
        #     sensitivity = self.sensor_reading + 10
        #     return sensitivity
        else: 
             logging.error(f"Robot is too far to calibrate")

        if self.chn_0.read()-self.chn_1.read() < 0 and self.chn_1.read()-self.chn_2.read() < 0:
            if self.chn_0.read()-self.chn_1.read() < 0:
                polarity = 0
                return polarity   
            else: 
                polarity = 1
                return polarity
        else: 
            logging.error(f"Robot cannot be calibrated")
            polarity = -1
            return polarity



if __name__ == "__main__":
    import time
    SN = Sensor()
    
    # while True:
    #     print(SN.sensor_reading())
    #     time.sleep(1)

    logging.debug(f"Sensor reading:{SN,SN.sensor_reading()}")
    logging.debug(f"Sensitivity and polarity :{SN,SN.calibrate()}")
    # logging.debug(f"debug")
    logging.info(f"info")
    logging.error(f"error")