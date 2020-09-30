import random
import string
import pygame
pygame.init()
screen_color = (0, 51, 102)
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Random Password Generator")
white = (255, 255, 255)

def generate_password(length):
    password = ''.join([random.choice(string.ascii_letters + string.digits) for char in range(length)])
    return password

font = pygame.font.Font('freesansbold.ttf', 34)
text = font.render(f"Password: {generate_password(8)}", True, white, screen_color)
tRect = text.get_rect()
tRect.center = ((200, 200))

running = True

while running:
    screen.fill(screen_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text, tRect)
    pygame.display.update()

