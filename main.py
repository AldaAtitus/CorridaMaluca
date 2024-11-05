import pygame
import random
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("recursos/fundo.png")
carro1 = pygame.image.load("recursos/carro1.png")
carro2 = pygame.image.load("recursos/carro2.png")
movXcar1 = 0
movXcar2 = 0
posYcar1 = 50
posYcar2 = 180
vitoria = pygame.mixer.Sound("recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("recursos/trilha.mp3")
pygame.mixer.music.play(-1) #looping
acabou = False
somDaVitoria = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    
    tela.fill(branco)
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXcar1,posYcar1))
    tela.blit(carro2, (movXcar2,posYcar2))
    
    if not acabou:
        movXcar1 = movXcar1 + random.randint(0,10)
        movXcar2 = movXcar2 + random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
    
    if movXcar1 > 1000:
        movXcar1 = 0
        posYcar1 = 350
    
    if movXcar2 > 1000:
        movXcar2 = 0
        posYcar2 = 480
        
    fonte = pygame.font.Font("freesansbold.ttf", 60) #ttf é a fonte
    textoVermelho = fonte.render("Vermelho Ganhou!!!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    
    if posYcar1 == 350 and movXcar1 >= 900 and movXcar1>movXcar2:
        tela.blit(textoVermelho, (270,70))
        acabou = True

        
    elif posYcar2 == 480 and movXcar2 >= 900 and movXcar2 > movXcar1:
        tela.blit(textoAmarelo, (270,180))
        acabou = True

    
    pygame.display.update()
    clock.tick(60)
pygame.quit()