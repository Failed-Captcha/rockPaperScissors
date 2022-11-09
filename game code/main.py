import pygame

def main():
    pygame.init()    
    clock = pygame.time.Clock()    
    mainSurface = pygame.display.set_mode((1200,720))
    
    name = "player1"
    mode = "game select"
    font = pygame.font.Font('freesansbold.ttf', 35)
    knucklebonesBackground = pygame.image.load("knucklebonesbg.PNG")
    
    while True:
        ev = pygame.event.poll()  
        if ev.type == pygame.QUIT:  
            break #end game 
        else:
            mousePos = pygame.mouse.get_pos()
            
        if mode == "game select":
            if ev.type == pygame.MOUSEBUTTONUP:
                if ev.pos[0]>=100 and ev.pos[0]<=400 and ev.pos[1]>=200 and ev.pos[1]<=300:
                    print("knucklebones")
                    mode = "knucklebones"
            
            #draw background and buttons
            pygame.Surface.fill(mainSurface,(255,255,255))
            
            pygame.draw.rect(mainSurface,(100,100,100),(100,200,300,100))
            pygame.draw.rect(mainSurface,(100,100,100),(450,200,300,100))
            line = font.render("knucklebones",1,(0,0,0))
            mainSurface.blit(line,(125,240))
            
        if mode == "knucklebones":
            mainSurface.blit(knucklebonesBackground,(0,0))
 
        
        #print(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
main()
