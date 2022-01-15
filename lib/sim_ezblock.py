import time 
from filedb import fileDB


class Servo(object):
    MAX_PW = 2500
    MIN_PW = 500
    _freq = 50
    def __init__(self, pwm):
        super().__init__()

    def map(self, x, in_min, in_max, out_min, out_max):
        return 1
        
    # angle ranges -90 to 90 degrees
    def angle(self, angle):
        pass

class Pin(object):
    # OUT = GPIO.OUT
    # IN = GPIO.IN
    # IRQ_FALLING = GPIO.FALLING
    # IRQ_RISING = GPIO.RISING
    # IRQ_RISING_FALLING = GPIO.BOTH
    # PULL_UP = GPIO.PUD_UP
    # PULL_DOWN = GPIO.PUD_DOWN
    PULL_NONE = None

    _dict = {
        "BOARD_TYPE": 12,
    }

    _dict_1 = {
        "D0":  17,
        "D1":  18,
        "D2":  27,
        "D3":  22,
        "D4":  23,
        "D5":  24,
        "D6":  25,
        "D7":  4,
        "D8":  5,
        "D9":  6,
        "D10": 12,
        "D11": 13,
        "D12": 19,
        "D13": 16,
        "D14": 26,
        "D15": 20,
        "D16": 21,
        "SW":  19,
        "LED": 26,
        "BOARD_TYPE": 12,
        "RST": 16,
        "BLEINT": 13,
        "BLERST": 20,
        "MCURST": 21,
    }

    _dict_2 = {
        "D0":  17,
        "D1":   4, # Changed
        "D2":  27,
        "D3":  22,
        "D4":  23,
        "D5":  24,
        "D6":  25, # Removed
        "D7":   4, # Removed
        "D8":   5, # Removed
        "D9":   6,
        "D10": 12,
        "D11": 13,
        "D12": 19,
        "D13": 16,
        "D14": 26,
        "D15": 20,
        "D16": 21,
        "SW":  25, # Changed
        "LED": 26,
        "BOARD_TYPE": 12,
        "RST": 16,
        "BLEINT": 13,
        "BLERST": 20,
        "MCURST":  5, # Changed
    }

    def __init__(self, *value):
        super().__init__()
        
    def check_board_type(self):
        pass
    def init(self, mode, pull=PULL_NONE):
        self._pull = pull
        self._mode = mode
        if mode != None:
            pass

    def dict(self, *_dict):
        if len(_dict) == 0:
            return 1
        else:
            pass

    def __call__(self, value):
        return 1

    def value(self, *value):
        if len(value) == 0:
            # self._debug("read pin %s: %s" % (self._pin, result))
            return 1
        else:
            pass

    def on(self):
        return 1

    def off(self):
        return 0

    def high(self):
        return 1

    def low(self):
        return 0

    def mode(self, *value):
        if len(value) == 0:
            return 1
        else:
            pass

    def pull(self, *value):
        return 1

    def irq(self, handler=None, trigger=None, bouncetime=200):
        pass

    def name(self):
        return 1

    def names(self):
        return 1

    class cpu(object):
        GPIO17 = 17
        GPIO18 = 18
        GPIO27 = 27
        GPIO22 = 22
        GPIO23 = 23
        GPIO24 = 24
        GPIO25 = 25
        GPIO26 = 26
        GPIO4  = 4
        GPIO5  = 5
        GPIO6  = 6
        GPIO12 = 12
        GPIO13 = 13
        GPIO19 = 19
        GPIO16 = 16
        GPIO26 = 26
        GPIO20 = 20
        GPIO21 = 21

        def __init__(self):
            pass

from i2c import I2C
class ADC(I2C):
    ADDR=0x14                   # 扩展板的地址为0x14

    def __init__(self, chn):    # 参数，通道数，树莓派扩展板上有8个adc通道分别为"A0, A1, A2, A3, A4, A5, A6, A7"
        super().__init__()
        pass
        
    def read(self):                     # adc通道读取数---写一次数据，读取两次数据 （读取的数据范围是0~4095）
        return 1

    def read_voltage(self):                             # 将读取的数据转化为电压值（0~3.3V）
        return 1
        
class I2C(object):
    MASTER = 0
    SLAVE  = 1
    RETRY = 5

    def __init__(self, *args, **kargs):     # *args表示位置参数（形式参数），可无，； **kargs表示默认值参数，可无。
        super().__init__()
        

    def _i2c_write_byte(self, addr, data):   # i2C 写系列函数
        # self._debug("_i2c_write_byte: [0x{:02X}] [0x{:02X}]".format(addr, data))
        return 1
    
    def _i2c_write_byte_data(self, addr, reg, data):
        # self._debug("_i2c_write_byte_data: [0x{:02X}] [0x{:02X}] [0x{:02X}]".format(addr, reg, data))
        return 1
    
    def _i2c_write_word_data(self, addr, reg, data):
        # self._debug("_i2c_write_word_data: [0x{:02X}] [0x{:02X}] [0x{:04X}]".format(addr, reg, data))
        return 1
    
    def _i2c_write_i2c_block_data(self, addr, reg, data):
        # self._debug("_i2c_write_i2c_block_data: [0x{:02X}] [0x{:02X}] {}".format(addr, reg, data))
        return 1
    
    def _i2c_read_byte(self, addr):   # i2C 读系列函数
        # self._debug("_i2c_read_byte: [0x{:02X}]".format(addr))
        return 1
    def _i2c_read_i2c_block_data(self, addr, reg, num):
        # self._debug("_i2c_read_i2c_block_data: [0x{:02X}] [0x{:02X}] [{}]".format(addr, reg, num))
        return 1

    def is_ready(self, addr):
        addresses = self.scan()
        if addr in addresses:
            return True
        else:
            return False

    def scan(self):                             # 查看有哪些i2c设备
        return 1

    def send(self, send, addr, timeout=0):                      # 发送数据，addr为从机地址，send为数据
        pass

    def recv(self, recv, addr=0x00, timeout=0):     # 接收数据
        if isinstance(recv, int):                   # 将recv转化为二进制数
            result = 1
        elif isinstance(recv, bytearray):
            result = 1
        else:
            return 0
        for i in range(len(result)):
            result[i] = 1
        return result

    def mem_write(self, data, addr, memaddr, timeout=5000, addr_size=8): #memaddr match to chn
        pass
    
    def mem_read(self, data, addr, memaddr, timeout=5000, addr_size=8):     # 读取数据
        if isinstance(data, int):
            pass
        elif isinstance(data, bytearray):
            pass
        else:
            return 0
        return 0
    
    def readfrom_mem_into(self, addr, memaddr, buf):
        return 1
    
    def writeto_mem(self, addr, memaddr, data):
        pass

# i2c = I2C()
# i2c.scan()
# i2c.mem_write(0xff53773, 20, 20)

class PWM(I2C):
    REG_CHN = 0x20
    REG_FRE = 0x30
    REG_PSC = 0x40
    REG_ARR = 0x44

    ADDR = 0x14

    CLOCK = 72000000

    def __init__(self, channel, debug="critical"):
        super().__init__()
        

    def i2c_write(self, reg, value):
        pass

    def freq(self, *freq):
        if len(freq) == 0:
            return 1
        else:
            pass

    def prescaler(self, *prescaler):
        pass

    def period(self, *arr):
        pass

    def pulse_width(self, *pulse_width):
        if len(pulse_width) == 0:
            return 1
        else:
            pass

    def pulse_width_percent(self, *pulse_width_percent):
        if len(pulse_width_percent) == 0:
            return 1
        else:
           pass

        
def test():
    pass
def test2():
    pass
        


