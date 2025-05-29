@startuml Huevos_a_la_Fuga_Corregido

' Configuración del diagrama
skinparam backgroundColor #FFFEF7
skinparam class {
    BackgroundColor #F0F8FF
    BorderColor #4682B4
    ArrowColor #4682B4
}

' Enumeraciones
enum EstadoJuego {
    MENU = 0
    INGRESO_NOMBRE = 1
    JUGANDO = 2
    PAUSA = 3
    GAME_OVER = 4
    VICTORIA = 5
}

' Clases del modelo de objetos del juego
class Huevo {
    - x: int
    - y: int
    - ancho: int
    - alto: int
    - rect: pygame.Rect
    - vel_x: float
    - vel_y: float
    - en_suelo: bool
    - grietas: int
    - invulnerable: bool
    - tiempo_invulnerable: int
    - aterrizaje_suave: bool
    - tiempo_aterrizaje_suave: int
    
    + __init__(x: int, y: int)
    + mover(direccion: int): void
    + saltar(): bool
    + recibir_daño(): void
    + aplicar_powerup(tipo_powerup: str): void
    + actualizar(plataformas: list): void
}

class Plataforma {
    - x: int
    - y: int
    - ancho: int
    - alto: int
    - rect: pygame.Rect
    
    + __init__(x: int, y: int, ancho: int, alto: int)
    + actualizar(): void
}

class Obstaculo {
    - x: int
    - y: int
    - tipo: str
    - ancho: int
    - alto: int
    - letal: bool
    - rect: pygame.Rect
    
    + __init__(x: int, y: int, tipo_obstaculo: str)
    + actualizar(): void
    + efecto(huevo: Huevo): str
}

class PowerUp {
    - x: int
    - y: int
    - tipo: str
    - ancho: int
    - alto: int
    - color: tuple
    - rect: pygame.Rect
    - activo: bool
    
    + __init__(x: int, y: int, tipo_powerup: str)
    + actualizar(): void
    + aplicar(huevo: Huevo): void
}

class Camara {
    - desplazamiento: int
    - ancho_nivel: int
    
    + __init__(ancho_nivel: int)
    + actualizar(huevo: Huevo): void
    + aplicar(rect: pygame.Rect): pygame.Rect
    + posicion_mundial_a_pantalla(x: int, y: int): tuple
    + posicion_pantalla_a_mundial(x: int, y: int): tuple
}

' Clases de lógica del juego
class GestorNiveles {
    {static} + cargar_nivel(numero_nivel: int): tuple
}

class GestorPuntuaciones {
    {static} + guardar_puntuacion(nombre: str, tiempo: int, nivel: int): void
    {static} + cargar_puntuaciones(): list
    {static} + obtener_mejores_puntuaciones(limite: int): list
    {static} + es_record(tiempo: int): bool
}

class ControladorEventos {
    {static} + procesar_eventos(estado_actual: EstadoJuego, nivel_actual: int, huevo: Huevo, mostrar_puntuaciones: bool, cargar_puntuaciones_callback: function): tuple
    {static} + procesar_movimiento(huevo: Huevo): void
}

class GestorColisiones {
    {static} + procesar_colisiones_obstaculos(huevo: Huevo, obstaculos: list): bool
    {static} + procesar_colisiones_powerups(huevo: Huevo, powerups: list): void
    {static} + verificar_meta(huevo: Huevo, meta: pygame.Rect, nivel_actual: int): tuple
    {static} + verificar_muerte_huevo(huevo: Huevo): bool
}

' Clase de configuración
class Configuracion {
    {static} + ANCHO_PANTALLA: int
    {static} + ALTO_PANTALLA: int
    {static} + VELOCIDAD_MOVIMIENTO: int
    {static} + FUERZA_SALTO: int
    {static} + GRAVEDAD: float
    {static} + NIVEL_INICIAL: int
    {static} + MAX_NIVEL: int
    {static} + ANCHO_HUEVO: int
    {static} + ALTO_HUEVO: int
    {static} + MAX_GRIETAS: int
    {static} + TIEMPO_INVULNERABILIDAD: int
    {static} + TIEMPO_INVULNERABILIDAD_POWERUP: int
    {static} + FPS: int
    {static} + BLANCO: tuple
    {static} + NEGRO: tuple
    {static} + ROJO: tuple
    {static} + VERDE: tuple
    {static} + AZUL: tuple
    {static} + AMARILLO: tuple
    {static} + AZUL_CLARO: tuple
    {static} + ARCHIVO_PUNTUACIONES: str
    {static} + NOMBRES_NIVELES: dict
}

' Clases de interfaz de usuario (Render principal)
class Render {
    {static} + obtener_nombre_nivel(nivel: int): str
    {static} + dibujar_menu(pantalla: pygame.Surface, mostrar_puntuaciones: bool, puntuaciones: list): void
    {static} + dibujar_pausa(pantalla: pygame.Surface): void
    {static} + dibujar_game_over(pantalla: pygame.Surface, nivel_actual: int): void
    {static} + dibujar_juego(pantalla: pygame.Surface, plataformas: list, obstaculos: list, powerups: list, meta: pygame.Rect, huevo: Huevo, nivel_actual: int, tiempo_transcurrido: int, camara: Camara): void
    {static} + dibujar_victoria(pantalla: pygame.Surface, tiempo_transcurrido: int): void
    {static} + dibujar_ingreso_nombre(pantalla: pygame.Surface, nombre_actual: str, cursor_visible: bool): void
}

