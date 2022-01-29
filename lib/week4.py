from readerwriterlock import rwlock


class Bus(object):
    
    def __init__(self):
        self.message = None
        self.lock = rwlock.RWLockWriteD()
    
    
    def read(self):
        with self.lock.gen_rlock():
            return self.message

    def write(self, message):
        with self.lock.gen_wlock():
                self.message = message
    



