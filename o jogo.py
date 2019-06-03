import pygame
pygame.init()

tela_w = 600
tela_h = 600
tela = pygame.display.set_mode((tela_w,tela_h)) # set tela + tamanho dela
pygame.display.set_caption('O Jogo') # nome da barrinha
clock = pygame.time.Clock() #set time


# images
parado = pygame.image.load('images/player.png')
bg = pygame.image.load('images/bg.png')

# set posicao inicial do player
x = 30
y = 540
# set tamanho/velocidade do personagem
width = 30
height = 30
velocidade = 15
# posicao player
left = False
right = False
cont = 0

# tempo = pygame.time.Clock() #funcao que define tempo 

def redrawGameWindow(): #funcao pra set imagens
    global count
     
    tela.blit(bg, (0,0)) # set imagem de fundo do level
    pygame.draw.rect(tela, (255,0,0), (x, y, width, height))  # player
    pygame.display.update() # update da tela
    clock.tick(60) #fps




run = True

while run:
    pygame.time.delay(35) # deleio baseado em milisegundos

    for event in pygame.event.get():  # loop para verificar cada evento do mouse ou teclado
        if event.type == pygame.QUIT: # verifica se o jogo foi fechado
            run = False

    teclas = pygame.key.get_pressed() # funcao que verifica se alguma tecla foi pressionada e faz o player andar conforme a tecla pressionada
    
    if teclas[pygame.K_LEFT] and x > velocidade:
        x -= velocidade
        left = True
        right = False
        front = False
        back = False

    if teclas[pygame.K_RIGHT] and x < 500 - velocidade - width:
        x += velocidade
        left = False
        right = True
        front = False
        back = False

    tela.fill((0,0,0))  # reseta a tela para nao ficar marcado o percurso do player
    pygame.display.update() # faz um update da do codigo para a tela
    redrawGameWindow() 



    
pygame.quit()  # se o while for encerrado o jogo vai ser fechado
