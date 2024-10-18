from tkinter import *
from tkinter import ttk
import random
import string

# Criando janela
root = Tk()

# Título da janela do app
root.title("Gerador de Senhas Alfanuméricas")

# Função para gerar a senha
def generate_password(*args):
    try:
        length = int(password_length.get())
        if length < 8:
            result.set("Erro: Mínimo de 8 caracteres")
        else:
            caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
            senha = ''.join(random.SystemRandom().choice(caracteres) for _ in range(length))
            result.set(senha)
    except ValueError:
        result.set("Erro: Digite um número válido")

# Criando as divisões do App
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
password_length = StringVar()
result = StringVar()

# Campo de entrada (comprimento da senha)
password_entry = ttk.Entry(mainframe, width=7, textvariable=password_length)
password_entry.grid(column=2, row=1, sticky=(W, E))

# Labels
ttk.Label(mainframe, text="Comprimento da senha").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Senha gerada:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

# Botão de gerar senha
ttk.Button(mainframe, text="Gerar Senha", command=generate_password).grid(column=2, row=3, sticky=W)

# Ajuste de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Foco no campo de entrada
password_entry.focus()

# Vinculando a tecla Enter à função de gerar senha
root.bind("<Return>", generate_password)

# Gerando loop de render
root.mainloop()