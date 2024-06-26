import pygame

#Initialize game
pygame.init()

#Set display window
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch the Clown')


#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#End game
pygame.quit()
