import pygame
import random
from os import system
from recursos.funcao import calc_dist_prim_seg, calc_dist_terc_seg
pygame.init()
system("cls")
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255, 0, 0) 
azul = (0, 0, 255) 
amarelo = (255, 255, 0)
fundo = pygame.image.load("recursos/fundo.png")
finalCorrida = pygame.image.load("recursos/finalCorrida.png")
carro1 = pygame.image.load("recursos/carro1.png")
carro2 = pygame.image.load("recursos/carro2.png")
carro3 = pygame.image.load("recursos/carro3.png")
movXcar1 = 0
movXcar2 = 0
movXcar3 = 0
posYcar1 = 50
posYcar2 = 180
posYcar3 = 110
vitoria = pygame.mixer.Sound("recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("recursos/trilha.mp3")
pygame.mixer.music.play(-1) #looping
acabou = False
somDaVitoria = False
atualizaLogCorrida = 0
distancia1 = 0
distancia2 = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (movXcar1,posYcar1))
    tela.blit(carro2, (movXcar2,posYcar2))
    tela.blit(carro3, (movXcar3,posYcar3))
    
    if not acabou:
        movXcar1 = movXcar1 + random.randint(0,10)
        movXcar2 = movXcar2 + random.randint(0,10)
        movXcar3 = movXcar3 + random.randint(0,10)
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
    
    if movXcar3 > 1000:
        movXcar3 = 0
        posYcar3 = 410
    
    if atualizaLogCorrida == 13:
        distancia1 = calc_dist_prim_seg(movXcar1, movXcar2, movXcar3)
        distancia2 = calc_dist_terc_seg(movXcar1, movXcar2, movXcar3)
        atualizaLogCorrida = 0
    
    posicoes = [
        (movXcar1, "Vermelho"),
        (movXcar2, "Amarelo"),
        (movXcar3, "Azul")
    ]
    
    posicoes.sort(reverse=True, key=lambda x: x[0])
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    textoPrimeiro = fonte.render(f"1º Lugar: {posicoes[0][1]}", True, preto)
    textoSegundo = fonte.render(f"2º Lugar: {posicoes[1][1]}", True, branco)
    textoTerceiro = fonte.render(f"3º Lugar: {posicoes[2][1]}", True, branco)
    tela.blit(textoPrimeiro, (810, 0))
    tela.blit(textoSegundo, (810, 30))
    tela.blit(textoTerceiro, (810, 60))
    
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    textoDistancia1 = fonte.render(f"Distância do segundo lugar para o primeiro: {distancia1}pixels", True, preto)
    textoDistancia2 = fonte.render(f"Distância do terceiro lugar para o segundo: {distancia2}pixels", True, branco)
    tela.blit(textoDistancia1, (10, 570))
    tela.blit(textoDistancia2, (10, 545))
    atualizaLogCorrida = atualizaLogCorrida + 1
    
    fonte = pygame.font.Font("freesansbold.ttf", 60) #ttf é a fonte
    textoVermelho = fonte.render("Vermelho Ganhou!!!", True, vermelho)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, amarelo)
    textoAzul = fonte.render("Azul Ganhou!", True, azul)
    
    
    if acabou == True:
        tela.fill(branco)
        tela.blit(finalCorrida, (0, 0))
        
    if posYcar1 == 350 and movXcar1 >= 900 and movXcar1> movXcar2 and movXcar3:
        tela.blit(textoVermelho, (200,70))
        acabou = True
    
    elif posYcar2 == 480 and movXcar2 >= 900 and movXcar2 > movXcar1 and movXcar3:
        tela.blit(textoAmarelo, (200,70))
        acabou = True
    
    elif posYcar3 == 410 and movXcar3 >= 900 and movXcar3 > movXcar1 and  movXcar2:
        tela.blit(textoAzul, (200,70))
        acabou = True

    pygame.display.update()
    clock.tick(60)
pygame.quit()