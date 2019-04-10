
from tkinter import *
from tkinter import ttk, font

import imgatms.main as m

class Application:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Sincronización de imágenes")
        self.raiz.geometry("450x400")

        self.fuente = font.Font(weight='bold')  
        
        # Declara variables de control  
        self.img_name = StringVar()
        
        self.MS = BooleanVar()
        self.PS = BooleanVar()
        self.PC = BooleanVar()
        self.NC = BooleanVar()

        self.accion = StringVar()
        
        self.mensaje = StringVar()
        self.mensaje.set("Esperando para ejecutar..")
        
        """ Define trazas con variables de control de los widgets Entry()
        para detectar cambios en los datos. Si se producen cambios
        se llama a la función 'self.calcular' para validación y para
        calcular importe a pagar
        self.km.trace('w', self.calcular)
        self.precio.trace('w', self.calcular)
        
        Llama a función para validar y calcular
        self.calcular() """
        
        # ------------------------------------
        # Declaracion de widgets de la ventana
        # ------------------------------------
        self.titulo_accion = ttk.Label(self.raiz, text="Accion:", 
            font=self.fuente)
        self.accion1 = ttk.Radiobutton(self.raiz, text='Copiar imágen', 
            variable=self.accion, value='cp')
        self.accion2 = ttk.Radiobutton(self.raiz, text='Eliminar imágen', 
            variable=self.accion, value='rm')
        
        self.titulo_imagen = ttk.Label(self.raiz, text="Nombre imagen: ",
            font=self.fuente)
        self.imagen = ttk.Entry(self.raiz, textvariable=self.img_name)

        self.titulo_complejos = ttk.Label(self.raiz, text="Complejos:", 
            font=self.fuente)                                                            
        self.check_MS = ttk.Checkbutton(self.raiz, text='Montevideo Shopping', 
            variable=self.MS,
            onvalue=True, offvalue=False)
        self.check_PS = ttk.Checkbutton(self.raiz, text='Portones Shopping', 
            variable=self.PS,
            onvalue=True, offvalue=False)
        self.check_PC = ttk.Checkbutton(self.raiz, text='Punta Carreta Shopping', 
            variable=self.PC,
            onvalue=True, offvalue=False)
        self.check_NC = ttk.Checkbutton(self.raiz, text='Nuevo Centro Shopping', 
            variable=self.NC,
            onvalue=True, offvalue=False)

        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        self.boton_ejecutar = ttk.Button(self.raiz, text="Ejecutar", 
            command=self.execute)

        self.titulo_mensaje = ttk.Label(self.raiz, textvariable=self.mensaje, 
            font=self.fuente)

        # -----------------------------
        # Posicionamiento en la ventana 
        # -----------------------------
        self.titulo_accion.grid(column=0, row=0, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.accion1.grid(column=0, row=1, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.accion2.grid(column=0, row=2, padx=5, pady=5, 
            sticky=(N, S, E, W))

        self.titulo_imagen.grid(column=0, row=3, padx=0, pady=0, sticky='nsew')
        self.imagen.grid(column=0, row=4, padx=5, pady=5, sticky='nsew')

        self.titulo_complejos.grid(column=0, row=5, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.check_MS.grid(column=0, row=6, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.check_PS.grid(column=0, row=7, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.check_PC.grid(column=0, row=8, padx=5, pady=5, 
            sticky=(N, S, E, W))
        self.check_NC.grid(column=0, row=9, padx=5, pady=5, 
            sticky=(N, S, E, W))

        self.separ1.grid(column=0, row=10, padx=5, pady=5, 
            sticky=(N, S, E, W))

        self.boton_ejecutar.grid(column=0, row=11, padx=5, pady=5, 
            sticky=(N, S, E, W))
        """ self.boton_salir.grid(column=1, row=9, padx=5, pady=5, 
            sticky=(N, S, E, W)) """

        self.titulo_mensaje.grid(column=0, row=12, padx=5, pady=5, 
            sticky=(N, S, E, W))

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(10, weight=1)

        self.raiz.mainloop()

    def execute(self):
        if not self.isActionSelected():
            print("DEBUG: ERROR: There is not action selected")
            self.setMessage("ERROR: There is not action selected")
        elif self.isEmptyImgName():
            print("DEBUG: ERROR: There is not text for img_name")
            self.setMessage("ERROR: There is not text introduced in 'Nombre imagen'")
        elif not self.isAtLeastOneCinemaSelected():
            print("DEBUG: ERROR: There must be at least one cinema selected")
            self.setMessage("ERROR: There must be at least one cinema selected")
        else:
            if self.isCheckedMS():
                print("DEBUG: MS selected")
            if self.isCheckedPS():
                print("DEBUG: PS selected")
            if self.isCheckedPC():
                print("DEBUG: PC selected")
            if self.isCheckedNC():
                print("DEBUG: NC selected")
            
            print("DEBUG: Execute button was pressed.")
            self.setMessage("Executing..")
            # Mando al main que está listo para ejecutar
            m.execute(self.getAction(), self.img_name.get(), self.isCheckedMS(), self.isCheckedPS(), self.isCheckedPC(), self.isCheckedNC())
    
    def isActionSelected(self):
        return not self.accion.get() == ""

    def isEmptyImgName(self):
        return self.img_name.get() == ""

    def isAtLeastOneCinemaSelected(self):
        return (self.isCheckedMS() or self.isCheckedPS() or self.isCheckedPC() or self.isCheckedNC())
         
    def isCheckedMS(self):
        return self.MS.get()

    def isCheckedPS(self):
        return self.PS.get()

    def isCheckedPC(self):
        return self.PC.get()

    def isCheckedNC(self):
        return self.NC.get()

    def setMessage(self, text):
        self.mensaje.set(text)
    
    def getAction(self):
        return self.accion.get()