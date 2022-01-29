import random
from adc import ADC
import time 
import logging
from threading import Thread
import concurrent.futures
from picarx_improved import Picarx
from controller import Controller
from sensor import Sensor
from interpreter import Interpreter
from week4 import Bus
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__": 
    sense_bus = Bus()
    sense_interp = Bus()
    car = Picarx()
    sense = Sensor()
    interp = Interpreter(sense.sensitivity, sense.polarity)
    control = Controller(car)

while True: 
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: 
        logging.debug("lets get ready to sense aka producer!!!")   
        eSensor = executor.submit(sense.sense_produce,sense_bus)

        logging.debug("starting the interpreter aka preducer-consumer!!!")
        eInterpreter = executor.submit(interp.interp_sense,sense_interp)

        logging.debug("starting the controller aka consumer!!!")
        eController= executor.submit(control.control_move, sense_interp, steer_angle= 20)

    eSensor.result()
    eInterpreter.result()
    eController.result()





