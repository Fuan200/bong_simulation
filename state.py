import pygame

def screen_percentage(percentage):
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h

    percentage /= 100
    format_width, format_height = int(percentage * screen_width), int(percentage * screen_height)
    return format_width, format_height

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_percentage(75)))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()