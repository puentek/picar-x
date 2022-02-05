import logging 

class UltraInterp:
    def __init__(self) -> None:
        pass

    def output (self, sensor_val):
        if sensor_val < 130:
            return 0
        else:
            return 1
            