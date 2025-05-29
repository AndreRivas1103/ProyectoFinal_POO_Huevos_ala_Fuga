import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.objetos_juego import Huevo, Camara
from model.estados import EstadoJuego
from src.logica.gestor_niveles import GestorNiveles
from src.ui.render import Render
from src.utils.puntuaciones import Puntuaciones
from config.configuracion import *

def inicializar_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Huevos a la Fuga")
    reloj = pygame.time.Clock()
    return pantalla, reloj

def juego():
    pantalla, reloj = inicializar_pygame()
    
    # Instanciar las clases
    gestor_niveles = GestorNiveles()
    render = Render()
    puntuaciones_manager = Puntuaciones()
    
    estado_actual = EstadoJuego.MENU
    nivel_actual = 1
    tiempo_inicio = 0
    tiempo_transcurrido = 0
    
    # Variables para entrada de nombre
    nombre_actual = ""
    cursor_visible = True
    ultimo_cambio_cursor = 0
    
    # Variables para mostrar puntuaciones
    mostrar_puntuaciones = False
    puntuaciones = []
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            
            if estado_actual == EstadoJuego.MENU:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        estado_actual = EstadoJuego.INGRESO_NOMBRE
                        nombre_actual = ""
                    elif evento.key == pygame.K_p:
                        mostrar_puntuaciones = not mostrar_puntuaciones
                        if mostrar_puntuaciones:
                            puntuaciones = puntuaciones_manager.cargar_puntuaciones()
            
            elif estado_actual == EstadoJuego.INGRESO_NOMBRE:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if nombre_actual.strip():
                            estado_actual = EstadoJuego.JUGANDO
                            nivel_actual = 1
                            tiempo_inicio = pygame.time.get_ticks()
                            plataformas, obstaculos, powerups, meta, ancho_nivel = gestor_niveles.cargar_nivel(nivel_actual)
                            huevo = Huevo(50, ALTO_PANTALLA - 150)
                            camara = Camara(ancho_nivel)
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre_actual = nombre_actual[:-1]
                    elif evento.key == pygame.K_ESCAPE:
                        estado_actual = EstadoJuego.MENU
                    elif evento.key not in [pygame.K_TAB]:
                        if len(nombre_actual) < 15:
                            char = evento.unicode
                            if char.isprintable():
                                nombre_actual += char
            
            elif estado_actual == EstadoJuego.JUGANDO:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                        huevo.saltar()
                    elif evento.key == pygame.K_ESCAPE:
                        estado_actual = EstadoJuego.PAUSA
            
            elif estado_actual == EstadoJuego.PAUSA:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        estado_actual = EstadoJuego.JUGANDO
                    elif evento.key == pygame.K_q:
                        estado_actual = EstadoJuego.MENU
                        nivel_actual = 1
                        tiempo_transcurrido = 0
                        nombre_actual = ""
                        mostrar_puntuaciones = False
                        plataformas, obstaculos, powerups, meta, ancho_nivel = gestor_niveles.cargar_nivel(nivel_actual)
                        huevo = Huevo(50, ALTO_PANTALLA - 150)
                        camara = Camara(ancho_nivel)
            
            elif estado_actual == EstadoJuego.GAME_OVER or estado_actual == EstadoJuego.VICTORIA:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        estado_actual = EstadoJuego.MENU
                        nivel_actual = 1
                        tiempo_transcurrido = 0
                        nombre_actual = ""
                        mostrar_puntuaciones = False
                        plataformas, obstaculos, powerups, meta, ancho_nivel = gestor_niveles.cargar_nivel(nivel_actual)
                        huevo = Huevo(50, ALTO_PANTALLA - 150)
                        camara = Camara(ancho_nivel)
        
        # Actualizar cursor para ingreso de nombre
        if estado_actual == EstadoJuego.INGRESO_NOMBRE:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - ultimo_cambio_cursor > 500:
                cursor_visible = not cursor_visible
                ultimo_cambio_cursor = tiempo_actual
        
        # Actualizar lógica del juego
        if estado_actual == EstadoJuego.JUGANDO:
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000
            
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                huevo.mover_izquierda()
            if teclas[pygame.K_RIGHT]:
                huevo.mover_derecha()
            
            huevo.actualizar(plataformas, obstaculos, powerups)
            camara.seguir_huevo(huevo)
            
            for powerup in powerups:
                powerup.actualizar()
            
            # Verificar si llegó a la meta
            if huevo.rect.colliderect(meta):
                if nivel_actual < MAX_NIVEL:
                    nivel_actual += 1
                    plataformas, obstaculos, powerups, meta, ancho_nivel = gestor_niveles.cargar_nivel(nivel_actual)
                    huevo = Huevo(50, ALTO_PANTALLA - 150)
                    camara = Camara(ancho_nivel)
                else:
                    estado_actual = EstadoJuego.VICTORIA
                    puntuaciones_manager.guardar_puntuacion(nombre_actual, tiempo_transcurrido, nivel_actual)
            
            # Verificar muerte por grietas
            if huevo.grietas >= MAX_GRIETAS:
                estado_actual = EstadoJuego.GAME_OVER
            
            # Verificar muerte por caída
            if huevo.y > ALTO_PANTALLA:
                estado_actual = EstadoJuego.GAME_OVER
        
        # Renderizado
        pantalla.fill((0, 0, 0))
        
        if estado_actual == EstadoJuego.MENU:
            render.dibujar_menu(pantalla, mostrar_puntuaciones, puntuaciones)
        elif estado_actual == EstadoJuego.INGRESO_NOMBRE:
            render.dibujar_ingreso_nombre(pantalla, nombre_actual, cursor_visible)
        elif estado_actual == EstadoJuego.JUGANDO:
            render.dibujar_juego(pantalla, plataformas, obstaculos, powerups, meta, huevo, nivel_actual, tiempo_transcurrido, camara)
        elif estado_actual == EstadoJuego.PAUSA:
            render.dibujar_juego(pantalla, plataformas, obstaculos, powerups, meta, huevo, nivel_actual, tiempo_transcurrido, camara)
            render.dibujar_pausa(pantalla)
        elif estado_actual == EstadoJuego.GAME_OVER:
            render.dibujar_game_over(pantalla, nivel_actual)
        elif estado_actual == EstadoJuego.VICTORIA:
            render.dibujar_victoria(pantalla, tiempo_transcurrido)
        
        pygame.display.flip()
        reloj.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    juego() 