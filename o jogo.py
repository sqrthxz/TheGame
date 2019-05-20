import pygame
pygame.init()

tela = pygame.display.set_mode((500,500)) # set tela + tamanho dela
pygame.display.set_caption('O Jogo') # nome da barrinha

# images
parado = pygame.image.load('images/parado.png')
bg = pygame.image.load('images/bg.png')

# set posicao inicial do player
x = 50
y = 50
# set tamanho/velocidade do personagem
width = 30
height = 30
velocidade = 7
# posicao player
left = False
right = False
front = False
back = False
cont = 0

# tempo = pygame.time.Clock() #funcao que define tempo 

def redrawGameWindow(): #funcao pra set imagens
    global count
     
    tela.blit(bg, (0,0)) # set imagem de fundo do level
    pygame.draw.rect(tela, (255,0,0), (x, y, width, height))  # player
    pygame.display.update() # update da tela




run = True

while run:
    pygame.time.delay(50) # deleio baseado em milisegundos

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

    if teclas[pygame.K_UP] and y > velocidade:
        y -= velocidade
        left = False
        right = False
        front = False
        back = True
        
    if teclas[pygame.K_DOWN] and y < 500 - velocidade - width:
        y += velocidade
        left = False
        right = False
        front = True
        back = False

    tela.fill((0,0,0))  # reseta a tela para nao ficar marcado o percurso do player
    pygame.display.update() # faz um update da do codigo para a tela
    redrawGameWindow() 



    
pygame.quit()  # se o while for encerrado o jogo vai ser fechado
