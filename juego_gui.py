import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # Importa las librerías necesarias de Pillow
import random

# --- Estructuras de Datos y Lógica del Juego ---

# Tupla para las opciones fijas del juego
OPCIONES = ("piedra", "papel", "tijeras")

# Diccionario para definir las reglas de forma clara y escalable
REGLAS = {
    "piedra": "tijeras",
    "papel": "piedra",
    "tijeras": "papel"
}

# Función para determinar el ganador, ahora más simple gracias al diccionario
def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif REGLAS[jugada_usuario] == jugada_computadora:
        return "Gana"
    else:
        return "Pierde"

# --- Clase de la Interfaz Gráfica (GUI) ---

class JuegoGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Piedra, Papel o Tijeras")
        self.ventana.geometry("500x550") # Tamaño fijo para la ventana
        self.ventana.resizable(False, False) # Evita que se pueda cambiar el tamaño

        # Configura la columna principal del grid para que se centre
        self.ventana.columnconfigure(0, weight=1)

        # Estilo para los widgets (botones y etiquetas)
        self.estilo = ttk.Style()
        self.estilo.configure("TButton", font=("Helvetica", 12), padding=10)
        self.estilo.configure("TLabel", font=("Helvetica", 14))
        self.estilo.configure("Resultado.TLabel", font=("Helvetica", 16, "bold"))

        # Diccionario para llevar el marcador del juego
        self.marcador = {"victorias": 0, "derrotas": 0, "empates": 0}
        
        # Carga las imágenes de forma segura usando Pillow
        self.imagenes = {
            "piedra": ImageTk.PhotoImage(Image.open("piedra.png")),
            "papel": ImageTk.PhotoImage(Image.open("papel.png")),
            "tijeras": ImageTk.PhotoImage(Image.open("tijeras.png"))
        }

        # --- Creación de los Widgets usando el sistema .grid() ---

        # 1. Título (Fila 0)
        ttk.Label(self.ventana, text="¡Elige tu jugada!", style="TLabel").grid(row=0, column=0, pady=10)

        # 2. Frame para los botones de elección (Fila 1)
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.grid(row=1, column=0, pady=10)

        ttk.Button(frame_botones, text="Piedra", command=lambda: self.jugar("piedra")).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Papel", command=lambda: self.jugar("papel")).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Tijeras", command=lambda: self.jugar("tijeras")).pack(side="left", padx=10)
        
        # 3. Frame para mostrar las jugadas (imágenes) (Fila 2)
        frame_jugadas = ttk.Frame(self.ventana)
        frame_jugadas.grid(row=2, column=0, pady=20, sticky="ew")
        frame_jugadas.columnconfigure(0, weight=1) # Columna para el jugador
        frame_jugadas.columnconfigure(1, weight=1) # Columna para la computadora

        self.label_jugador = ttk.Label(frame_jugadas, text="Tú", style="TLabel")
        self.label_jugador.grid(row=0, column=0)

        self.label_computadora = ttk.Label(frame_jugadas, text="Computadora", style="TLabel")
        self.label_computadora.grid(row=0, column=1)

        # 4. Etiqueta para mostrar el resultado de la ronda (Fila 3)
        self.label_resultado = ttk.Label(self.ventana, text="¡Mucha suerte!", style="Resultado.TLabel")
        self.label_resultado.grid(row=3, column=0, pady=20)

        # 5. Marcador visual (Fila 4)
        self.label_marcador = ttk.Label(self.ventana, text="", style="TLabel")
        self.label_marcador.grid(row=4, column=0, pady=10)
        self.actualizar_marcador()

    def jugar(self, jugada_usuario):
        jugada_computadora = random.choice(OPCIONES)
        resultado = determinar_ganador(jugada_usuario, jugada_computadora)

        # Actualiza las imágenes en la pantalla
        self.label_jugador.config(image=self.imagenes[jugada_usuario])
        self.label_computadora.config(image=self.imagenes[jugada_computadora])

        # Actualiza el marcador y el texto del resultado
        if resultado == "Gana":
            self.marcador["victorias"] += 1
            self.label_resultado.config(text="🎉 ¡GANASTE! 🎉", foreground="green")
        elif resultado == "Pierde":
            self.marcador["derrotas"] += 1
            self.label_resultado.config(text="🤖 ¡PERDISTE! 🤖", foreground="red")
        else:
            self.marcador["empates"] += 1
            self.label_resultado.config(text="🤝 ¡EMPATE! 🤝", foreground="blue")
        
        self.actualizar_marcador()

    def actualizar_marcador(self):
        # Actualiza el texto del marcador en la pantalla
        texto_marcador = f"Victorias: {self.marcador['victorias']} | Derrotas: {self.marcador['derrotas']} | Empates: {self.marcador['empates']}"
        self.label_marcador.config(text=texto_marcador)


#--- Lógica principal para lanzar la aplicación ---

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = JuegoGUI(ventana_principal)
    ventana_principal.mainloop()