# Diagrama UML - Proyecto "Huevos a la Fuga"

## Descripción General
Este documento describe el diagrama UML del proyecto "Huevos a la Fuga", un juego de plataformas 2D desarrollado en Python con Pygame donde el jugador controla un huevo que debe escapar de una cocina evitando obstáculos y recogiendo power-ups.

## Arquitectura del Sistema

### 1. Enumeraciones
- **EstadoJuego**: Define los diferentes estados del juego (MENU, INGRESO_NOMBRE, JUGANDO, PAUSA, GAME_OVER, VICTORIA)

### 2. Clases del Modelo de Objetos del Juego

#### Huevo (Clase Principal)
- **Responsabilidad**: Representa el personaje jugable
- **Atributos principales**: posición (x, y), velocidades, estado de grietas, invulnerabilidad
- **Métodos principales**: mover(), saltar(), recibir_daño(), aplicar_powerup(), actualizar()

#### Plataforma
- **Responsabilidad**: Representa las superficies donde el huevo puede caminar
- **Atributos**: posición, dimensiones, rectángulo de colisión
- **Métodos**: actualizar()

#### Obstaculo
- **Responsabilidad**: Representa elementos peligrosos del juego
- **Tipos**: "sarten" (letal), "aceite" (deslizante)
- **Métodos**: efecto() para aplicar daño o efectos al huevo

#### PowerUp
- **Responsabilidad**: Representa objetos que benefician al jugador
- **Tipos**: "cascara" (reduce grietas), "turbo" (velocidad), "papel" (invulnerabilidad)
- **Métodos**: aplicar() para dar beneficios al huevo

#### Camara
- **Responsabilidad**: Maneja el seguimiento visual del huevo
- **Funcionalidad**: Desplaza la vista para mantener al huevo visible
- **Métodos**: actualizar(), aplicar(), conversiones de coordenadas

### 3. Clases de Lógica del Juego

#### GestorNiveles
- **Responsabilidad**: Carga y configura los diferentes niveles
- **Patrón**: Factory Method para crear niveles
- **Método principal**: cargar_nivel() retorna plataformas, obstáculos, power-ups y meta

#### GestorPuntuaciones
- **Responsabilidad**: Maneja persistencia de puntuaciones
- **Funcionalidad**: Guardar/cargar puntuaciones en JSON
- **Métodos**: guardar_puntuacion(), cargar_puntuaciones(), es_record()

#### ControladorEventos
- **Responsabilidad**: Procesa entrada del usuario
- **Funcionalidad**: Maneja eventos de teclado según el estado del juego
- **Métodos**: procesar_eventos(), procesar_movimiento()

#### GestorColisiones
- **Responsabilidad**: Detecta y procesa colisiones
- **Funcionalidad**: Maneja interacciones entre el huevo y otros objetos
- **Métodos**: procesar_colisiones_obstaculos(), procesar_colisiones_powerups(), verificar_meta()

### 4. Clases de Interfaz de Usuario

#### Render (Clase Principal de Renderizado)
- **Responsabilidad**: Coordina el dibujado de todas las pantallas
- **Métodos**: dibujar_menu(), dibujar_juego(), dibujar_pausa(), etc.

#### Clases de Renderizado Específico
- **RendererJuego**: Renderizado del estado de juego
- **RendererHuevo**: Dibujado específico del personaje
- **RendererMenu**: Renderizado de menús

### 5. Clase Principal

#### JuegoPrincipal
- **Responsabilidad**: Coordina todo el juego (Game Loop)
- **Funcionalidad**: Inicialización, bucle principal, gestión de estados
- **Patrón**: Singleton implícito (una instancia por ejecución)

## Patrones de Diseño Utilizados

### 1. State Pattern
- La enumeración `EstadoJuego` junto con el `JuegoPrincipal` implementa el patrón Estado
- Cada estado tiene comportamiento específico para eventos y renderizado

### 2. Factory Method
- `GestorNiveles.cargar_nivel()` crea niveles con diferentes configuraciones
- Encapsula la lógica de creación de objetos del juego

### 3. Static Factory Methods
- Clases como `GestorPuntuaciones`, `ControladorEventos`, `GestorColisiones` usan métodos estáticos
- Proporcionan funcionalidad sin necesidad de instanciación

### 4. Observer Pattern (Implícito)
- El `Huevo` notifica cambios de estado a través de sus atributos
- Otros sistemas reaccionan a estos cambios (colisiones, renderizado)

## Relaciones Principales

### Composición
- `JuegoPrincipal` contiene instancias de `Huevo`, `Camara`, listas de objetos del juego

### Dependencia
- `Huevo` depende de `Plataforma` para las colisiones
- `Camara` depende de `Huevo` para el seguimiento
- `Render` depende de todos los objetos visuales

### Asociación
- `Obstaculo` y `PowerUp` interactúan con `Huevo`
- `GestorColisiones` procesa las interacciones entre objetos

## Flujo de Ejecución

1. **Inicialización**: `JuegoPrincipal` inicializa Pygame y crea objetos iniciales
2. **Bucle Principal**: 
   - Procesamiento de eventos (`ControladorEventos`)
   - Actualización de física (`Huevo.actualizar()`)
   - Detección de colisiones (`GestorColisiones`)
   - Actualización de cámara (`Camara.actualizar()`)
   - Renderizado (`Render`)
3. **Cambio de Niveles**: `GestorNiveles` crea nuevos objetos del juego
4. **Persistencia**: `GestorPuntuaciones` guarda/carga datos

## Extensibilidad

El diseño permite fácil extensión:
- **Nuevos tipos de obstáculos**: Agregar casos en `Obstaculo.efecto()`
- **Nuevos power-ups**: Agregar casos en `PowerUp.aplicar()`
- **Nuevos niveles**: Agregar configuraciones en `GestorNiveles.cargar_nivel()`
- **Nuevos estados**: Agregar a `EstadoJuego` y manejar en `JuegoPrincipal`

## Principios SOLID Aplicados

- **SRP**: Cada clase tiene una responsabilidad específica
- **OCP**: Fácil extensión sin modificar código existente
- **DIP**: Dependencias hacia abstracciones (interfaces implícitas)
- **ISP**: Interfaces pequeñas y específicas (métodos estáticos agrupados)

Este diagrama UML representa una arquitectura bien estructurada que separa claramente las responsabilidades entre modelo, vista y controlador, facilitando el mantenimiento y la extensión del juego. 