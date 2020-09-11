import pygame
import random

pygame.init()

#CREATING WINDOW
WIDTH ,HEIGHT = 600 ,400
win =  pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Snake Game")

#Game Variabales
WHITE = (255,255,255)
BLUE = (0 , 0 ,255)
RED = (255, 0 ,0)
GREEN =  (0, 255, 0)
BLACK = (0,0,0)

snake_move = 10


font_style = pygame.font.SysFont("comicsans" ,60)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg ,  color):
    game_over = font_style.render(msg,True,color)
    win.blit(game_over,[WIDTH/6  ,HEIGHT/3])

#GAME LOOP
def gameloop():
    FPS = 15
    x1 = WIDTH/2
    y1 = HEIGHT/2
    x1_move = 0
    y1_move = 0
    snake_List = []
    Length_of_snake = 1
    clock = pygame.time.Clock()
    run = True
    game_end = False
    foodx = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_move) / 10.0) * 10.0
    while run :
        #while  not game_end:
        """    win.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_end = True
                        run = False
                    if event.key == pygame.K_c:
                        gameloop()"""

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    x1_move = -snake_move
                    y1_move = 0
                elif event.key == pygame.K_RIGHT :
                    x1_move = snake_move
                    y1_move = 0
                elif event.key == pygame.K_UP :
                    x1_move = 0
                    y1_move = -snake_move
                elif event.key == pygame.K_DOWN :
                    x1_move = 0
                    y1_move = snake_move
        if(x1 >= WIDTH or x1 <0 or y1 >=HEIGHT or y1 < 0 ) :
            run = False;
        x1 += x1_move
        y1 += y1_move
        win.fill(BLUE)
        pygame.draw.rect(win, GREEN, [foodx, foody, snake_move, snake_move])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1) #To makae a tuple
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake :
            del snake_List[0] 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_end = True
        our_snake(snake_move, snake_List)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_move) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(FPS)
    pygame.QUIT()

gameloop()






