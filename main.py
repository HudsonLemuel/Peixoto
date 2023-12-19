import os, sys


dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import random
import pygame, sys

x=1280
y=700


class Bilbo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/bilbo.png").convert_alpha()
        #self.image = pygame.transform.smoothscale(self.image, (500, 200))
        self.rect = self.image.get_rect(center=(largura/2,autura/2))
        self.mask = pygame.mask.from_surface(self.image)


        self.listadisparo = []
        self.vida = True
        self.velocidade = 7

        self.y = 300
        self.x = 200

    def disparar(self, x, y):
        minhabala = Bala(x,y)
        self.listadisparo.append(minhabala)

    def criar_bala(self):
        return Bala(self.rect.centerx, self.rect.centery)

class Bala(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("data/blhoa.png").convert_alpha()
        #self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += 5

        if self.rect.x >= largura + 20:
            self.kill()

class Lixo(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y, velocidade, nivel):
        super().__init__()
        if nivel ==1:
            self.image = pygame.image.load('data/lixo1.png').convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (100, 100))
        elif nivel == 2:
            self.image = pygame.image.load('data/lixin2.png').convert_alpha()
        else :
            self.image = pygame.image.load('data/lixo3.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.listadisparo = []
        self.velocidadelixo = velocidade


    def update(self):
        self.rect.x -= self.velocidadelixo





pygame.init()
tempo = pygame.time.Clock()
largura,autura= 1280,700
tela = pygame.display.set_mode((largura, autura))
tela_png = pygame.image.load("data/fundinhopp.png").convert_alpha()
pygame.display.set_caption('PEIXOTO')
pygame.mouse.set_visible(True)


nivel = 1
quantidade_por_nivel = 5
tempo_ate_nascerlixo = 10
vitoria = False

bala_grupo = pygame.sprite.Group()
grupo_lixo = pygame.sprite.Group()



pontos = 0
vida = 3

tempo_spaw = 0

font = pygame.font.SysFont('data/fast99.ttf', 50)

screem = pygame.image.load('data/menuzin.png')

vida = 3


def respawn():
    x = 1350
    y = random.randint(1, 640)
    return[x,y]

pp1 = pygame.image.load("data/image level 2.png")
pp2 = pygame.image.load("data/image level 3.png")

fim = pygame.image.load("data/cena final de bilbo e anya.png").convert_alpha()
fim= pygame.transform.smoothscale(fim, (1280, 700))

regras = pygame.image.load("data/regras.png").convert_alpha()
regras= pygame.transform.smoothscale(regras, (1280, 700))




fundo_interface = pygame.image.load('data/menuzin.PNG').convert_alpha()
fundo_interface = pygame.transform.smoothscale(fundo_interface, (1280, 700))

jogando = True
jogar = True
sair = True

while jogando:
    while jogar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                jogar = False
                vitoria = False
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    jogar = False
                    regrinhas = True

        tela.blit(fundo_interface,(0,0))
        pygame.display.update()

    while regrinhas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                sair = False
                vitoria = False
                regrinhas = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regrinhas = False
                    sair = True
        tela.blit(regras, (0, 0))
        pygame.display.update()

    bilbo = Bilbo()
    bilbo_grupo = pygame.sprite.Group()
    bilbo_grupo.add(bilbo)

    bilboy = bilbo.y
    bilbox = bilbo.x

    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                sair = False
                vitoria = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bala_grupo.add(bilbo.criar_bala())

        if quantidade_por_nivel:
            if tempo_spaw >= tempo_ate_nascerlixo:
                respaw = respawn()
                lixo = Lixo(respaw[0], respaw[1], random.randint(3, 5),nivel)
                lixo.add(grupo_lixo)
                tempo_spaw = 0
                quantidade_por_nivel -= 1
            else:
                tempo_spaw += 0.10
        else:
            if not grupo_lixo:
                nivel += 1
                if nivel == 2:
                    niver_2 = True
                    while niver_2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                jogando = False
                                sair = False
                                vitoria = False
                                niver_2 = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    niver_2 = False
                        tela.blit(pp1, (0, 0))
                        pygame.display.update()
                        quantidade_por_nivel = 10
                        tempo_ate_nascerlixo = 8
                        tela_png = pygame.image.load('data/pano 1 completo.png').convert_alpha()
                elif nivel == 3:
                    niver_3 = True
                    while niver_3:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                jogando = False
                                sair = False
                                vitoria = False
                                niver_3 = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    niver_3 = False
                        tela.blit(pp2, (0, 0))
                        pygame.display.update()
                        quantidade_por_nivel = 15
                        tempo_ate_nascerlixo = 6
                        tela_png = pygame.image.load('data/pao2.png').convert_alpha()

                else:
                    if pontos == 30:
                        vitoria = True
                        sair= False




        colisao_bala = pygame.sprite.groupcollide(
            bala_grupo, grupo_lixo, True, True, pygame.sprite.collide_mask
        )
        colisao_bilbo = pygame.sprite.spritecollide(
            bilbo, grupo_lixo, False, pygame.sprite.collide_mask
        )

        if colisao_bala:
            pontos += 1

        if colisao_bilbo:
            vida -= 1
            lixo = colisao_bilbo[0]
            lixo.rect.x = 1300

        tela.blit(tela_png,(0,0))

        #tela andando
        part_x = x % tela_png.get_rect().width
        tela.blit(tela_png, (part_x - tela_png.get_rect().width,0))
        if part_x <1280:
            tela.blit(tela_png, (part_x, 0))

        #jkl
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            bilboy -= bilbo.velocidade
        if keys[pygame.K_s]:
            bilboy += bilbo.velocidade
        if keys[pygame.K_d]:
            bilbox += bilbo.velocidade
        if keys[pygame.K_a]:
            bilbox -= bilbo.velocidade

        for lixo in grupo_lixo:

            for lixo in grupo_lixo:
                if lixo.rect.x <= -30:
                    grupo_lixo.remove(lixo)
                    vida -= 3
            if vida == 0 or vida == -1 or vida == -2 or vida == -3:
                grupo_lixo.remove(grupo_lixo)
                bala_grupo.remove(bala_grupo)
                nivel = 1
                vida = 3
                pontos = 0
                quantidade_por_nivel = 5
                tela_png = pygame.image.load('data/fundinhopp.png').convert_alpha()
                tempo_ate_nascerlixo = 10
                jogar = True
                sair = False



        #posção dos rects
        bilbo.rect.y = bilboy
        bilbo.rect.x = bilbox

        #movimento
        x-=2

        bala_grupo.draw(tela)
        grupo_lixo.draw(tela)
        tela.blit(bilbo.image, (bilbox, bilboy))

        life = font.render(f' Vida: {int(vida)} ', True, (255, 0, 0))
        tela.blit(life, (1100, 50))

        score = font.render(f' Pontos: {int(pontos)} ', True, (255,255,255))
        tela.blit(score, (50,50))



        bilbo_grupo.update()
        bala_grupo.update()
        grupo_lixo.update()
        pygame.display.flip()
        tempo.tick(60)
        pygame.display.update()

    while vitoria:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                sair = False
                vitoria = False

        tela.blit(fim, (0, 0))
        pygame.display.update()

