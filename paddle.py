import threading 
from time import sleep

class PaddleThread(threading.Thread): 
    def __init__(self, thread_name, thread_ID): 
        threading.Thread.__init__(self) 
        self.thread_name = thread_name 
        self.thread_ID = thread_ID 
        self.direction = 1
        self.time = 0
 
    def run(self): 
        while True:
            sleep(0.001)
            if self.time > 500:
                self.direction *= -1
                self.time = 0 

        # Asegurarse de que la plataforma no se salga de los bordes izquierdo y derecho
            if self.direction == 1:
                self.thread_ID += 1
            else:
                self.thread_ID -= 1

            self.time += 1


    def get_direction(self):
        self.time += 1
        return self.direction

    def get_paddle_position(self, ball_position, paddle_width):
        paddle_center = paddle_width / 2
        ball_x, ball_y = ball_position

        if ball_y < self.thread_ID - paddle_center:
        # Mover la plataforma hacia la posición x de la pelota
            target_position = ball_x - paddle_center
        # Asegurarse de que la plataforma no se salga del borde izquierdo
            return max(0, min(target_position, self.thread_ID - paddle_width))
        else:
        # Colocar la plataforma en el centro horizontal de la pantalla, permitiendo un rango más amplio
            target_position = ball_x - paddle_center
        # Asegurarse de que la plataforma no se salga del borde derecho
            return max(0, min(target_position, self.thread_ID - paddle_width))


