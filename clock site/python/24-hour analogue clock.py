import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 410, 420
center = (width // 2, height // 2)
radius = 150
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Digital Hand Clock")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)

# Fonts
font_size = 24
font = pygame.font.SysFont(None, font_size)

def draw_hand(text, angle, length, color):
    radian = math.radians(angle)
    num_repeats = 6  # Adjust the number of repeats as needed
    step_length = length / num_repeats
    for i in range(num_repeats):
        end_pos = (
            center[0] + (i * step_length) * math.cos(radian),
            center[1] + (i * step_length) * math.sin(radian)
        )
        hand_text = font.render(text, True, color)
        text_rect = hand_text.get_rect(center=end_pos)
        screen.blit(hand_text, text_rect)

def draw_clock(hour, minute, second):
    screen.fill(white)

    # Draw clock face
    pygame.draw.circle(screen, black, center, radius, 2)

    # Calculate angles for hands
    hour_angle = (360 / 24) * hour - 90
    minute_angle = (360 / 60) * minute - 90
    second_angle = (360 / 60) * second - 90

    # Draw digital hands
    draw_hand(f"{hour:02d}", hour_angle, radius * 0.93, blue)   # Hour hand
    draw_hand(f"{minute:02d}", minute_angle, radius * 1.0, green)  # Minute hand
    draw_hand(f"{second:02d}", second_angle, radius * 1.1, red)  # Second hand

    # Draw date and current time
    current_date = time.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")
    
    date_text = font.render(current_date, True, cyan)
    time_text = font.render(current_time, True, cyan)
    
    screen.blit(date_text, (width // 2 - date_text.get_width() // 2, height // 2 + 160))
    screen.blit(time_text, (width // 2 - time_text.get_width() // 2, height // 2 + 190))

    pygame.display.flip()

running = True
clock = pygame.time.Clock()  # Create a Pygame clock object
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    draw_clock(hour, minute, second)
    clock.tick(1)  # Ensure the loop runs at 1 frame per second

pygame.quit()
