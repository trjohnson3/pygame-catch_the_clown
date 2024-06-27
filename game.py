import pygame, random

#Initialize game
pygame.init()

#Set display window
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch the Clown')

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

#Set colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('./fonts/Franxurter.ttf', 32)

#Set text
title_text = font.render('Catch the Clown', True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render('Lives: ' + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

player_lives_text = font.render('Lives: ' + str(player_lives), True, YELLOW)
player_lives_rect = player_lives_text.get_rect()
player_lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render('GAME OVER', True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Press any key to play again', True, BLUE, YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set sounds
hit_sound = pygame.mixer.Sound('./sounds/click.wav')
miss_sound = pygame.mixer.Sound('./sounds/miss.wav')
pygame.mixer.music.load('./sounds/song.wav')


#Set images
background_image = pygame.image.load('./images/background.png')
background_rect = background_image.get_rect()
background_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

clown_image = pygame.image.load('./images/clown.png')
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)




#Main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #Check if clown was clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                hit_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                # Move clown in new direction
                prev_dx = clown_dx
                prev_dy = clown_dy
                while(prev_dx == clown_dx and prev_dy == clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

            #if missed clown
            else:
                miss_sound.play()
                player_lives -= 1

    #Move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    #Bounce the clown
    if clown_rect.x <= 0 or clown_rect.x >= WINDOW_WIDTH - 48:
        clown_dx = -1*clown_dx
    if clown_rect.y <= 0 or clown_rect.y >= WINDOW_HEIGHT - 48:
        clown_dy = -1*clown_dy

    #Update HUD
    score_text = font.render('Score: ' + str(score), True, YELLOW)
    player_lives_text = font.render('Lives: ' + str(player_lives), True, YELLOW)

    #Check for game over
    if player_lives <= 0:
        display.blit(player_lives_text, player_lives_rect)
        display.blit(game_over_text, game_over_rect)
        display.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause until the player clicks, then restart game
        pygame.mixer.music.stop()
        pygame.time.wait(500)
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #Wants to play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                #Wants to quit
                elif event.type == pygame.QUIT:
                    is_paused = False
                    running = False



    #Filling display
    display.fill(BLACK)

    #Blit background
    display.blit(background_image, background_rect)

    #Blit HUD
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
    display.blit(player_lives_text, player_lives_rect)

    #Blit Assests
    display.blit(clown_image, clown_rect)

    #Tick the Clock
    clock.tick(FPS)



    #Update display
    pygame.display.update()


#End game
pygame.quit()
