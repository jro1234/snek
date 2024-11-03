

import pygame
import time
import random



# Game loop function
def gameLoop():

    game_over  = False
    game_close = False

    x1 = app.display_width  / 2
    y1 = app.display_height / 2

    x1_change = 0
    y1_change = 0

    while not game_over:

        while game_close:

            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            Your_score(Length_of_snake - 1)
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

                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0

                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0


        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change

        dis.fill(black)

        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:

            del snake_List[0]

        for x in snake_List[:-1]:

            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width  - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

    quit()

