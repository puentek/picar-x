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
from rossros import Bus, Consumer, ConsumerProducer, Producer, Timer
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__": 
    sense_bus = Bus()
    sense_interp = Bus()
    car = Picarx()
    sense = Sensor()
    interp = Interpreter(sense.sensitivity, sense.polarity)
    control = Controller(car)
    consumer_producer = ConsumerProducer(consumer_producer_function,
                        input_busses= Sensor(),
                        output_busses= sense_interp,
                        delay=0,
                        termination_busses=default_termination_bus,
                        name="Unnamed consumer_producer")
    producer =  Producer(producer_function,
                output_busses = sense_interp,
                delay=0,
                termination_busses=default_termination_bus,
                name="Unnamed producer")
    consumer =  Consumer(consumer_function,
                input_busses= Sensor(),
                delay=0,
                termination_busses=default_termination_bus,
                name="Unnamed consumer")
    
    timer = Timer(timer_busses,  # busses that should be set to true when timer triggers
                 duration=5,  # how many seconds the timer should run for (0 is forever)
                 delay=0,  # how many seconds to sleep for between checking time
                 termination_busses=default_termination_bus,
                 name="Unnamed termination timer")



# while True: 
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: 
#         logging.debug("lets get ready to sense aka producer!!!")   
#         eSensor = executor.submit(sense.sense_produce,sense_bus)

#         logging.debug("starting the interpreter aka producer-consumer!!!")
#         eInterpreter = executor.submit(interp.interp_sense, sense_bus, sense_interp)

#         logging.debug("starting the controller aka consumer!!!")
#         eController= executor.submit(control.control_move, sense_interp, steer_angle= 20)

#     eSensor.result()
#     eInterpreter.result()
#     eController.result()





