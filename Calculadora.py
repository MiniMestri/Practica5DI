import tkinter as tk

#Funcion gráfica encarga de parte de la ventana interactiva
def grafica():
    tk.Button(raiz,text="1",width=5,height=2,command=lambda: valor(1)).grid(row=1, column=0, padx=5,pady=10)
    tk.Button(raiz,text="2",width=5,height=2,command=lambda: valor(2)).grid(row=1, column=1, padx=5,pady=10)
    tk.Button(raiz,text="3",width=5,height=2,command=lambda: valor(3)).grid(row=1, column=2, padx=5,pady=10)
    tk.Button(raiz,text="4",width=5,height=2,command=lambda: valor(4)).grid(row=2, column=0, padx=5,pady=10)
    tk.Button(raiz,text="5",width=5,height=2,command=lambda: valor(5)).grid(row=2, column=1, padx=5,pady=10)
    tk.Button(raiz,text="6",width=5,height=2,command=lambda: valor(6)).grid(row=2, column=2, padx=5,pady=10)
    tk.Button(raiz,text="7",width=5,height=2,command=lambda: valor(7)).grid(row=3, column=0, padx=5,pady=10)
    tk.Button(raiz,text="8",width=5,height=2,command=lambda: valor(8)).grid(row=3, column=1, padx=5,pady=10)
    tk.Button(raiz,text="9",width=5,height=2,command=lambda: valor(9)).grid(row=3, column=2, padx=5,pady=10)
    tk.Button(raiz,text="0",width=10,height=2,command=lambda: valor(0)).grid(row=4, column=1, padx=5,pady=10)

#Funcion que se encarga de las operaciones del meno basico como sumar,restar,multiplicar y dividir. Ademas de declarar una variable flobal
def operaciones():
    global botonDiv
    global botonMul
    tk.Button(raiz,text="+",width=5,height=2,command=lambda: valor("+")).grid(row=5, column=0, padx=5,pady=10)
    tk.Button(raiz,text="-",width=5,height=2,command=lambda: valor("-")).grid(row=5, column=1, padx=5,pady=10)
    botonMul=tk.Button(raiz,text="*",width=5,height=2,command=lambda: valor("*"))
    botonMul.grid(row=5, column=2, padx=5,pady=10)
    botonDiv=tk.Button(raiz,text=":",width=5,height=2,command=lambda: valor("/"))
    botonDiv.grid(row=5, column=3, padx=5,pady=10)

#Función que se encarga de las operaciones avanzadas como los cuadrados o cubos y deshabilitar dos botones
def avanzadas():
    tk.Button(raiz,text="x2",width=5,height=2,command=lambda: valor("**2")).grid(row=5, column=0, padx=5,pady=10)
    tk.Button(raiz,text="x3",width=5,height=2,command=lambda: valor("**3")).grid(row=5, column=1, padx=5,pady=10)
    botonMul.config(state="disabled")
    botonDiv.config(state="disabled")

#funcion valor, es la funcion encargada de insertar el contenido que el usuario ha pulsado con los botones
def valor(num):
    entrada.insert(tk.END,str(num))

#Función encargada de calcular las operaciones en la entrada del primer entry  
def calcular():
    resultado=eval(entrada.get())
    salida.delete(0,tk.END)
    salida.insert(tk.END,str(resultado))

#Función encargada de borrar de uno en uno el contenido del entry de entrada y entero el de salida
def borrar():
    entrada.delete((len(entrada.get())-1),tk.END)
    if salida.get()!="":
        salida.delete(0,tk.END)
        entrada.delete(0,tk.END)

raiz = tk.Tk()
raiz.title("Aprendiendo Tkinter")

#Inicialización de las opciones del menú horizontal
barramenu=tk.Menu(raiz)
raiz.config(menu=barramenu)
calculadora=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Tipos",menu=calculadora)

#Opciones
calculadora.add_command(label="Básica", command=operaciones)
calculadora.add_command(label="Avanzada", command=avanzadas)

#Declaración de los entry y los botones fijos
entrada=tk.Entry(raiz)
salida=tk.Entry(raiz)
entrada.grid(row=0, column=0, padx=5,pady=10)
salida.grid(row=0, column=2, padx=5,pady=10)
grafica()
tk.Button(raiz,text="=",width=20,height=4,command=calcular).grid(row=6, column=1, padx=5,pady=10)
tk.Button(raiz,text="BORRAR",width=10,height=4,command=borrar).grid(row=6, column=2, padx=5,pady=10)

raiz.mainloop()
