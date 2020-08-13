# Game text 
import pygame

black = (0,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(gameDisplay, text, y):
    
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    #TextRect.center = ((display_width/2),(display_height/2))
    #TextRect.center = (20,10)
    gameDisplay.blit(TextSurf, (20,y))

    pygame.display.update()



