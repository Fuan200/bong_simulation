import pygame

percentage = 75

def screen_percentage_width(percentage):
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    percentage /= 100
    format_width = int(percentage * screen_width)
    return format_width

def screen_percentage_height(percentage):
    screen_info = pygame.display.Info()
    screen_height = screen_info.current_h
    percentage /= 100
    format_height = int(percentage * screen_height)
    return format_height

def get_width():
    screen_width = screen_percentage_width(percentage)
    return screen_width

def get_height():
    screen_height = screen_percentage_height(percentage)
    return screen_height