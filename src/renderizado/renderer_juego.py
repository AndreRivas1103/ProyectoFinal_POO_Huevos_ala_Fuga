import pygame
from config.configuracion import *
from .renderer_huevo import RendererHuevo

class RendererJuego:
    def __init__(self):
        self.renderer_huevo = RendererHuevo()

    def dibujar_plataformas(self, pantalla, plataformas):
        for plataforma in plataformas:
            pygame.draw.rect(pantalla, AZUL, plataforma.rect)

    def dibujar_obstaculos(self, pantalla, obstaculos):
        for obstaculo in obstaculos:
            if obstaculo.tipo == "sarten":
                pygame.draw.rect(pantalla, ROJO, obstaculo.rect)
            elif obstaculo.tipo == "aceite":
                pygame.draw.rect(pantalla, AMARILLO, obstaculo.rect)

    def dibujar_powerups(self, pantalla, powerups):
        for powerup in powerups:
            if powerup.activo:
                pygame.draw.rect(pantalla, powerup.color, powerup.rect)

    def dibujar_meta(self, pantalla, meta):
        pygame.draw.rect(pantalla, VERDE, meta)
        fuente_meta = pygame.font.SysFont(None, 24)
        texto_meta = fuente_meta.render("META", True, BLANCO)
        pantalla.blit(texto_meta, (meta.x - 20, meta.y - 30))

    def dibujar_info_juego(self, pantalla, huevo, nivel_actual, tiempo_transcurrido):
        fuente = pygame.font.SysFont(None, 24)
        info_grietas = fuente.render(f"Grietas: {huevo.grietas}/{MAX_GRIETAS}", True, BLANCO)
        info_nivel = fuente.render(f"Nivel: {nivel_actual}", True, BLANCO)
        info_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido}s", True, BLANCO)
        
        pantalla.blit(info_grietas, (10, 10))
        pantalla.blit(info_nivel, (10, 40))
        pantalla.blit(info_tiempo, (10, 70))

    def dibujar_nivel_completo(self, pantalla, plataformas, obstaculos, powerups, meta, huevo, nivel_actual, tiempo_transcurrido):
        self.dibujar_plataformas(pantalla, plataformas)
        self.dibujar_obstaculos(pantalla, obstaculos)
        self.dibujar_powerups(pantalla, powerups)
        self.dibujar_meta(pantalla, meta)
        self.renderer_huevo.dibujar_huevo(pantalla, huevo)
        self.dibujar_info_juego(pantalla, huevo, nivel_actual, tiempo_transcurrido) 