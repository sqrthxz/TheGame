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


class BOSS(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/boss.png")
        self.rect = self.ImageEnemy.get_rect()

        self.rect.top = posy
        self.rect.left = posx

    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

class BOSS2(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/boss2.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)
# ------------------------------------------------------------------------------------
class BalaB(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/laser.png")
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)
#------------------------------------------------------------------------------------
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
#-------------------------------------------------------

#-------------------------------------------------------
def invasaoEspaco():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))#tamanho da tela
    pygame.display.set_caption("Skyway")
    cont = 0

    e1= 20
    e2= 20
    e3= 20
    e4= 20
    e5= 90
    e6= 90
    e7= 90
    e8= 160
    e9= 160
    e10= 160
    e11= 160
    con= 0.10

    boss = BOSS(-100,-100)
    bp= 0
    bm= 135
    le= 1


    dc= 1
    dd= 1
    de= 1
    fechar= 1

    lado1=40
    lado2=130
    lado3=220
    lado4=310
    lado5=85
    lado6=177
    lado7=269
    lado8=40
    lado9=130
    lado10=220
    lado11=310
    ganhar= 0
    p= 475 #pos para perder

    jogador = player()

    bala = Bala(largura /2, altura - 55)

    bC=0
    bA=bp+166
    damage = 0

    menucount=0
    menu=0
#----------------------------------------------------------
    vitoria = pygame.image.load("images/vitoria.png")
    bg = pygame.image.load("images/bg.png")
    menu1= pygame.image.load("images/menu1.png")
    menu2=pygame.image.load("images/menu2.png")
    derrota= pygame.image.load('images/Derrota.png')

#----------------------------------------------------------
    relogio = pygame.time.Clock()

    while menu==0:
        relogio.tick(60)
        if menucount==0:
            tela.blit(menu1,(0,0))
            pygame.display.update()






        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == K_DOWN :
                    tela.blit(menu2,(0,0))
                    pygame.display.update()
                    menucount=1
                if event.key==K_UP:
                    menucount=0
                if event.key==K_RIGHT and menucount==0:
                    menu=1
                if event.key==K_RIGHT and menucount==1:
                    pygame.quit()
                    sys.exit()
    while menu==1:

        relogio.tick(60) #fps
        jogador.movimento()


        #-------------posicao dos inimigos------------
        enemy1 = Enemy3(lado1,e1)
        enemy2 = Enemy2(lado2,e2)
        enemy3 = Enemy4(lado3,e3)
        enemy4 = Enemy1(lado4,e4)
        enemy5 = Enemy4(lado5,e5)
        enemy6 = Enemy3(lado6,e6)
        enemy7 = Enemy1(lado7,e7)
        enemy8 = Enemy2(lado8,e8)
        enemy9 = Enemy3(lado9,e9)
        enemy10 = Enemy1(lado10,e10)
        enemy11 = Enemy4(lado11,e11)

        e1+=con
        e2+=con
        e3+=con
        e4+=con
        e5+=con
        e6+=con
        e7+=con
        e8+=con
        e9+=con
        e10+=con
        e11+=con

        #------------------------------------------------
        parede1 = Enemy4(-25,120)
        parede2 = Enemy4(375,120)
        #-----------------------------------------------
        bL=bm+62
        tiro = BalaB(bL,bA)


        #-----------------------------------------------

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

        if cont == 11:
            boss = BOSS(bm,bp)
            boss.put(tela)
            bp+=dc

            if bp>70:
                dc=0
                bm+=le
                tiro.put(tela)
                boss.put(tela)

                if boss.rect.colliderect(parede2.rect):
                    le=-1
                if boss.rect.colliderect(parede1.rect):
                    le=1

                bC+=1
                if bC>5:
                    bA+=7 #velocidade da bala do boss
                    if bA>600:
                        bC=0
                        bA=bp+50
                if tiro.rect.colliderect(jogador.rect):
                    damage+=1
                    bA=100





        if ganhar >= 11:
            tela.blit(vitoria,(0,0))
            jogador.colocar(tela)
            bm= 5000
            bp= 5000
            fechar +=1

            if fechar >= 100:
                pygame.quit()

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
#-------------------------------

#------------------------------

        #att a tela apos disparo
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.colliderect(enemy1.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e1= -10000
                    lado1= 500
                    con+=0.30

                elif x.rect.colliderect(enemy2.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e2= -10000
                    lado2= 500
                    con+=0.30

                elif x.rect.colliderect(enemy3.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e3= -10000
                    lado3= 500
                    con+=0.30

                elif x.rect.colliderect(enemy4.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e4= -10000
                    lado4= 500
                    con+=0.30


                elif x.rect.colliderect(enemy5.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e5= -10000
                    lado5= 500
                    con+=0.30


                elif x.rect.colliderect(enemy6.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e6= -10000
                    lado6= 500
                    con+=0.30


                elif x.rect.colliderect(enemy7.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e7= -10000
                    lado7= 500
                    con+=0.30

                elif x.rect.colliderect(enemy8.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    lado8= 500
                    e8= -10000
                    con+=0.30


                elif x.rect.colliderect(enemy9.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e9= -10000
                    lado9= 500
                    con+=0.30


                elif x.rect.colliderect(enemy10.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e10= -10000
                    lado10= 500
                    con+=0.30


                elif x.rect.colliderect(enemy11.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e11= -10000
                    lado11= 500
                    con+=0.30

                elif x.rect.top < -10:
                    jogador.listaDisparo.remove(x)

                elif cont>=11:
                    if x.rect.colliderect(boss.rect):
                        boss2 = BOSS2(bm,bp)
                        boss2.put(tela)

                        jogador.listaDisparo.remove(x)
                        ganhar+=1

        if damage>2 or e1 > p  or e2 > p or e3 > p or e4 > p or e5 > p or e6 > p or e7> p or e8 > p or e9 > p or e10 > p or e11 > p:
            tela.blit(derrota,(0,0))
            fechar+=1
            if fechar>100:
                pygame.quit()

        pygame.display.update()
        parede1.put(tela)
        parede2.put(tela)

invasaoEspaco()
