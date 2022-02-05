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
import rossros as rs
from rossros import Bus, Consumer, ConsumerProducer, Producer, Timer
from ultrasonic import Ultrasonic
from ultra_control import UltraControl
from ultra_interp import UltraInterp
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__": 
    sense_bus = Bus()
    sense_interp = Bus()
    default_termination_bus = Bus(False)
    car = Picarx()
    sense = Sensor()
    interp = Interpreter(sense.sensitivity, sense.polarity)
    car_control = Controller(car, 15.0)



    ultra_bus_in = Bus()
    ultra_interp_bus_ot= Bus()

    ultra_sense = Ultrasonic()
    ultra_interp = UltraInterp()
    ultra_control = UltraControl(car)

    consumer_producer = ConsumerProducer(interp.output,
                        input_busses= Sensor(),
                        output_busses= sense_interp,
                        delay=0,
                        termination_busses=default_termination_bus,
                        name="Unnamed consumer_producer")
    producer =  Producer(sense.sensor_reading,
                output_busses = sense_interp,
                delay=0,
                termination_busses=default_termination_bus,
                name="Unnamed producer")
    consumer =  Consumer(controller.control,
                input_busses= Sensor(),
                delay=0,
                termination_busses=default_termination_bus,
                name="Unnamed consumer")
    
    timer = Timer(timer_busses = default_termination_bus,  # busses that should be set to true when timer triggers
                 duration=5,  # how many seconds the timer should run for (0 is forever)
                 delay=0,  # how many seconds to sleep for between checking time
                 termination_busses=default_termination_bus,
                 name="Unnamed termination timer")



    consumer_producer_ultrasonic = ConsumerProducer(ultra_interp.output, 
                                        input_busses=ultra_bus_in, 
                                        output_busses=ultra_interp_bus_ot,
                                        delay=1.0,
                                        termination_busses=default_termination_bus,
                                        name="ultrasonic_interpret_sensor_cp")
    producer_ultrasonic = Producer(ultra_sense.read,
                 ultra_bus_in,
                 delay=1.0,
                 termination_busses=default_termination_bus,
                 name="ultrasonic_p")
    
    consumer_ultrasonic = Consumer(ultra_control.control,
                 ultra_interp_bus_ot,
                 delay=1.0,
                 termination_busses=default_termination_bus,
                 name="ultrasonic_control_c")

    timer_producer = Timer(default_termination_bus,  # busses that should be set to true when timer triggers
                 duration=10.0,  # how many seconds the timer should run for (0 is forever)
                 delay=0,  # how many seconds to sleep for between checking time
                 termination_busses=default_termination_bus,
                 name="timer_p")


    # producer_consumer_list = [producer, consumer_producer, consumer, producer_ultrasonic, consumer_producer_ultrasonic, consumer_ultrasonic, timer_producer]
    # producer_consumer_list = [producer, consumer_producer, consumer, timer_producer]
    producer_consumer_list = [producer_ultrasonic, consumer_producer_ultrasonic, consumer_ultrasonic, timer_producer]


    rs.runConcurrently(producer_consumer_list)

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





