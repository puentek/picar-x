

from random import random

import time

from adc import ADC
import logging 
import random 
logging.basicConfig(level=logging.DEBUG)

class Sensor(object):
    def __init__(self):
        self.chn_0 = ADC("A0")
        self.chn_1 = ADC("A1")
        self.chn_2 = ADC("A2")
        
        self.sensitivity, self.polarity = self.calibrate()
        
    def sensor_reading(self):
        adc_value_list = []
        adc_value_list.append(self.chn_0.read())
        adc_value_list.append(self.chn_1.read())
        adc_value_list.append(self.chn_2.read())
        return adc_value_list

    def calibrate(self):
        sensitivity = -1
        polarity = -1
        # if abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_0.read()-self.chn_1.read()) and abs(self.chn_0.read() - self.chn_2.read()) < abs(self.chn_1.read()-self.chn_2.read()):
        x = min(abs(self.chn_0.read()-self.chn_1.read()), abs(self.chn_1.read() - self.chn_2.read()))/2
        sensitivity = abs(self.chn_0.read() - self.chn_2.read()) + x
         

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
        logging.debug("got sensitivity from: {}")
        return sensitivity, polarity
    
    def sense_produce (self,sense_bus,time_delay=0.15):
        while True:
            reading = self.sensor_reading()
            sense_bus.write(reading)
            time.sleep(time_delay)
            logging.debug(f"sense_produce= {reading}")



# if __name__ == "__main__":
#     import time
#     SN = Sensor()
    
#     # while True:
#     #     print(SN.sensor_reading())
#     #     time.sleep(1)

#     logging.debug(f"Sensor reading:{SN,SN.sensor_reading()}")
#     logging.debug(f"Sensitivity and polarity :{SN,SN.calibrate()}")
    