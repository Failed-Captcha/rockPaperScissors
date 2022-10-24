import pygame

def main():
    pygame.init()
    surfaceSize = 650 
    
    clock = pygame.time.Clock()  
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    pygame_icon = pygame.image.load('icon.png')
    pygame.display.set_caption("Client")
    pygame.display.set_icon(pygame_icon)
    while True:
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit() # Once we leave the loop, close the window.
    
main()