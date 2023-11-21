import threading 
from time import sleep
class PaddleThread(threading.Thread): 
    def __init__(self, thread_name, thread_ID): 
        threading.Thread.__init__(self) 
        self.thread_name = thread_name 
        self.thread_ID = thread_ID 
        self.direction = 1
        self.time = 0
 
        # helper function to execute the threads
    def run(self): 
        while True:
            sleep(0.001)
            if self.time > 500:
                self.direction *= -1
                self.time = 0 
    def get_direction(self):
        self.time += 1
        return self.direction