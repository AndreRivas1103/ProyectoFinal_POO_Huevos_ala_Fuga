import pygame
import math
import random
from config.configuracion import (
    ANCHO_PANTALLA, ALTO_PANTALLA, 
    BLANCO, NEGRO, ROJO, VERDE, AZUL, AMARILLO
)

CREMA = (255, 253, 208)
MARRON_CLARO = (210, 180, 140)
MARRON_OSCURO = (139, 69, 19)  
ROJO_COCINA = (178, 34, 34)
VERDE_COCINA = (0, 128, 0)
AZUL_COCINA = (70, 130, 180)
AMARILLO_COCINA = (255, 215, 0)

def obtener_nombre_nivel(nivel):
    nombres_niveles = {
        1: "Cocina Inicial",
        2: "Zona de Cocción", 
        3: "Gran Escape"
    }
    return nombres_niveles.get(nivel, f"Nivel {nivel}")

def dibujar_menu(pantalla, mostrar_puntuaciones, puntuaciones):
    pantalla.fill(CREMA)
    
    tamaño_azulejo = 50
    for y in range(0, ALTO_PANTALLA, tamaño_azulejo):
        for x in range(0, ANCHO_PANTALLA, tamaño_azulejo):
            pygame.draw.rect(pantalla, (240, 240, 200), (x, y, tamaño_azulejo, tamaño_azulejo), 1)
            
    for i in range(5):
        x = 100 + i * 150
        pygame.draw.rect(pantalla, MARRON_OSCURO, (x, 50, 80, 10))
        if i % 3 == 0:
            pygame.draw.circle(pantalla, MARRON_CLARO, (x + 40, 100), 20)
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 35, 100, 10, 40))
        elif i % 3 == 1:
            pygame.draw.circle(pantalla, (100, 100, 100), (x + 40, 110), 25)
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 60, 90, 15, 10))
        else:
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 30, 80, 20, 50))
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 25, 80, 30, 10))
    
    if mostrar_puntuaciones:
        pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 250, 180, 500, 300))
        pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 250, 180, 500, 300), 5)
        fuente_titulo = pygame.font.SysFont("arial", 40, bold=True)
        titulo = fuente_titulo.render("MEJORES TIEMPOS", True, MARRON_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 200))
        pygame.draw.line(pantalla, MARRON_OSCURO, 
                       (ANCHO_PANTALLA//2 - 200, 245), 
                       (ANCHO_PANTALLA//2 + 200, 245), 3)
        fuente_lista = pygame.font.SysFont("arial", 24)
        
        if not puntuaciones:
            mensaje = fuente_lista.render("Aún no hay puntuaciones registradas", True, MARRON_OSCURO)
            pantalla.blit(mensaje, (ANCHO_PANTALLA//2 - mensaje.get_width()//2, 300))
        else:
            encabezado = fuente_lista.render("Nombre         Nivel         Tiempo", True, MARRON_OSCURO)
            pantalla.blit(encabezado, (ANCHO_PANTALLA//2 - 200, 260))
            for i, p in enumerate(puntuaciones[:5]):
                color_fila = MARRON_OSCURO
                texto = fuente_lista.render(f"{p['nombre']}            {p['nivel']}             {p['tiempo']}s", True, color_fila)
                pantalla.blit(texto, (ANCHO_PANTALLA//2 - 200, 300 + i*40))
        boton_volver = pygame.Rect(ANCHO_PANTALLA//2 - 150, 500, 300, 50)
        pygame.draw.rect(pantalla, MARRON_CLARO, boton_volver, border_radius=10)
        pygame.draw.rect(pantalla, MARRON_OSCURO, boton_volver, 2, border_radius=10)
        fuente_boton = pygame.font.SysFont("arial", 22)
        volver = fuente_boton.render("Presiona P para volver", True, MARRON_OSCURO)
        pantalla.blit(volver, (boton_volver.centerx - volver.get_width()//2, 
                               boton_volver.centery - volver.get_height()//2))
    else:
        pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO_PANTALLA//2 - 300, 120, 600, 200), border_radius=15)
        pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 300, 120, 600, 200), 5, border_radius=15)
        
        fuente_titulo = pygame.font.SysFont("arial", 60, bold=True)
        titulo = fuente_titulo.render("HUEVOS A LA FUGA", True, MARRON_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 150))
        
        fuente_subtitulo = pygame.font.SysFont("arial", 24, italic=True)
        subtitulo = fuente_subtitulo.render("¡Ayuda al huevo a escapar de la cocina!", True, MARRON_OSCURO)
        pantalla.blit(subtitulo, (ANCHO_PANTALLA//2 - subtitulo.get_width()//2, 220))
        
        tamaño_huevo = 100
        pos_huevo_x = ANCHO_PANTALLA//2
        pos_huevo_y = 350
        
        pygame.draw.ellipse(pantalla, BLANCO, 
                          (pos_huevo_x - tamaño_huevo//2, pos_huevo_y, tamaño_huevo, tamaño_huevo * 1.3))
        
        ojo_izq_x = pos_huevo_x - 20
        ojo_der_x = pos_huevo_x + 20
        ojos_y = pos_huevo_y + 40
        
        pygame.draw.circle(pantalla, NEGRO, (ojo_izq_x, ojos_y), 8)
        pygame.draw.circle(pantalla, NEGRO, (ojo_der_x, ojos_y), 8)
        
        pygame.draw.arc(pantalla, NEGRO, 
                      (pos_huevo_x - 30, pos_huevo_y + 60, 60, 30), 
                      math.pi, 2*math.pi, 3)
    
    fuente_botones = pygame.font.SysFont("arial", 22)
    
    boton_jugar = pygame.Rect(ANCHO_PANTALLA//2 - 180, 500, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_jugar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_jugar, 2, border_radius=10)
    
    instruccion1 = fuente_botones.render("Presiona ENTER para jugar", True, MARRON_OSCURO)
    pantalla.blit(instruccion1, (boton_jugar.centerx - instruccion1.get_width()//2, 
                                boton_jugar.centery - instruccion1.get_height()//2))
    
    boton_puntuaciones = pygame.Rect(ANCHO_PANTALLA//2 - 180, 570, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_puntuaciones, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_puntuaciones, 2, border_radius=10)
    
    instruccion2 = fuente_botones.render("Presiona P para puntuaciones", True, MARRON_OSCURO)
    pantalla.blit(instruccion2, (boton_puntuaciones.centerx - instruccion2.get_width()//2, 
                                boton_puntuaciones.centery - instruccion2.get_height()//2))

def dibujar_pausa(pantalla):
    s = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
    s.set_alpha(150)
    s.fill((50, 50, 50))
    pantalla.blit(s, (0, 0))

    pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), border_radius=15)
    pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), 5, border_radius=15)
    fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
    titulo = fuente_titulo.render("PAUSA", True, MARRON_OSCURO)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 180))
    pygame.draw.line(pantalla, MARRON_OSCURO, 
                   (ANCHO_PANTALLA//2 - 150, 230), 
                   (ANCHO_PANTALLA//2 + 150, 230), 3)

    fuente_botones = pygame.font.SysFont("arial", 22) 
    
    boton_continuar = pygame.Rect(ANCHO_PANTALLA//2 - 150, 280, 300, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_continuar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_continuar, 2, border_radius=10)
    
    instruccion1 = fuente_botones.render("ESC - Continuar", True, MARRON_OSCURO)
    pantalla.blit(instruccion1, (boton_continuar.centerx - instruccion1.get_width()//2, 
                               boton_continuar.centery - instruccion1.get_height()//2))
    
    boton_salir = pygame.Rect(ANCHO_PANTALLA//2 - 150, 350, 300, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_salir, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_salir, 2, border_radius=10)
    
    instruccion2 = fuente_botones.render("Q - Salir al menú", True, MARRON_OSCURO)

    pantalla.blit(instruccion2, (boton_salir.centerx - instruccion2.get_width()//2, 
                               boton_salir.centery - instruccion2.get_height()//2))

def dibujar_game_over(pantalla, nivel_actual):
    pantalla.fill((50, 50, 50))
    pygame.draw.circle(pantalla, (100, 100, 100), (ANCHO_PANTALLA//2, ALTO_PANTALLA//2), 250)
    pygame.draw.circle(pantalla, (80, 80, 80), (ANCHO_PANTALLA//2, ALTO_PANTALLA//2), 230)
    pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO_PANTALLA//2 + 200, ALTO_PANTALLA//2 - 40, 150, 80), border_radius=10)
    centro_x = ANCHO_PANTALLA//2
    centro_y = ALTO_PANTALLA//2
    radio_clara = 120
    
    pygame.draw.ellipse(pantalla, (240, 240, 240), 
                      (centro_x - radio_clara, centro_y - radio_clara//1.3, 
                       radio_clara*2, radio_clara*1.8))
    
    for i in range(8):
        angulo = i * (math.pi / 4)
        offset_x = int(math.cos(angulo) * (radio_clara * 0.8))
        offset_y = int(math.sin(angulo) * (radio_clara * 0.8))
        tamaño_x = random.randint(30, 60)
        tamaño_y = random.randint(30, 60)
        pygame.draw.ellipse(pantalla, (240, 240, 240), 
                          (centro_x + offset_x - tamaño_x//2, centro_y + offset_y - tamaño_y//2,
                           tamaño_x, tamaño_y))
    
    for i in range(12):
        angulo = i * (math.pi / 6)
        offset_x = int(math.cos(angulo) * (radio_clara * 0.9))
        offset_y = int(math.sin(angulo) * (radio_clara * 0.9))
        
        pygame.draw.circle(pantalla, (220, 220, 220), 
                         (centro_x + offset_x, centro_y + offset_y), 15)
    radio_yema = 45
    pygame.draw.circle(pantalla, (255, 200, 30), (centro_x, centro_y), radio_yema)
    pygame.draw.circle(pantalla, (240, 180, 0), (centro_x, centro_y), radio_yema, 3)
    pygame.draw.ellipse(pantalla, (255, 230, 80), 
                      (centro_x - radio_yema//3, centro_y - radio_yema//2, 
                       radio_yema//2, radio_yema//3))
                       
    for i in range(8):
        burbuja_x = centro_x + random.randint(-radio_clara+20, radio_clara-20)
        burbuja_y = centro_y + random.randint(-radio_clara+20, radio_clara-20)
        distancia_centro = math.sqrt((burbuja_x - centro_x)**2 + (burbuja_y - centro_y)**2)
        if distancia_centro > radio_yema * 1.2:
            tamaño_burbuja = random.randint(3, 8)
            pygame.draw.circle(pantalla, (255, 255, 255), (burbuja_x, burbuja_y), tamaño_burbuja)
    
    pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), border_radius=15)
    pygame.draw.rect(pantalla, ROJO_COCINA, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), 5, border_radius=15)
    
    fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
    titulo = fuente_titulo.render("HUEVO ROTO", True, ROJO_COCINA)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 180))
    pos_huevo_x = ANCHO_PANTALLA//2
    pos_huevo_y = 270
    
    pygame.draw.ellipse(pantalla, (240, 240, 240), 
                      (pos_huevo_x - 40, pos_huevo_y - 30, 80, 60))
    
    pygame.draw.circle(pantalla, AMARILLO_COCINA, (pos_huevo_x, pos_huevo_y), 20)
    pygame.draw.circle(pantalla, (240, 180, 0), (pos_huevo_x, pos_huevo_y), 20, 2)
    
    fuente_info = pygame.font.SysFont("arial", 24)
    info_nivel = fuente_info.render(f"Llegaste al nivel {nivel_actual}", True, MARRON_OSCURO)
    pantalla.blit(info_nivel, (ANCHO_PANTALLA//2 - info_nivel.get_width()//2, 350))
    
    boton_reiniciar = pygame.Rect(ANCHO_PANTALLA//2 - 180, 400, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_reiniciar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_reiniciar, 2, border_radius=10)
    
    fuente_boton = pygame.font.SysFont("arial", 22)
    instruccion = fuente_boton.render("Presiona ENTER para volver al menú", True, MARRON_OSCURO)
    pantalla.blit(instruccion, (boton_reiniciar.centerx - instruccion.get_width()//2, 
                              boton_reiniciar.centery - instruccion.get_height()//2))
