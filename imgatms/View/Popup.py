import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def showLog():
    print("Mostrando log")

class Popup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Finalizado")
        self.root.geometry("590x90")
        
        self.text = ttk.Label(self.root, text="Copiado finalizado.")
        self.text.grid(row=0, column=0, columnspan=2)
        self.description = ttk.Label(self.root, text="Puedes ver el log de la ejecución en la carpeta Log buscando por el nombre de la horafecha que corriste.")
        self.description.grid(row=1, column=0)
        self.button_showinfo = ttk.Button(self.root, text="Show Log", command=showLog)
        self.button_showinfo.grid(row=2, column=0)
        

