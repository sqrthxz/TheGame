import pygame, sys, os, ctypes
from pygame.locals import *


#set tamanho da tela do jogo
largura = 400
altura = 600
setTop = 20

# -------------------------------------- INIMIGOS ------------------------------------

class Enemy1(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/enemy1.png")
        self.rect = self.ImageEnemy.get_rect()
        
        self.rect.top = posy
        self.rect.left = posx
        
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy2.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie): 
        superficie.blit(self.ImageEnemy, self.rect)
        
class Enemy3(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy3.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie): #coloca img na tela
        superficie.blit(self.ImageEnemy, self.rect)
        
class Enemy4(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy4.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)
 

# ------------------------------------------------------------------------------------



class Bala(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load("images/laser.png")
        self.rect = self.ImagemBala.get_rect()
        self.teste = self.ImagemBala.get_rect()
        self.velocidadeBala = 10
        self.rect.top = posy
        self.rect.left = posx
        

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala
        
    def colocar(self,superficie): #coloca img na tela
        superficie.blit(self.ImagemBala, self.rect)



#----------------------------------------------------
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("images/player.png")

        self.rect = self.ImagemNave.get_rect()
        #set posicao inicial
        self.rect.centerx = largura/2
        self.rect.centery = altura - 55
        self.listaDisparo = [] #onde add bullets
        self.vida = True
        self.velocidade= 70 #vel de mov player
        
    def movimento(self): #set limite do movimento do player
        if self.vida == True:
            if self.rect.left < 4: #esquerda
                self.rect.left = 4
            elif self.rect.right > 395: #direita
                self.rect.right = 395
                
    def disparar(self, x, y): #set dispara o projetil
        minhaBala = Bala(x,y)
        self.listaDisparo.append(minhaBala)

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)

def invasaoEspaco():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))#tamanho da tela
    pygame.display.set_caption("Skyway")
    cont = 0
    jogador = player()
    bala = Bala(largura /2, altura - 55)
    enemy1 = Enemy3(40,20)
    enemy2 = Enemy2(130,20)
    enemy3 = Enemy4(220,20)
    enemy4 = Enemy1(310,20)
    enemy5 = Enemy4(85,90)
    enemy6 = Enemy3(177,90)
    enemy7 = Enemy1(269,90)
    enemy8 = Enemy2(40,160)
    enemy9 = Enemy3(130,160)
    enemy10 = Enemy1(220,160)
    enemy11 = Enemy4(310,160)


    
    jogando = True
    bg = pygame.image.load("images/bg.png")
    relogio = pygame.time.Clock()

    def win():
        if cont == 11 and len(jogador.listaDisparo) >= 1:
            ctypes.windll.user32.MessageBoxW(0, "You win!", "Congrats!", 1)
            pygame.quit()
        
    while True:
        
        relogio.tick(60) #fps
        jogador.movimento()
        

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN: #pega tecla pressionada
                if event.key == K_LEFT :
                    jogador.rect.left -= jogador.velocidade
                if event.key== K_RIGHT:
                    jogador.rect.right += jogador.velocidade
                if event.key== K_SPACE:
                    x,y= jogador.rect.center
                    jogador.disparar(x-13,y-50)
        
        
        bala.trajetoria()            
        tela.blit(bg,(0,0))
        
        jogador.colocar(tela)
        
        enemy1.put(tela)
        enemy2.put(tela)
        enemy3.put(tela)
        enemy4.put(tela)
        enemy5.put(tela)
        enemy6.put(tela)
        enemy7.put(tela)
        enemy8.put(tela)
        enemy9.put(tela)
        enemy10.put(tela)
        enemy11.put(tela)
        
        #att a tela apos disparo
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.colliderect(enemy1.rect):
                    enemy1 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1
                    
                elif x.rect.colliderect(enemy2.rect):
                    enemy2 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1
                    
                elif x.rect.colliderect(enemy3.rect):
                    enemy3 = Enemy2(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy4.rect):
                    enemy4 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy5.rect):
                    enemy5 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy6.rect):
                    enemy6 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy7.rect):
                    enemy7 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1
  
                elif x.rect.colliderect(enemy8.rect):
                    enemy8 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy9.rect):
                    enemy9 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy10.rect):
                    enemy10 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1

                elif x.rect.colliderect(enemy11.rect):
                    enemy11 = Enemy1(500,0)
                    jogador.listaDisparo.remove(x)
                    cont += 1
                    
                elif x.rect.top < -10:
                    jogador.listaDisparo.remove(x)
        win()
        pygame.display.update()
        

invasaoEspaco()
