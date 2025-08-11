import random
#---Funciones del juego---

def MOSTRAR_BIENVENIDA():
  """
  Muestra un mensaje de bienvenida al juego y las reglas.
  """
  print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
  print("-------------------------------------------------")
  print("Reglas del juego:")
  print("- Piedra aplasta a Tijeras.")
  print("- Tijeras cortan a Papel.")
  print("- Papel envuelve a Piedra.")
  print("¡Que comience la diversión!")

def obtener_nombre_usuario():
    """
    Solicita el nombre del usuario y se asegura que no este vacio.
    """
    while True:
        nombre = input("Por favor, ingresa tu nombre de usuario: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")

def obtener_jugada_usuario():
    """
    Solicitar la jugada al usuario y valida la entrada.
    """
    opciones_validas = ["piedra", "papel", "tijeras"]
    while True:
        jugada = input("Elige tu jugada (piedra, papel o tijeras): ").strip().lower()
        if jugada in opciones_validas:
            return jugada
        else:
            print("Opción no válida. Inténtalo de nuevo.")
def obtener_jugada_computadora():
    """
    Genera una jugada aleatoria para la computadora.
    """
    opciones_validas = ["piedra", "papel", "tijeras"]
    return random.choice(opciones_validas)
def determinar_ganador(jugada_usuario, jugada_computadora):
    """
    Determina el ganador de la partida.
    """
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif (jugada_usuario == "piedra" and jugada_computadora == "tijeras") or \
         (jugada_usuario == "papel" and jugada_computadora == "piedra") or \
         (jugada_usuario == "tijeras" and jugada_computadora == "papel"):
        return "Gana"
    else:
        return "Pierde"
    
#---------Logica principal del programa------

if __name__ == "__main__":
    MOSTRAR_BIENVENIDA()
    nombre_usuario = obtener_nombre_usuario()
    print(f"¡Hola, {nombre_usuario}! Vamos a jugar.")
    
    while True:
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()
        
        print(f"Tú elegiste: {jugada_usuario}")
        print(f"La computadora eligió: {jugada_computadora}")
        
        resultado = determinar_ganador(jugada_usuario, jugada_computadora)
        
        if resultado == "Gana":
            print("!Ganaste esta ronda!")
        elif resultado == "Pierde":
            print("¡Perdiste esta ronda!")
        else:
            print("Es un empate.")