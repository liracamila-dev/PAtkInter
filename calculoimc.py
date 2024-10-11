from tkinter import *
from tkinter import ttk

#criando janela
root = Tk()
#configurando titulo do app
root.title("Calculo IMC")

def calculate(*args):
    try:
        getaltura = float(altura.get()) #entrada
        getpeso = float(peso.get()) #entrada
        result = getpeso/(getaltura*getaltura) #processamento
        imc.set(f"{result: .2f}") #saida
    except ValueError:
        pass

#criando o nosso container <div></div>pyth
mainframe = ttk.Frame(root, padding = "5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

getaltura=StringVar()
getpeso=StringVar()

#input
altura=StringVar()
altura_entry = ttk.Entry(mainframe, width=7, textvariable=altura)
altura_entry.grid(column=1, row=1, sticky=(W, E))
peso=StringVar()
peso_entry = ttk.Entry(mainframe, width=7, textvariable=peso)
peso_entry.grid(column=1, row=2, sticky=(W, E))

imc = StringVar()
ttk.Label(mainframe, textvariable=imc) .grid(column=3, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

#<p></p>
ttk.Label(mainframe, text="Altura").grid(column=3, row=1, sticky=W)
#<p></p>
ttk.Label(mainframe, text="Peso").grid(column=3, row=2, sticky=W)
#<p></p>
ttk.Label(mainframe, text="O resultado do IMC é:").grid(column=1, row=4, sticky=E)
#<p><p/>

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

altura_entry.focus()
root.bind("<Return>", calculate)

#gerando loop para renderização intermitente
root.mainloop()
