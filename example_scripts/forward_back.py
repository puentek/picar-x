import sys
sys.path.insert(1,'../../picar-x/lib')
from picarx_improved import Picarx
import time 

if __name__ == "__main__":
    px = Picarx()
  
    px.forward(30)
    time.sleep(1)
    px.backward(30)
    time.sleep(1)
    px.stop()
    
