import pygame, sys
from pygame.locals import *

largura= 850
altura= 400

class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load("L11E.png")

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala
    def colocar(self,superficie):
        superficie.blit(self.ImagemBala, self.rect)

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("stop.png")

        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura - 50

        self.listaDisparo = []
        self.vida = True
        self.velocidade= 20


    
        
    def movimento(self):
        if self.vida == True:
            if self.rect.left <=0:
                self.rect.left =0
            elif self.rect.right > largura:
                self.rect.right = largura
    
    def disparar(self,x,y):
        minhaBala= Bala(x,y)
        self.listaDisparo.append(minhaBala)
        

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)




def invasaoEspaco():
    pygame.init()
    tela= pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("xd")
    jogador = naveEspacial()
    jogando = True
    bg= pygame.image.load("bg.jpg")
    balaProjetil = Bala(largura /2, altura - 50)
    relogio = pygame.time.Clock()
    while True:
        relogio.tick(60)
        jogador.movimento()
        balaProjetil.trajetoria()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key == K_LEFT :
                    jogador.rect.left -= jogador.velocidade

                if event.key== K_RIGHT:
                    jogador.rect.right += jogador.velocidade
                if event.key== K_SPACE:
                    x,y= jogador.rect.center
                    jogador.disparar(x-45,y-50)
                    
                
        tela.blit(bg, (0,0))    
        
        jogador.colocar(tela)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.listaDisparo.remove(x)
        pygame.display.update()

invasaoEspaco()
