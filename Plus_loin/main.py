
import pygame
import random

# Definir el tamaño de la pantalla
WIDTH = 800
HEIGHT = 600

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clase para representar la serpiente
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, 10, 10))

# Clase para representar la manzana
class Apple:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 10)
        self.y = random.randint(0, HEIGHT - 10)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, 10, 10))

# Función principal del juego
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    apple = Apple()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        snake.move()

        if snake.body[0] == (apple.x, apple.y):
            apple = Apple()

        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.flip()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
