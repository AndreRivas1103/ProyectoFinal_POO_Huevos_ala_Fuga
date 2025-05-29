@startuml Huevos_a_la_Fuga

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

' Clases de interfaz de usuario
class Render {
    {static} + obtener_nombre_nivel(nivel: int): str
    {static} + dibujar_menu(pantalla: pygame.Surface, mostrar_puntuaciones: bool, puntuaciones: list): void
    {static} + dibujar_pausa(pantalla: pygame.Surface): void
    {static} + dibujar_game_over(pantalla: pygame.Surface, nivel_actual: int): void
    {static} + dibujar_juego(pantalla: pygame.Surface, plataformas: list, obstaculos: list, powerups: list, meta: pygame.Rect, huevo: Huevo, nivel_actual: int, tiempo_transcurrido: int, camara: Camara): void
    {static} + dibujar_victoria(pantalla: pygame.Surface, tiempo_transcurrido: int): void
    {static} + dibujar_ingreso_nombre(pantalla: pygame.Surface, nombre_actual: str, cursor_visible: bool): void
}

' Clases de renderizado específico
class RendererJuego {
    {static} + renderizar_fondo(pantalla: pygame.Surface, camara: Camara): void
    {static} + renderizar_elementos(pantalla: pygame.Surface, elementos: list, camara: Camara): void
}

class RendererHuevo {
    {static} + dibujar_huevo(pantalla: pygame.Surface, huevo: Huevo, camara: Camara): void
    {static} + obtener_color_huevo(grietas: int): tuple
}

class RendererMenu {
    {static} + dibujar_fondo_menu(pantalla: pygame.Surface): void
    {static} + dibujar_botones(pantalla: pygame.Surface): void
    {static} + dibujar_titulo(pantalla: pygame.Surface): void
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

' Utilidades
class Puntuaciones {
    {static} + guardar_puntuacion(nombre: str, tiempo: int, nivel: int): void
    {static} + cargar_puntuaciones(): list
}

' Relaciones principales
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

Huevo --> Plataforma : collides_with
Huevo --> Obstaculo : collides_with
Huevo --> PowerUp : collides_with

GestorNiveles --> Plataforma : creates
GestorNiveles --> Obstaculo : creates
GestorNiveles --> PowerUp : creates

GestorColisiones --> Huevo : processes
GestorColisiones --> Obstaculo : processes
GestorColisiones --> PowerUp : processes

ControladorEventos --> Huevo : controls
ControladorEventos --> EstadoJuego : manages

Render --> Huevo : draws
Render --> Plataforma : draws
Render --> Obstaculo : draws
Render --> PowerUp : draws
Render --> Camara : uses

RendererJuego --> Camara : uses
RendererHuevo --> Huevo : draws
RendererHuevo --> Camara : uses

Camara --> Huevo : follows

Obstaculo --> Huevo : affects
PowerUp --> Huevo : affects

GestorPuntuaciones <|-- Puntuaciones : implements

note top of Huevo
    Clase principal del personaje jugable.
    Maneja física, movimiento y estado del huevo.
end note

note top of GestorNiveles
    Gestiona la creación y configuración
    de los diferentes niveles del juego.
end note

note top of Camara
    Maneja el seguimiento visual del huevo
    y el desplazamiento de la vista.
end note

note bottom of EstadoJuego
    Enumeración que define todos
    los estados posibles del juego.
end note

@enduml 