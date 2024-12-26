import tkinter as tk
import random

# Função para gerar cores aleatórias
def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Criação da janela principal
root = tk.Tk()
root.title("Linguagens de Programação")
root.geometry("800x600")
root.configure(bg="white")

# Canvas para desenhar as palavras
canvas = tk.Canvas(root, width=800, height=600, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Lista de palavras e suas posições
words = [
    ("C", 100, 50),
    ("C++", 200, 100),
    ("C#", 300, 150),
    ("Java", 400, 200),
    ("Ruby", 500, 250),
    ("Python", 600, 300),
    ("R", 100, 350),
    ("SQL", 200, 400),
    ("HTML", 300, 450),
    ("CSS", 400, 500),
    ("Javascript", 500, 100),
    ("PHP", 600, 150)
]

# Desenhando as palavras no canvas
for word, x, y in words:
    font_size = random.randint(16, 32)  # Tamanhos de fonte variados
    canvas.create_text(
        x, y,
        text=word,
        font=("Arial", font_size, "bold"),
        fill=random_color()
    )

# Iniciando o loop da interface gráfica
root.mainloop()
