import pygame
from ..estados import EstadoJuego
from config.configuracion import (
    VELOCIDAD_MOVIMIENTO, FUERZA_SALTO, GRAVEDAD,
    ANCHO_PANTALLA, ALTO_PANTALLA, ANCHO_HUEVO,
    ALTO_HUEVO, TIEMPO_INVULNERABILIDAD,
    TIEMPO_INVULNERABILIDAD_POWERUP
)

class Huevo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = ANCHO_HUEVO
        self.alto = ALTO_HUEVO
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = False
        self.grietas = 0
        self.invulnerable = False
        self.tiempo_invulnerable = 0
        self.aterrizaje_suave = False
        self.tiempo_aterrizaje_suave = 0

    def mover(self, direccion):
        self.vel_x = direccion * VELOCIDAD_MOVIMIENTO

    def saltar(self):
        if self.en_suelo:
            self.vel_y = FUERZA_SALTO
            self.en_suelo = False

    def recibir_daño(self):
        if not self.invulnerable:
            self.grietas += 1
            self.invulnerable = True
            self.tiempo_invulnerable = TIEMPO_INVULNERABILIDAD

    def aplicar_powerup(self, tipo_powerup):
        if tipo_powerup == "cascara":
            self.grietas = max(0, self.grietas - 1)
        elif tipo_powerup == "papel":
            self.invulnerable = True
            self.tiempo_invulnerable = TIEMPO_INVULNERABILIDAD_POWERUP
        elif tipo_powerup == "turbo":
            self.vel_x *= 1.5
            self.invulnerable = True
            self.tiempo_invulnerable = TIEMPO_INVULNERABILIDAD_POWERUP

    def actualizar(self, plataformas, nivel_actual=None):

        if not self.en_suelo:
            if nivel_actual == 3:
                tiempo = pygame.time.get_ticks() // 2000
                if tiempo % 2 == 0:
                    self.vel_y -= GRAVEDAD
                else:
                    self.vel_y += GRAVEDAD
            else:
                self.vel_y += GRAVEDAD

        self.x += self.vel_x
        self.y += self.vel_y

        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO_PANTALLA - self.ancho:
            self.x = ANCHO_PANTALLA - self.ancho

        self.en_suelo = False
        self.rect.x = self.x
        self.rect.y = self.y

        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.vel_y > 0 and self.rect.bottom > plataforma.rect.top and self.rect.top < plataforma.rect.top:
                    self.y = plataforma.rect.top - self.alto
                    self.vel_y = 0
                    self.en_suelo = True

        if self.invulnerable:
            self.tiempo_invulnerable -= 1
            if self.tiempo_invulnerable <= 0:
                self.invulnerable = False

        if self.aterrizaje_suave:
            self.tiempo_aterrizaje_suave -= 1
            if self.tiempo_aterrizaje_suave <= 0:
                self.aterrizaje_suave = False