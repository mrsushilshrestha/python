import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Car Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Car settings
CAR_WIDTH = 50
CAR_HEIGHT = 100
car_speed = 5

# Load car image or create a rectangle for the car
car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car.fill(BLUE)
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10

# Obstacle settings
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
obstacle = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle.fill(RED)
obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
obstacle_y = -OBSTACLE_HEIGHT
obstacle_speed = 7

# Power-up settings
POWERUP_WIDTH = 30
POWERUP_HEIGHT = 30
powerup = pygame.Surface((POWERUP_WIDTH, POWERUP_HEIGHT))
powerup.fill(YELLOW)
powerup_x = random.randint(0, SCREEN_WIDTH - POWERUP_WIDTH)
powerup_y = -POWERUP_HEIGHT
powerup_speed = 5
powerup_active = False
powerup_timer = 0

# Score, lives, and difficulty
score = 0
lives = 3
level = 1
font = pygame.font.Font(None, 36)

# Road settings
ROAD_WIDTH = 400
road_x = (SCREEN_WIDTH - ROAD_WIDTH) // 2
road_y1 = 0
road_y2 = -SCREEN_HEIGHT
lane_width = ROAD_WIDTH // 3
line_height = 40
line_gap = 20
line_color = WHITE
road_speed = 5

def draw_road():
    pygame.draw.rect(screen, GRAY, (road_x, 0, ROAD_WIDTH, SCREEN_HEIGHT))

    # Draw lane dividers
    for y in range(road_y1 % (line_height + line_gap), SCREEN_HEIGHT, line_height + line_gap):
        for lane in range(1, 3):  # Draw lines for two lanes
            line_x = road_x + lane * lane_width - 2
            pygame.draw.rect(screen, line_color, (line_x, y, 4, line_height))

    for y in range(road_y2 % (line_height + line_gap), SCREEN_HEIGHT, line_height + line_gap):
        for lane in range(1, 3):
            line_x = road_x + lane * lane_width - 2
            pygame.draw.rect(screen, line_color, (line_x, y, 4, line_height))

def display_info():
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(level_text, (10, 90))

def reset_powerup():
    global powerup_x, powerup_y, powerup_active
    powerup_x = random.randint(road_x + 10, road_x + ROAD_WIDTH - POWERUP_WIDTH - 10)
    powerup_y = -POWERUP_HEIGHT
    powerup_active = False

def increase_difficulty():
    global obstacle_speed, powerup_speed, road_speed, level
    level += 1
    obstacle_speed += 1
    powerup_speed += 0.5
    road_speed += 0.5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > road_x:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < road_x + ROAD_WIDTH - CAR_WIDTH:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y < SCREEN_HEIGHT - CAR_HEIGHT:
        car_y += car_speed

    # Update road position
    road_y1 += road_speed
    road_y2 += road_speed
    if road_y1 >= SCREEN_HEIGHT:
        road_y1 = -SCREEN_HEIGHT
    if road_y2 >= SCREEN_HEIGHT:
        road_y2 = -SCREEN_HEIGHT

    # Update obstacle position
    obstacle_y += obstacle_speed

    # Respawn obstacle if it goes off screen
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = -OBSTACLE_HEIGHT
        obstacle_x = random.randint(road_x, road_x + ROAD_WIDTH - OBSTACLE_WIDTH)
        score += 1
        if score % 10 == 0:  # Increase difficulty every 10 points
            increase_difficulty()

    # Update power-up position
    powerup_y += powerup_speed

    # Respawn power-up if it goes off screen
    if powerup_y > SCREEN_HEIGHT:
        reset_powerup()

    # Check for collision with obstacle
    if (car_x < obstacle_x + OBSTACLE_WIDTH and
        car_x + CAR_WIDTH > obstacle_x and
        car_y < obstacle_y + OBSTACLE_HEIGHT and
        car_y + CAR_HEIGHT > obstacle_y):
        lives -= 1
        obstacle_y = -OBSTACLE_HEIGHT
        obstacle_x = random.randint(road_x, road_x + ROAD_WIDTH - OBSTACLE_WIDTH)
        if lives == 0:
            print("Game Over!")
            print(f"Your final score: {score}")
            running = False

    # Check for collision with power-up
    if (car_x < powerup_x + POWERUP_WIDTH and
        car_x + CAR_WIDTH > powerup_x and
        car_y < powerup_y + POWERUP_HEIGHT and
        car_y + CAR_HEIGHT > powerup_y):
        powerup_active = True
        powerup_timer = pygame.time.get_ticks()
        reset_powerup()

    # Handle power-up effect (temporary speed boost)
    if powerup_active:
        car_speed = 8
        if pygame.time.get_ticks() - powerup_timer > 5000:  # Power-up lasts 5 seconds
            car_speed = 5
            powerup_active = False

    # Drawing everything
    screen.fill(BLACK)  # Clear screen
    draw_road()  # Draw road with lanes
    screen.blit(car, (car_x, car_y))  # Draw car
    screen.blit(obstacle, (obstacle_x, obstacle_y))  # Draw obstacle
    screen.blit(powerup, (powerup_x, powerup_y))  # Draw power-up
    display_info()  # Display score, lives, and level

    pygame.display.flip()  # Update screen
    clock.tick(60)  # Limit frame rate

pygame.quit()
sys.exit()
