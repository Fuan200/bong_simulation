import pygame
import random
from screen_percentage import get_width, get_height
from colors import get_rgb

screen_width = 0
screen_height = 0
ball_radius = 20
ball_speed = 10

#serving_angle = random.uniform(10, 10)

ball_x = 0
ball_y = 0

ball_speed_x = random.choice([-1, 1])
ball_speed_y = 1

paddle_width = 0
paddle_height = 20
paddle_x = 0

def main():
    pygame.init()

    global screen_width, screen_height, ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_width, paddle_x
    screen_width, screen_height = get_width(), get_height()
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball_x = random.randint(ball_radius, screen_width - ball_radius)

    paddle_width = screen_width // 12
    paddle_x = (screen_width - paddle_width) // 2

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= 2
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += 2

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
            ball_speed_x *= -1

        if ball_y <= ball_radius:
            ball_speed_y = abs(ball_speed_y) 

        if (
            screen_height - paddle_height - ball_radius <= ball_y <= screen_height - ball_radius
            and paddle_x <= ball_x <= paddle_x + paddle_width
        ):
            ball_speed_y *= -1

        if ball_y >= screen_height - ball_radius:
            ball_x = random.randint(ball_radius, screen_width - ball_radius)
            ball_y = 0
            #serving_angle = random.uniform(10, 10)
            ball_speed_x = random.choice([-1, 1])
            ball_speed_y = 1

        screen.fill(get_rgb('black'))

        pygame.draw.circle(screen, get_rgb('magenta'), (int(ball_x), int(ball_y)), ball_radius)

        pygame.draw.rect(screen, get_rgb('white'), (paddle_x, screen_height - paddle_height, paddle_width, paddle_height))

        pygame.display.flip()
    
    pygame.quit()