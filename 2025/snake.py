import pygame
import random

WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (34, 47, 62)
SNAKE_SIZE = 20
SNAKE_COLOR = (87, 101, 116)
SNAKE_HEAD_COLOR = (131, 149, 167)
APPLE_COLOR = (238, 82, 83)
BUTTON_COLOR = (16, 172, 132)
BUTTON_TEXT_COLOR = (200, 214, 229)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 20)
button_font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2
dx, dy = 0, 0
snake_body = [(x, y)]
score = 0
game_running = False
paused = False


def spawn_apple():
    while True:
        apple_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        apple_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

        if (apple_x, apple_y) not in snake_body:
            return apple_x, apple_y


apple_x, apple_y = spawn_apple()


def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))
    text_surf = button_font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)


is_run = True
while is_run:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 200 <= mx <= 400 and 150 <= my <= 200:
                game_running = True
                paused = False
                x, y = WIDTH // 2, HEIGHT // 2
                dx, dy = 0, 0
                score = 0
                snake_body = [(x, y)]
                apple_x, apple_y = spawn_apple()
            if 200 <= mx <= 400 and 210 <= my <= 260:
                game_running = True
                paused = False
                x, y = WIDTH // 2, HEIGHT // 2
                dx, dy = 0, 0
                score = 0
                snake_body = [(x, y)]
                apple_x, apple_y = spawn_apple()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and game_running:
                paused = not paused
            if game_running and not paused:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -SNAKE_SIZE
                if event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, SNAKE_SIZE
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -SNAKE_SIZE, 0
                if event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = SNAKE_SIZE, 0

    if game_running and not paused:
        x += dx
        y += dy
        snake_body.append((x, y))
        snake_body = snake_body[-(score + 1) :]

        if x == apple_x and y == apple_y:
            score += 1
            apple_x, apple_y = spawn_apple()
            pygame.display.set_caption(f"Snake v0.1 - Score: {score}")

        if (
            x < 0
            or x >= WIDTH
            or y < 0
            or y >= HEIGHT
            or len(snake_body) != len(set(snake_body))
        ):
            game_running = False

    if game_running:
        pygame.draw.rect(
            screen, APPLE_COLOR, (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        )
        for i, segment in enumerate(snake_body):
            color = SNAKE_HEAD_COLOR if i == len(snake_body) - 1 else SNAKE_COLOR
            pygame.draw.rect(
                screen, color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE)
            )
    else:
        draw_button("Start", 200, 150, 200, 50)
        if paused:
            draw_button("Restart", 200, 210, 200, 50)

    pygame.display.update()
    clock.tick(8)
pygame.quit()
