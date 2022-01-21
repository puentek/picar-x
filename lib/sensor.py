

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

if __name__ == "__main__":
    import time
    # SN = Sensor(950)
    # while True:
    #     print(SN.sensor_reading())
    #     time.sleep(1)

    logging.debug(f"Sensor reading:{SN,SN.sensor_reading()}")
    # logging.debug(f"debug")
    logging.info(f"info")
    logging.error(f"error")