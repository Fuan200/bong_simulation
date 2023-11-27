import threading 
from time import sleep

class PaddleThread(threading.Thread): 
    def __init__(self, thread_name, thread_ID): 
        threading.Thread.__init__(self) 
        self.thread_name = thread_name 
        self.thread_ID = thread_ID 
        self.direction = 0
        self.position = 0
        self.target_position = 0
        self.shouldRun = True
    
    def notifyQuit(self):
        self.shouldRun = False

    def notifyCeilingTouch(self, ball_position, ball_speed,ball_radius,screen_size):
        # Simulate floor travel path
        curr_ball_x, curr_ball_y = ball_position
        curr_ball_speed_x, curr_ball_speed_y = ball_speed
        screen_width, screen_height = screen_size

        while curr_ball_y <= screen_height:
            curr_ball_x += curr_ball_speed_x
            curr_ball_y += curr_ball_speed_y

            if curr_ball_y < ball_radius:
                curr_ball_speed_y = -curr_ball_speed_y
                curr_ball_y = ball_radius
            
            if curr_ball_x <= 10 <= ball_radius or curr_ball_x >= screen_width-10:
                curr_ball_speed_x *= -1
        self.target_position = curr_ball_x - screen_width//2
        print("Predicted position: "+str(self.target_position))

    def run(self): 
        while self.shouldRun:
            sleep(0.0001)
            if abs(self.target_position-self.position) < 5:
                self.direction = 0
            elif self.target_position > self.position:
                self.direction = 1
            else:
                self.direction = -1
            #print("Current position: "+str(self.position)+" Final position: "+str(self.target_position)+" Direction: "+str(self.direction))

    def notifyFrame(self,screen_size):
        screen_width, screen_height = screen_size
        self.position += self.direction*((screen_height)/screen_width)

    def get_direction(self):
        return self.direction
