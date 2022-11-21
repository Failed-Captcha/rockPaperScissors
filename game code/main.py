import pygame
import random

def main():
    pygame.init()    
    clock = pygame.time.Clock()    
    mainSurface = pygame.display.set_mode((1200,720))
    
    name = ""
    turn = 0
    mode = "game select"
    font = pygame.font.Font('freesansbold.ttf', 35)
    knucklebonesBackground = pygame.image.load("knucklebonesbg.PNG")
    die = pygame.image.load("die.png")
    diceRect = [0,0,60,60]
    diceValue = 0;
    dieColumn1 = [0,0,0]
    dieColumn2 = [0,0,0]
    dieColumn3 = [0,0,0]
    dieRows = [0,0,0]
    
    yPos = [450,530,600]
    xPos = [460,570,680]
    white = [255,255,255]
    
    while True:
        ev = pygame.event.poll()  
        if ev.type == pygame.QUIT:
            reset();
            break #end game 
        else:
            mousePos = pygame.mouse.get_pos()
            
        if mode == "game select":
            loadVariables = [line.rstrip() for line in open('knucklebones new game.txt')]
            playersConnected = int(loadVariables[0])
            
            #type name
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += ev.unicode
                
            if ev.type == pygame.MOUSEBUTTONUP:
                
                if ev.pos[0]>=775 and ev.pos[0]<=875 and ev.pos[1]>=500 and ev.pos[1]<=600:
                    reset();
                    
                #if knucklebones button pressed
                if ev.pos[0]>=100 and ev.pos[0]<=400 and ev.pos[1]>=200 and ev.pos[1]<=300:
                    turn = 1
                    diceValue = random.randint(1,6)
                    diceRect = [60*diceValue-60,0,60,60]
                    
                    #load new game variables
                    if playersConnected == 0:
                        if name == "":
                            name = "player 1"
                        playerNum = 1;
                        player = "knucklebones player1.txt"
                        otherPlayer = "knucklebones player2.txt"
                    else:
                        if name == "":
                            name = "player 2"
                        playerNum = 2;
                        player = "knucklebones player2.txt"
                        otherPlayer = "knucklebones player1.txt"
                    
                    #change playersConnected in file
                    if playersConnected < 3:
                        loadVariables[0]= int(loadVariables[0])+1;
                        file = open('knucklebones new game.txt', 'w')
                        for i in range (len(loadVariables)):
                            file.write(f'{loadVariables[i]}\n')
                        file.close()
                    if playersConnected < 3:
                        print("knucklebones")
                        mode = "knucklebones"
                    elif playersConnected > 2:
                        print("the game is full :(")
                        
                    file = open(player, 'w')
                    loadVariables[1] = name
                    loadVariables[0] = 1
                    for i in range (len(loadVariables)):
                        file.write(f'{loadVariables[i]}\n')
                    file.close()
            
            #draw background and buttons
            pygame.Surface.fill(mainSurface,(255,255,255))
            
            pygame.draw.rect(mainSurface,(100,100,100),(100,200,300,100))
            pygame.draw.rect(mainSurface,(100,100,100),(450,200,300,100))
            pygame.draw.rect(mainSurface,(200,200,200),(450,500,300,100))
            pygame.draw.rect(mainSurface,(200,200,200),(775,500,100,100))
            line = font.render("knucklebones",1,(0,0,0))
            mainSurface.blit(line,(125,240))
            line = font.render("Enter Name:",1,(0,0,0))
            mainSurface.blit(line,(450,450))
            line = font.render(name,1,(0,0,0))
            mainSurface.blit(line,(450,500))
            line = font.render(f'{playersConnected}',1,(0,0,0))
            mainSurface.blit(line,(810,530))
            
        if mode == "knucklebones":
            mainSurface.blit(knucklebonesBackground,(0,0))
           
            if turn==playerNum:
                if diceValue>0:
                    if ev.type == pygame.MOUSEBUTTONUP:
                        if ev.pos[0]>450 and ev.pos[0]<770 and ev.pos[1]>450 and ev.pos[1]<670:
                            if ev.pos[0]<550 and dieRows[0]<3:
                                dieColumn1[dieRows[0]] = diceValue
                                dieRows[0]+=1
                                diceValue = 0
                                
                            elif ev.pos[0]<660 and ev.pos[0]>550 and dieRows[1]<3:
                                dieColumn2[dieRows[1]] = diceValue
                                dieRows[1]+=1
                                diceValue = 0
                                
                            elif ev.pos[0]>660 and dieRows[2]<3:
                                dieColumn3[dieRows[2]] = diceValue
                                dieRows[2]+=1       
                                diceValue = 0
                                
                            if diceValue == 0:
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                else: 
                    diceValue = random.randint(1,6)
                    diceRect = [60*diceValue-60,0,60,60]
                        
                    
                pygame.draw.rect(mainSurface,white,(140,520,60,60))
                mainSurface.blit(die,(140,520),diceRect)
            
            for i in range (3):
                if dieColumn1[i]>0:
                    pygame.draw.rect(mainSurface,white,(xPos[0],yPos[i],60,60))
                    mainSurface.blit(die,(xPos[0],yPos[i]),[60*dieColumn1[i]-60,0,60,60])
                if dieColumn2[i]>0:
                    pygame.draw.rect(mainSurface,white,(xPos[1],yPos[i],60,60))
                    mainSurface.blit(die,(xPos[1],yPos[i]),[60*dieColumn2[i]-60,0,60,60])
                if dieColumn3[i]>0:
                    pygame.draw.rect(mainSurface,white,(xPos[2],yPos[i],60,60))
                    mainSurface.blit(die,(xPos[2],yPos[i]),[60*dieColumn3[i]-60,0,60,60])
            
            saveVariables = [turn,name,0,0,0,0,diceValue,dieColumn1[0],dieColumn1[1],dieColumn1[2],dieColumn2[0],dieColumn2[1],dieColumn2[2],dieColumn3[0],dieColumn3[1],dieColumn3[2]]
            file = open(player, 'w')
            for i in range (len(saveVariables)):
                file.write(f'{saveVariables[i]}\n')
            file.close()
                
            loadOpponent = [line.rstrip() for line in open(otherPlayer)]
            opponentName = loadOpponent[1]
            if int(loadOpponent[0])>0:
                turn = loadOpponent[0]
            
            line = font.render(name,1,(255,255,255))
            mainSurface.blit(line,(100,400))
            line = font.render(opponentName,1,(255,255,255))
            mainSurface.blit(line,(960,425))
        
        #print(pygame.mouse.get_pos())
        #print(turn)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

def reset():
    loadVariables = [line.rstrip() for line in open('knucklebones new game.txt')]
    if int(loadVariables[0])>0:
        loadVariables[0]=int(loadVariables[0])-1;
        loadVariables[1]="";
        file = open('knucklebones new game.txt', 'w')
        for i in range (len(loadVariables)):
            file.write(f'{loadVariables[i]}\n')
        file.close()
        file = open('knucklebones player1.txt', 'w')
        for i in range (len(loadVariables)):
            file.write(f'{loadVariables[i]}\n')
        file.close()
        file = open('knucklebones player2.txt', 'w')
        for i in range (len(loadVariables)):
            file.write(f'{loadVariables[i]}\n')
        file.close()

    
main()

