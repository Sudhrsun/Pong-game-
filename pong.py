import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the clock
clock = pygame.time.Clock()

# Paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
PADDLE_SPEED = 5

# Ball properties
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Font settings
FONT_SIZE = 36
font = pygame.font.SysFont(None, FONT_SIZE)

class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = color
        self.speed = PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = BALL_SIZE
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def draw(self):
        pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce(self):
        if self.y <= 0 or self.y >= HEIGHT:
            self.speed_y *= -1

        if self.x <= player_paddle.x + player_paddle.width and \
           player_paddle.y <= self.y <= player_paddle.y + player_paddle.height:
            self.speed_x *= -1

        if self.x >= computer_paddle.x - self.size and \
           computer_paddle.y <= self.y <= computer_paddle.y + computer_paddle.height:
            self.speed_x *= -1

        if self.x <= 0:
            return "player"
        elif self.x >= WIDTH:
            return "computer"
        else:
            return None

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update():
    # Move the player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.y > 0:
        player_paddle.y -= player_paddle.speed
    if keys[pygame.K_DOWN] and player_paddle.y < HEIGHT - player_paddle.height:
        player_paddle.y += player_paddle.speed

    # Move the computer's paddle
    if ball.y < computer_paddle.y + computer_paddle.height // 2:
        computer_paddle.y -= computer_paddle.speed
    elif ball.y > computer_paddle.y + computer_paddle.height // 2:
        computer_paddle.y += computer_paddle.speed

    # Move the ball
    ball.move()

    # Check for collisions with walls and paddles
    result = ball.bounce()
    if result == "player":
        return "Game Over! You missed the ball."
    elif result == "computer":
        return "Congratulations! You won."

    return None

def draw():
    # Clear the screen
    WIN.fill(BLACK)

    # Draw the paddles
    player_paddle.draw()
    computer_paddle.draw()

    # Draw the ball
    ball.draw()

    # Update the display
    pygame.display.update()

def render_text(text):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(text_surface, text_rect)
    pygame.display.update()

def main():
    global player_paddle, computer_paddle, ball

    player_paddle = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, GREEN)
    computer_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, RED)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        running = handle_events()
        if not running:
            break

        result = update()
        if result:
            print(result)
            render_text(result)
            time.sleep(8)  # Wait for 2 seconds before closing
            break

        draw()

        # Limit frames per second
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
