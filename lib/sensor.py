

from random import random
from re import L
from adc import ADC
import logging 
import random 
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
        sensitivity = -1
        polarity = -1
        if abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_0.read()-self.chn_1.read()) and abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_1.read()-self.chn_2.read()):
            x = (self.chn_0.read() - self.chn_2.read()) + min((self.chn_0.read()-self.chn_1.read()), self.chn_0.read() - self.chn_2.read())/2
            sensitivity = abs(self.chn_0.read() - self.chn_2.read()) + x
            # return sensitivity
            logging.debug(f"sensitivity: {sensitivity}")
            # return sensitivity
        # elif abs(self.chn_0.read() - self.chn_2.read()) > abs(self.chn_1.read()-self.chn_2.read()):
        #     sensitivity = self.sensor_reading + 10
        #     return sensitivity
        else: 
             logging.error(f"Robot is too far to calibrate")

        if self.chn_0.read()-self.chn_1.read() < 0 and self.chn_2.read()-self.chn_1.read() < 0:
            polarity = 0
            # return polarity
            logging.debug(f"polarity: {polarity}")   
             
        elif self.chn_0.read()-self.chn_1.read() > 0 and self.chn_2.read()-self.chn_1.read() > 0: 
            polarity = 1
            # return polarity
            logging.debug(f"polarity: {polarity}")   
    

        else:
            # logging.error(f"Robot cannot be calibrated")
            polarity = -1
            # return polarity
            logging.debug(f"Robot cannot be calibrated; polarity: {polarity}")   
        
        return sensitivity, polarity



if __name__ == "__main__":
    import time
    SN = Sensor()
    
    # while True:
    #     print(SN.sensor_reading())
    #     time.sleep(1)

    logging.debug(f"Sensor reading:{SN,SN.sensor_reading()}")
    logging.debug(f"Sensitivity and polarity :{SN,SN.calibrate()}")
    # logging.debug(f"debug")
    # logging.info(f"info")
    # logging.error(f"error")