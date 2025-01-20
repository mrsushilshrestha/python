import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Initialize mixer for sound
pygame.mixer.init()

# Load background music
if getattr(sys, 'frozen', False):  # Check if running as an exe
    music_path = os.path.join(sys._MEIPASS, "background_music.mp3")
else:  # Running as a script
    music_path = os.path.join(os.path.dirname(__file__), "background_music.mp3")

# Check if the music file exists in the directory
if not os.path.exists(music_path):
    print(f"Error: The music file was not found at {music_path}")
    sys.exit()

# Load the music
pygame.mixer.music.load(music_path)

# Get screen dimensions (fullscreen)
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)

# Initialize screen (fullscreen)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Dynamic Road Car Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Car settings
CAR_WIDTH = 50
CAR_HEIGHT = 100
car_speed = 5
car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car.fill(BLUE)
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10

# Obstacle settings
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
obstacle = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle.fill(RED)
obstacle_x = random.randint((SCREEN_WIDTH - 400) // 2, (SCREEN_WIDTH + 400) // 2 - OBSTACLE_WIDTH)
obstacle_y = -OBSTACLE_HEIGHT
obstacle_speed = 7

# Power-up settings
POWERUP_WIDTH = 30
POWERUP_HEIGHT = 30
powerup = pygame.Surface((POWERUP_WIDTH, POWERUP_HEIGHT))
powerup.fill(YELLOW)
powerup_x = random.randint((SCREEN_WIDTH - 400) // 2, (SCREEN_WIDTH + 400) // 2 - POWERUP_WIDTH)
powerup_y = -POWERUP_HEIGHT
powerup_speed = 5
powerup_active = False
powerup_timer = 0

# Road settings
ROAD_WIDTH = 400
road_x = (SCREEN_WIDTH - ROAD_WIDTH) // 2
road_y = 0
road_speed = 5

# Score and lives
score = 0
lives = 5
level = 1
font = pygame.font.Font(None, 36)

def draw_road():
    global road_y
    pygame.draw.rect(screen, GRAY, (road_x, 0, ROAD_WIDTH, SCREEN_HEIGHT))

    # Move lane dividers
    road_y += road_speed
    if road_y > SCREEN_HEIGHT:
        road_y -= SCREEN_HEIGHT

    # Draw lane dividers
    for y in range(-SCREEN_HEIGHT, SCREEN_HEIGHT, 60):
        offset_y = y + road_y
        pygame.draw.line(screen, WHITE, (road_x + ROAD_WIDTH // 3, offset_y), (road_x + ROAD_WIDTH // 3, offset_y + 40), 2)
        pygame.draw.line(screen, WHITE, (road_x + 2 * ROAD_WIDTH // 3, offset_y), (road_x + 2 * ROAD_WIDTH // 3, offset_y + 40), 2)

def display_info():
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(level_text, (SCREEN_WIDTH - 150, 10))

def reset_obstacle():
    global obstacle_x, obstacle_y
    obstacle_x = random.randint(road_x, road_x + ROAD_WIDTH - OBSTACLE_WIDTH)
    obstacle_y = -OBSTACLE_HEIGHT

def reset_powerup():
    global powerup_x, powerup_y
    powerup_x = random.randint(road_x, road_x + ROAD_WIDTH - POWERUP_WIDTH)
    powerup_y = -POWERUP_HEIGHT

def game_over():
    global score, level, lives
    pygame.mixer.music.stop()  # Stop music when game is over
    screen.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, RED)
    replay_text = font.render("Press 'R' to Replay or 'Q' to Quit", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(replay_text, (SCREEN_WIDTH // 2 - replay_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Replay
                    score = 0
                    lives = 5
                    level = 1
                    return True
                elif event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    sys.exit()

    return False

# Game loop
running = True
while running:
    screen.fill(BLACK)
    game_start_text = font.render("Press any key to Start", True, WHITE)
    screen.blit(game_start_text, (SCREEN_WIDTH // 2 - game_start_text.get_width() // 2, SCREEN_HEIGHT // 3))
    pygame.display.flip()

    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Start game
                pygame.mixer.music.play(-1)  # Start music when game starts
                waiting_for_start = False
                break

    # Game loop
    car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
    car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

        # Update obstacle
        obstacle_y += obstacle_speed
        if obstacle_y > SCREEN_HEIGHT:
            reset_obstacle()
            score += 1

        # Update power-up
        powerup_y += powerup_speed
        if powerup_y > SCREEN_HEIGHT:
            reset_powerup()

        # Collision detection
        if (car_x < obstacle_x + OBSTACLE_WIDTH and
            car_x + CAR_WIDTH > obstacle_x and
            car_y < obstacle_y + OBSTACLE_HEIGHT and
            car_y + CAR_HEIGHT > obstacle_y):
            lives -= 1
            reset_obstacle()
            if lives == 0:
                if not game_over():
                    running = False
                break

        if (car_x < powerup_x + POWERUP_WIDTH and
            car_x + CAR_WIDTH > powerup_x and
            car_y < powerup_y + POWERUP_HEIGHT and
            car_y + CAR_HEIGHT > powerup_y):
            powerup_active = True
            powerup_timer = pygame.time.get_ticks()
            reset_powerup()

        # Power-up effect
        if powerup_active and pygame.time.get_ticks() - powerup_timer > 5000:
            powerup_active = False

        # Increase level
        level = score // 5 + 1
        obstacle_speed = 7 + level

        # Draw everything
        screen.fill(BLACK)
        draw_road()
        screen.blit(car, (car_x, car_y))
        screen.blit(obstacle, (obstacle_x, obstacle_y))
        screen.blit(powerup, (powerup_x, powerup_y))
        display_info()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()
