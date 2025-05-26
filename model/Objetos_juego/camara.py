import pygame
from config.configuracion import ANCHO_PANTALLA, ALTO_PANTALLA


class Camara:
    def _init_(self, ancho_nivel):
        self.desplazamiento = 0
        self.ancho_nivel = ancho_nivel
        self.limite_derecho = ancho_nivel - ANCHO_PANTALLA
        if self.limite_derecho < 0:
            self.limite_derecho = 0

    def actualizar(self, huevo):
        x_relativa = huevo.x - self.desplazamiento

        if x_relativa > ANCHO_PANTALLA * 0.66 and self.desplazamiento < self.limite_derecho:
            desplazamiento_deseado = min(huevo.x - (ANCHO_PANTALLA * 0.5), self.limite_derecho)
            self.desplazamiento += (desplazamiento_deseado - self.desplazamiento) * 0.1
            if self.desplazamiento > self.limite_derecho:
                self.desplazamiento = self.limite_derecho

        elif x_relativa < ANCHO_PANTALLA * 0.33 and self.desplazamiento > 0:
            desplazamiento_deseado = max(huevo.x - (ANCHO_PANTALLA * 0.33), 0)
            self.desplazamiento += (desplazamiento_deseado - self.desplazamiento) * 0.1
            if self.desplazamiento < 0:
                self.desplazamiento = 0

    def aplicar(self, rect):
        return pygame.Rect(rect.x - self.desplazamiento, rect.y, rect.width, rect.height)

    def posicion_mundial_a_pantalla(self, x, y):
        return x - self.desplazamiento, y

    def posicion_pantalla_a_mundial(self, x, y):
        return x + self.desplazamiento, y