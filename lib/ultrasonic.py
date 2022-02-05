import time
import logging 
logging.basicConfig(level=logging.DEBUG)
from pin import Pin


class Ultrasonic():
    def __init__(self, trig, echo, timeout=0.02):
        
        self.trig = Pin("D2") 
        self.echo = Pin("D3")
        self.timeout = timeout

    def _read(self):
        self.trig.low()
        time.sleep(0.01)
        self.trig.high()
        time.sleep(0.00001)
        self.trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -1
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def read(self, times=10):
        for i in range(times):
            a = self._read()
            if a != -1 or a <= 300:
                return a
        return -1

# class USensor():
#     def __init__(self) -> None:
#         pass

#     def ultra_sense_produce (self,sense_bus,time_delay=0.15):
#         while True:
#             reading = self.sensor_reading()
#             sense_bus.write(reading)
#             time.sleep(time_delay)
#             logging.debug(f"sense_produce= {reading}")
