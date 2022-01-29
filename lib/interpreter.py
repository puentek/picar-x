from cmath import log

import time
from adc import ADC
from sensor import Sensor
import logging 
logging.basicConfig(level=logging.DEBUG)

class Interpreter(object): 
    def __init__(self, sensitivity, polarity):
        self.sensitivity = sensitivity
        self.polarity = polarity 
        

    def processor(self,sense_val):
        # center for p= 0
        logging.debug(f"sensor vals: {sense_val}, sensitivity: {self.sensitivity}, polarity: {self.polarity}")
        c = abs(sense_val[1]-sense_val[0]) > self.sensitivity
        c_1 = abs(sense_val[1]-sense_val[2]) > self.sensitivity

        # center for p= 1
        c_p = abs(sense_val[1]-sense_val[0]) < self.sensitivity
        c_p1 = abs(sense_val[1]-sense_val[2]) < self.sensitivity

        #left for p = 0
        l = abs(sense_val[1]-sense_val[0]) > self.sensitivity
        l_1 = abs(sense_val[1]-sense_val[2]) < self.sensitivity
        l_2 = abs(sense_val[1]) > abs(sense_val[0])

         #left for p = 1
        l_p = abs(sense_val[1]-sense_val[0]) > self.sensitivity
        l_p1 = abs(sense_val[1]-sense_val[2]) < self.sensitivity
        l_p2 = abs(sense_val[1]) < abs(sense_val[0])

        # left left for p = 0
        ll = abs(sense_val[1]-sense_val[0]) < self.sensitivity
        ll_1 = abs(sense_val[1]-sense_val[2]) > self.sensitivity
        ll_2 = abs(sense_val[2]) > abs(sense_val[1])

        # left left for p = 1
        llp = abs(sense_val[1]-sense_val[0]) < self.sensitivity
        ll_p1 = abs(sense_val[1]-sense_val[2]) > self.sensitivity
        ll_p2 = abs(sense_val[2]) < abs(sense_val[1])


        # right for p = 0
        r = abs(sense_val[1]-sense_val[0]) < self.sensitivity
        r_1 = abs(sense_val[1]-sense_val[2]) > self.sensitivity
        r_2 = abs(sense_val[1]) > abs(sense_val[2])

         # right for p = 1
        rp = abs(sense_val[1]-sense_val[0]) < self.sensitivity
        r_p1 = abs(sense_val[1]-sense_val[2]) > self.sensitivity
        r_p2 = abs(sense_val[1]) < abs(sense_val[2])


        # right right for p = 0
        rr = abs(sense_val[1]-sense_val[0]) > self.sensitivity
        rr_1 = abs(sense_val[1]-sense_val[2])< self.sensitivity
        rr_2 = abs(sense_val[1]) < abs(sense_val[0])

        # right right for p = 1
        rrp = abs(sense_val[1]-sense_val[0]) > self.sensitivity
        rr_p1 = abs(sense_val[1]-sense_val[2])< self.sensitivity
        rr_p2 = abs(sense_val[1]) > abs(sense_val[0])



        if self.polarity == 0: 
          # center condition 
            if c and c_1:
                return 'c'
                # logging.debug(f"c:  {self.sensitivity} ")
        
            elif l and l_1 and l_2:
                return 'l'
            elif ll and ll_1 and ll_2:
                return 'll'
            elif r and r_1 and r_2:
                return 'r'  
            elif rr and rr_1 and rr_2:
                return 'rr' 
            else:
                logging.debug(f"sensitivity not detectable: {self.sensitivity}")
                return 'c'
            
        elif self.polarity == 1:
            if c_p and c_p1:
                return 'c'
                # logging.debug(f"c:  {self.sensitivity} ")
            elif l_p and l_p1 and l_p2:
                return 'l' 
            elif llp and ll_p1 and ll_p2:
                return 'll'
            elif rp and r_p1 and r_p2:
                return 'r'
            elif rrp and rr_p1 and rr_p2:
                return 'rr'  
            else:
                logging.debug(f"sensitivity not detectable: {self.sensitivity}")
                return 'c'
            

            
    def output(self, sensor_vals):
        posi = self.processor(sensor_vals)
        logging.debug(f"processor out (posi:): {posi}")
        if posi =='c':
            return 0
        elif posi == 'l':
            return -0.33
            
        elif posi == 'll':
            return -0.66
        
        elif posi == 'r':
                return 0.33
        
        elif posi == 'rr':
                return 0.66
       
       
        else: 
            (f"sensitivity not detectable from output: {self.sensitivity}")


    def interp_sense (self,sensor_bus, interp_bus, time_delay=0.15):
        while True:
            sensor_vals = sensor_bus.read()
            interp_bus.write(self.output(sensor_vals))
            time.sleep(time_delay)



# if __name__ == "__main__":

    
    
#     sensor = Sensor()
#     sensitivity, polarity = sensor.calibrate()
#     interp = Interpreter(sensitivity,polarity)
#     sense_val= sensor.sensor_reading()
#     offset = interp.output(sense_val)
    

#     # logging.debug(f"Sensitivity and polarity :{IN}")