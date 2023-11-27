import pygame
import random
from screen_percentage import get_width, get_height
from colors import get_rgb
from position import get_position
from paddle import PaddleThread
from time import sleep
from modify_files import write_file, get_max

pygame.init()

lost_balls_count = 0
rallis_number = 0
font = pygame.font.SysFont(None, 36)

screen_width = 0
screen_height = 0
ball_radius = 20
ball_speed = 10

ball_x = 0
ball_y = 20

#lost_balls_count = 0
#rallis_number = 0
#font = pygame.font.SysFont(None, 36)


ball_speed_x = random.choice([-1, 1])
ball_speed_y = 1

paddle_width = 0
paddle_height = 20
paddle_x = 0

file_path = './record.txt'

def main(pThread):
    #pygame.init()

    global lost_balls_count, rallis_number, screen_width, screen_height, ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_width, paddle_x
    screen_width, screen_height = get_width(), get_height()
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball_x = random.randint(ball_radius, screen_width - ball_radius)

    paddle_width = screen_width // 12
    paddle_x = (screen_width - paddle_width) // 2

    running = True
    pThread.notifyCeilingTouch((ball_x,ball_y),(ball_speed_x,ball_speed_y),ball_radius,(screen_width,screen_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pThread.notifyQuit()

        sleep(0.0001)
        # Obtén la posición actual de la pelota
        ball_position = (ball_x, ball_y)
        rallis_large = get_max(file_path)

        # Actualiza la posición de la plataforma según la posición de la pelota
        #paddle_x = pThread.get_paddle_position(ball_position, paddle_width)
        paddle_x += pThread.get_direction()*((screen_height)/screen_width)
        pThread.notifyFrame((screen_width,screen_height))

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
            ball_speed_x *= -1

        if ball_y < ball_radius:
            ball_speed_y = -ball_speed_y
            ball_y = ball_radius
            #pThread.notifyCeilingTouch(ball_position,(ball_speed_x,ball_speed_y),ball_radius,(screen_width,screen_height))

        if (
            screen_height - paddle_height - ball_radius <= ball_y <= screen_height - ball_radius
            and paddle_x <= ball_x <= paddle_x + paddle_width
        ):
            ball_speed_y *= -1
            rallis_number += 1
            ball_y = screen_height - paddle_height - ball_radius
            pThread.notifyCeilingTouch(ball_position,(ball_speed_x,ball_speed_y),ball_radius,(screen_width,screen_height))
            
        if ball_y >= screen_height - ball_radius:
            lost_balls_count += 1

            write_file(file_path, str(rallis_number))
            rallis_number = 0

            ball_x = random.randint(ball_radius, screen_width - ball_radius)
            ball_y = ball_radius
            ball_speed_x = random.choice([-1, 1])
            ball_speed_y = 1
            pThread.notifyCeilingTouch((ball_x,ball_y),(ball_speed_x,ball_speed_y),ball_radius,(screen_width,screen_height))

        screen.fill(get_rgb('black'))

        text = font.render(f"Lost Balls: {lost_balls_count}", True, get_rgb('white'))
        screen.blit(text, (10, 10))

        text_rallis_number = font.render(f"Rallis number: {rallis_number}", True, get_rgb('white'))
        screen.blit(text_rallis_number, (10, 40))

        text_rallis_large = font.render(f"Rallis large: {rallis_large}", True, get_rgb('white'))
        screen.blit(text_rallis_large, (10, 70))

        ball = pygame.draw.circle(screen, get_rgb('magenta'), (int(ball_x), int(ball_y)), ball_radius)
        #print(get_position(ball))
        pygame.draw.rect(screen, get_rgb('red'), (pThread.target_position+(screen_width/2), screen_height - paddle_height, 10, paddle_height))

        pygame.draw.rect(screen, get_rgb('white'), (paddle_x, screen_height - paddle_height, paddle_width, paddle_height))

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()