' Módulos de renderizado específico (FUNCIONES, no clases)
package "renderer_juego" {
    class RendererJuegoFunctions <<module>> {
        {static} + dibujar_plataformas(pantalla: pygame.Surface, plataformas: list): void
        {static} + dibujar_obstaculos(pantalla: pygame.Surface, obstaculos: list): void
        {static} + dibujar_powerups(pantalla: pygame.Surface, powerups: list): void
        {static} + dibujar_meta(pantalla: pygame.Surface, meta: pygame.Rect): void
        {static} + dibujar_info_juego(pantalla: pygame.Surface, huevo: Huevo, nivel_actual: int, tiempo_transcurrido: int): void
        {static} + dibujar_nivel_completo(pantalla: pygame.Surface, plataformas: list, obstaculos: list, powerups: list, meta: pygame.Rect, huevo: Huevo, nivel_actual: int, tiempo_transcurrido: int): void
    }
}

package "renderer_huevo" {
    class RendererHuevoFunctions <<module>> {
        {static} + dibujar_huevo(pantalla: pygame.Surface, huevo: Huevo): void
    }
}

package "renderer_menu" {
    class RendererMenuFunctions <<module>> {
        {static} + dibujar_menu_principal(pantalla: pygame.Surface): void
        {static} + dibujar_tabla_puntuaciones(pantalla: pygame.Surface, puntuaciones: list): void
        {static} + dibujar_menu_pausa(pantalla: pygame.Surface): void
        {static} + dibujar_game_over(pantalla: pygame.Surface, nivel_actual: int): void
        {static} + dibujar_victoria(pantalla: pygame.Surface, tiempo_transcurrido: int): void
    }
}

' Utilidades (FUNCIONES, no clases)
package "utils_puntuaciones" {
    class PuntuacionesFunctions <<module>> {
        {static} + guardar_puntuacion(nombre: str, tiempo: int, nivel: int): void
        {static} + cargar_puntuaciones(): list
        {static} - RUTA_PUNTUACIONES: str
    }
}

' Clase principal del juego
class JuegoPrincipal {
    - pantalla: pygame.Surface
    - reloj: pygame.time.Clock
    - estado_actual: EstadoJuego
    - nivel_actual: int
    - tiempo_inicio: int
    - tiempo_transcurrido: int
    - nombre_actual: str
    - cursor_visible: bool
    - ultimo_cambio_cursor: int
    - plataformas: list
    - obstaculos: list
    - powerups: list
    - meta: pygame.Rect
    - ancho_nivel: int
    - huevo: Huevo
    - camara: Camara
    - mostrar_puntuaciones: bool
    - puntuaciones: list
    - ejecutando: bool
    
    + inicializar_pygame(): tuple
    + juego(): void
}

' Launcher principal
class Launcher {
    {static} + main(): void
}

' Relaciones principales
Launcher --> JuegoPrincipal : launches

JuegoPrincipal --> EstadoJuego : uses
JuegoPrincipal --> Huevo : creates/manages
JuegoPrincipal --> Plataforma : manages
JuegoPrincipal --> Obstaculo : manages
JuegoPrincipal --> PowerUp : manages
JuegoPrincipal --> Camara : uses
JuegoPrincipal --> GestorNiveles : uses
JuegoPrincipal --> GestorPuntuaciones : uses
JuegoPrincipal --> ControladorEventos : uses
JuegoPrincipal --> GestorColisiones : uses
JuegoPrincipal --> Render : uses
JuegoPrincipal --> PuntuacionesFunctions : uses

Huevo --> Plataforma : collides_with
Huevo --> Obstaculo : collides_with
Huevo --> PowerUp : collides_with
Huevo --> Configuracion : uses

GestorNiveles --> Plataforma : creates
GestorNiveles --> Obstaculo : creates
GestorNiveles --> PowerUp : creates
GestorNiveles --> Configuracion : uses

GestorColisiones --> Huevo : processes
GestorColisiones --> Obstaculo : processes
GestorColisiones --> PowerUp : processes
GestorColisiones --> Configuracion : uses

ControladorEventos --> Huevo : controls
ControladorEventos --> EstadoJuego : manages

Render --> Huevo : draws
Render --> Plataforma : draws
Render --> Obstaculo : draws
Render --> PowerUp : draws
Render --> Camara : uses
Render --> RendererJuegoFunctions : uses
Render --> RendererHuevoFunctions : uses
Render --> RendererMenuFunctions : uses
Render --> Configuracion : uses

RendererJuegoFunctions --> Configuracion : uses
RendererJuegoFunctions --> RendererHuevoFunctions : uses
RendererHuevoFunctions --> Configuracion : uses
RendererMenuFunctions --> Configuracion : uses

Camara --> Huevo : follows
Camara --> Configuracion : uses

Obstaculo --> Huevo : affects
PowerUp --> Huevo : affects

GestorPuntuaciones --> PuntuacionesFunctions : delegates_to
PuntuacionesFunctions --> Configuracion : uses

note top of Configuracion
    Clase que centraliza todas las
    constantes y configuraciones del juego.
end note

note top of RendererJuegoFunctions
    Módulo de funciones para renderizar
    elementos específicos del juego.
end note

note top of PuntuacionesFunctions
    Módulo de funciones utilitarias
    para manejo de puntuaciones.
end note

note bottom of Launcher
    Punto de entrada principal
    del programa.
end note

@enduml 