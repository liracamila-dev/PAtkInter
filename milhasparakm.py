from tkinter import *
from tkinter import ttk

#criando janela
root = Tk()
#configurando titulo do app
root.title("Milhas para KM")

def calculate(*args):
    try:
        value = float(feet.get()) #entrada
        result = int(1.609 * value * 10000.0)/10000.0 #processamento
        meters.set(result) #saida
    except ValueError:
        pass

#criando o nosso container <div></div>pyth
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet=StringVar()
#input
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters) .grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

#<p></p>
ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)
#<p></p>
ttk.Label(mainframe, text="É equivalente a").grid(column=1, row=2, sticky=E)
#<p><p/>
ttk.Label(mainframe, text="Kilometros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

#gerando loop para renderização intermitente
root.mainloop()
