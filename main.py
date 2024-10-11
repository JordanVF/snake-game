import pygame
import random

#region Setup/Initialization
pygame.init()

    # Setting game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

    #Object Colors
snake_color = (255,0,25)
fruit_color = (252,211,3)
score_color = (13,255,0)
background_color = (0,0,0)

    #Game state
score = 0
running = True
clock = pygame.time.Clock()

#region Snake Values
    #Starting position
x1 = window_width/2
y1 = window_height/2
    #Direction changes
x1_change = 0
y1_change = 0
    #Length
snake_body = []
snake_length = 1
#endregion

#region Food Values
foodx = round(random.randrange(0,window_width - 10) / 10) * 10.0
foody = round(random.randrange(0,window_height - 10) / 10) * 10.0
#endregion

#endregion

while running:
    #Keep program running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Check for arrow key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    #Update Position
    x1 = x1 + x1_change
    y1 = y1 + y1_change
    window.fill(background_color)

    #Keep track of growing body
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    #Grow snake, also delete shadow as moving
    snake_body.append(snake_head)
    if len(snake_body)>snake_length:
        del snake_body[0]

    #Boundaries
    if x1>=window_width or x1<0 or y1>=window_height or y1<0:
        running = False

    #Snake Collision
    for segment in snake_body[:-1]:
        if segment == snake_head:
            running = False

    #Check/Snake eats food
    if x1 == foodx and y1 == foody:
        #Regenerate food after eaten
        foodx = round(random.randrange(0,window_width - 10) / 10) * 10.0
        foody = round(random.randrange(0,window_height - 10) / 10) * 10.0
        #Add length to snake after eating
        snake_length += 1
        score += 1

    #Draw Food
    pygame.draw.rect(window,fruit_color,[foodx,foody,10,10])

    #Draw Snake
    for segment in snake_body:
        pygame.draw.rect(window,snake_color,[segment[0],segment[1],10,10])
    print(snake_body)
    print(f"Final Score: {score}")
    
    #Display Score
    font_style = pygame.font.SysFont(None,50)
    score_text = font_style.render("Score: "+str(score),True,score_color)
    window.blit(score_text,(10,10))

    #Gameplay
    pygame.display.update()
    clock.tick(15)