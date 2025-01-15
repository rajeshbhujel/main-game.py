import pygame
import random

pygame.init()

# Screen dimensions
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake properties
snake_block = 20
snake_speed = 10

# Initialize fonts
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 35)

# Functions
def draw_snake(snake_list):
    for i, block in enumerate(snake_list):
        color = pygame.Color(0, 255, 0)
        color.hsva = (120 + (i * 5) % 360, 100, 100, 100)
        pygame.draw.rect(window, color, [block[0], block[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 2 + y_displace))
    window.blit(mesg, text_rect)

def draw_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))

    button_text = small_font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=(x + w / 2, y + h / 2))
    window.blit(button_text, text_rect)
    return False

def gameLoop():
    game_over = False
    game_close = False

    x1 = width // 2
    y1 = height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message("Game Over!", RED, -50)
            message(f"Score: {length_of_snake - 1}", WHITE, 0)

            if draw_button("Restart", width // 2 - 60, height // 2 + 50, 120, 40, GREEN, BLUE):
                gameLoop()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = snake_block

        # Wall collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        window.fill(BLACK)
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        # Draw score
        score = length_of_snake - 1
        score_text = font.render(f"Score: {score}", True, WHITE)
        window.blit(score_text, [10, 10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
