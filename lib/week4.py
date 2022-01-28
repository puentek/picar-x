import random
from adc import ADC
import time 
import logging
from threading import Thread
import concurrent.futures
from picarx_improved import Picarx
from readerwriterlock import rwlock
from nbformat import read
logging.basicConfig(level=logging.DEBUG)


class Bus (object ):
    
    def __init__(self,message):
        self.message = message 
        self.lock = rwlock.RWLockWriteD()
    
    #Producer 
    def read(self):
        with self.lock.gen_rlock():
            return self.message

    def write(self, message):
        with self.lock.gen_wlock():
                self.message = message

# Producer function 
class Sensor(object):
    def __init__(self,bus, delay = 0.15):
        self.chn_0 = ADC("A0")
        self.chn_1 = ADC("A1")
        self.chn_2 = ADC("A2")
        self.bus = bus
        self.delay = delay

    def sensor_reading(self):
        adc_value_list = []
        adc_value_list.append(self.chn_0.read())
        adc_value_list.append(self.chn_1.read())
        adc_value_list.append(self.chn_2.read())
        
        
        
        self.bus.write(adc_value_list)
        time.sleep(self.delay)
        # return adc_value_list
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

