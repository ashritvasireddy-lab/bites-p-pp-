import pygame
import random
import sys

# Global Variables
FPS = 32
SCREENWIDTH = 400
SCREENHEIGHT = 600
GROUNDY = SCREENHEIGHT * 0.8

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Pygame Setup
pygame.init()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Flappy Bird - Python")
FPSCLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

# Bird Variables
bird_x = 50
bird_y = 300
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_strength = -10

# Pipes
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipes = []

# Score
score = 0

# Function to create new pipe
def create_pipe():
    y = random.randint(100, SCREENHEIGHT - pipe_gap - 100)
    pipes.append({'x': SCREENWIDTH, 'y': y})

# Initial Pipes
for i in range(2):
    create_pipe()
    pipes[i]['x'] += i * 200

# Welcome Screen
def welcomeScreen():
    SCREEN.fill(BLUE)
    msg = FONT.render("Press SPACE to Start", True, WHITE)
    SCREEN.blit(msg, (SCREENWIDTH//2 - msg.get_width()//2, SCREENHEIGHT//2))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Collision Detection
def isCollide():
    if bird_y - bird_radius <= 0 or bird_y + bird_radius >= GROUNDY:
        return True
    for pipe in pipes:
        if pipe['x'] < bird_x + bird_radius < pipe['x'] + pipe_width:
            if bird_y - bird_radius < pipe['y'] or bird_y + bird_radius > pipe['y'] + pipe_gap:
                return True
    return False

# Main Game Loop
def mainGame():
    global bird_y, bird_velocity, pipes, score
    bird_y = 300
    bird_velocity = 0
    score = 0
    pipes = []
    for i in range(2):
        create_pipe()
        pipes[i]['x'] += i * 200

    running = True
    while running:
        FPSCLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_velocity = flap_strength

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Move pipes
        for pipe in pipes:
            pipe['x'] -= pipe_speed

        # Add new pipe
        if pipes[-1]['x'] < SCREENWIDTH - 200:
            create_pipe()

        # Remove offscreen pipes
        if pipes[0]['x'] + pipe_width < 0:
            pipes.pop(0)

        # Check collision
        if isCollide():
            print(f"Game Over! Score: {score}")
            return

        # Check score
        for pipe in pipes:
            if pipe['x'] + pipe_width == bird_x:
                score += 1
                print(f"Score: {score}")

        # Draw everything
        SCREEN.fill(BLUE)
        # Draw bird
        pygame.draw.circle(SCREEN, YELLOW, (bird_x, int(bird_y)), bird_radius)
        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(SCREEN, GREEN, (pipe['x'], 0, pipe_width, pipe['y']))
            pygame.draw.rect(SCREEN, GREEN, (pipe['x'], pipe['y'] + pipe_gap, pipe_width, SCREENHEIGHT - pipe['y'] - pipe_gap))
        # Draw ground
        pygame.draw.rect(SCREEN, RED, (0, GROUNDY, SCREENWIDTH, SCREENHEIGHT - GROUNDY))
        # Draw score
        score_text = FONT.render(str(score), True, WHITE)
        SCREEN.blit(score_text, (SCREENWIDTH//2 - score_text.get_width()//2, 20))

        pygame.display.update()

# Run the game
while True:
    welcomeScreen()
    mainGame()
