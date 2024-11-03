
import pygame
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Screen size
dis_width = 800
dis_height = 600

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the snake
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)


class Snake:
    def __init__(self, snake_block):
        self.snake_block = snake_block
        self.snake_speed = 15
        self.snake_list = []
        self.length_of_snake = 1
        self.head_x = dis_width / 2
        self.head_y = dis_height / 2
        self.x_change = 0
        self.y_change = 0

    def grow(self):
        self.length_of_snake += 1
        self.snake_speed += 1  # Increase speed with each food

    def move(self):
        self.head_x += self.x_change
        self.head_y += self.y_change

        # Boundary wrapping
        if self.head_x >= dis_width:
            self.head_x = 0
        elif self.head_x < 0:
            self.head_x = dis_width
        if self.head_y >= dis_height:
            self.head_y = 0
        elif self.head_y < 0:
            self.head_y = dis_height

    def update_snake_list(self):
        snake_head = [self.head_x, self.head_y]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

    def check_collision_with_self(self):
        for x in self.snake_list[:-1]:
            if x == [self.head_x, self.head_y]:
                return True
        return False

    def draw_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], self.snake_block, self.snake_block])

    def change_direction(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change


def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


# Main game loop function
def gameLoop():
    game_over  = False
    game_close = False

    snake = Snake(snake_block=10)

    # Initial food position
    foodx = round(random.randrange(0, dis_width - snake.snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake.snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 4, dis_height / 3])
            display_score(snake.length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.x_change == 0:
                    snake.change_direction(-snake.snake_block, 0)
                elif event.key == pygame.K_RIGHT and snake.x_change == 0:
                    snake.change_direction(snake.snake_block, 0)
                elif event.key == pygame.K_UP and snake.y_change == 0:
                    snake.change_direction(0, -snake.snake_block)
                elif event.key == pygame.K_DOWN and snake.y_change == 0:
                    snake.change_direction(0, snake.snake_block)

        snake.move()
        if snake.check_collision_with_self():
            game_close = True

        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake.snake_block, snake.snake_block])

        snake.update_snake_list()
        snake.draw_snake()
        display_score(snake.length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten the food
        if snake.head_x == foodx and snake.head_y == foody:
            foodx = round(random.randrange(0, dis_width - snake.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake.snake_block) / 10.0) * 10.0
            snake.grow()

        clock.tick(snake.snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
