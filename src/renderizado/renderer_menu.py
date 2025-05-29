import pygame
from config.configuracion import *

class RendererMenu:
    def __init__(self):
        pass

    def dibujar_menu_principal(self, pantalla):
        pantalla.fill((50, 50, 50))
        fuente_titulo = pygame.font.SysFont(None, 48)
        titulo = fuente_titulo.render("HUEVOS A LA FUGA", True, AMARILLO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 200))
        
        fuente_instrucciones = pygame.font.SysFont(None, 28)
        instruccion1 = fuente_instrucciones.render("Presiona ENTER para comenzar", True, VERDE)
        instruccion2 = fuente_instrucciones.render("Presiona P para ver puntuaciones", True, AZUL_CLARO)
        
        pantalla.blit(instruccion1, (ANCHO_PANTALLA//2 - instruccion1.get_width()//2, 350))
        pantalla.blit(instruccion2, (ANCHO_PANTALLA//2 - instruccion2.get_width()//2, 400))

    def dibujar_tabla_puntuaciones(self, pantalla, puntuaciones):
        pantalla.fill((30, 30, 30))
        fuente_titulo = pygame.font.SysFont(None, 36)
        titulo = fuente_titulo.render("MEJORES PUNTUACIONES", True, BLANCO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 50))
        
        fuente_lista = pygame.font.SysFont(None, 24)
        
        if not puntuaciones:
            mensaje = fuente_lista.render("No hay puntuaciones registradas", True, ROJO)
            pantalla.blit(mensaje, (ANCHO_PANTALLA//2 - mensaje.get_width()//2, 200))
        else:
            for i, p in enumerate(puntuaciones[:10]):
                y_pos = 120 + i * 30
                texto = fuente_lista.render(f"{i+1}. {p['nombre']} - Nivel {p['nivel']} - {p['tiempo']}s", True, BLANCO)
                pantalla.blit(texto, (50, y_pos))
        
        fuente_volver = pygame.font.SysFont(None, 24)
        volver = fuente_volver.render("Presiona P para volver", True, AZUL_CLARO)
        pantalla.blit(volver, (ANCHO_PANTALLA//2 - volver.get_width()//2, ALTO_PANTALLA - 50))

    def dibujar_menu_pausa(self, pantalla):
        overlay = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        
        fuente_titulo = pygame.font.SysFont(None, 48)
        titulo = fuente_titulo.render("PAUSA", True, BLANCO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 250))
        
        fuente_opciones = pygame.font.SysFont(None, 24)
        opcion1 = fuente_opciones.render("ESC - Continuar", True, VERDE)
        opcion2 = fuente_opciones.render("Q - Salir al menú", True, ROJO)
        
        pantalla.blit(opcion1, (ANCHO_PANTALLA//2 - opcion1.get_width()//2, 320))
        pantalla.blit(opcion2, (ANCHO_PANTALLA//2 - opcion2.get_width()//2, 360))

    def dibujar_game_over(self, pantalla, nivel_actual):
        pantalla.fill((50, 0, 0))
        fuente_titulo = pygame.font.SysFont(None, 60)
        titulo = fuente_titulo.render("¡HUEVO ROTO!", True, ROJO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 200))
        
        fuente_info = pygame.font.SysFont(None, 32)
        info_nivel = fuente_info.render(f"Llegaste al nivel {nivel_actual}", True, BLANCO)
        pantalla.blit(info_nivel, (ANCHO_PANTALLA//2 - info_nivel.get_width()//2, 300))
        
        fuente_instruccion = pygame.font.SysFont(None, 28)
        instruccion = fuente_instruccion.render("Presiona ENTER para volver al menú", True, AMARILLO)
        pantalla.blit(instruccion, (ANCHO_PANTALLA//2 - instruccion.get_width()//2, 400))

    def dibujar_victoria(self, pantalla, tiempo_transcurrido):
        pantalla.fill((0, 50, 0))
        fuente_titulo = pygame.font.SysFont(None, 60)
        titulo = fuente_titulo.render("¡VICTORIA!", True, VERDE)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 150))
        
        fuente_subtitulo = pygame.font.SysFont(None, 32)
        subtitulo = fuente_subtitulo.render("¡El huevo ha escapado de la cocina!", True, BLANCO)
        pantalla.blit(subtitulo, (ANCHO_PANTALLA//2 - subtitulo.get_width()//2, 220))
        
        fuente_tiempo = pygame.font.SysFont(None, 36)
        info_tiempo = fuente_tiempo.render(f"Tiempo total: {tiempo_transcurrido} segundos", True, AMARILLO)
        pantalla.blit(info_tiempo, (ANCHO_PANTALLA//2 - info_tiempo.get_width()//2, 300))
        
        fuente_instruccion = pygame.font.SysFont(None, 28)
        instruccion = fuente_instruccion.render("Presiona ENTER para volver al menú", True, BLANCO)
        pantalla.blit(instruccion, (ANCHO_PANTALLA//2 - instruccion.get_width()//2, 400)) 