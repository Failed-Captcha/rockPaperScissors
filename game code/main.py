import pygame

def main():
    pygame.init()    
    clock = pygame.time.Clock()    
    mainSurface = pygame.display.set_mode((1200,720))
    
    name = ""
    mode = "game select"
    font = pygame.font.Font('freesansbold.ttf', 35)
    knucklebonesBackground = pygame.image.load("knucklebonesbg.PNG")
    
    while True:
        ev = pygame.event.poll()  
        if ev.type == pygame.QUIT:
            loadVariables = [line.rstrip() for line in open('knucklebones new game.txt')]
            if int(loadVariables[0])>0:
                loadVariables[0]=int(loadVariables[0])-1;
                file = open('knucklebones new game.txt', 'w')
                for i in range (len(loadVariables)):
                    file.write(f'{loadVariables[i]}\n')
                file.close()
            break #end game 
        else:
            mousePos = pygame.mouse.get_pos()
            
        if mode == "game select":
            
            #type name
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += ev.unicode
                
            if ev.type == pygame.MOUSEBUTTONUP:
                
                #if knucklebones button pressed
                if ev.pos[0]>=100 and ev.pos[0]<=400 and ev.pos[1]>=200 and ev.pos[1]<=300:
                    
                    #load new game variables
                    loadVariables = [line.rstrip() for line in open('knucklebones new game.txt')]
                    playersConnected = int(loadVariables[0])
                    if name == "":
                        if playersConnected == 0:
                            name = "player 1"
                        else:
                            name = "player 2"
                    
                    #change playersConnected in file
                    if playersConnected < 3:
                        loadVariables[0]= int(loadVariables[0])+1;
                        file = open('knucklebones new game.txt', 'w')
                        for i in range (len(loadVariables)):
                            file.write(f'{loadVariables[i]}\n')
                        file.close()
                        
                    if playersConnected == 1:
                        print("waiting for another player...")
                        loadVariables = [line.rstrip() for line in open('knucklebones new game.txt')]
                        playersConnected = int(loadVariables[0])
                        
                if playersConnected == 2:
                    print("knucklebones")
                    mode = "knucklebones"
                elif playersConnected > 2:
                    print("the game is full :(")
            
            #draw background and buttons
            pygame.Surface.fill(mainSurface,(255,255,255))
            
            pygame.draw.rect(mainSurface,(100,100,100),(100,200,300,100))
            pygame.draw.rect(mainSurface,(100,100,100),(450,200,300,100))
            pygame.draw.rect(mainSurface,(200,200,200),(450,500,300,100))
            line = font.render("knucklebones",1,(0,0,0))
            mainSurface.blit(line,(125,240))
            line = font.render("Enter Name:",1,(0,0,0))
            mainSurface.blit(line,(450,450))
            line = font.render(name,1,(0,0,0))
            mainSurface.blit(line,(450,500))
            
        if mode == "knucklebones":
            mainSurface.blit(knucklebonesBackground,(0,0))
            line = font.render(name,1,(255,255,255))
            mainSurface.blit(line,(100,400))
        
        #print(pygame.mouse.get_pos())
        #print(name)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
main()
