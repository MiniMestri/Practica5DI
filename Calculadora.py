import tkinter as tk

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

def operaciones():
    tk.Button(raiz,text="+",width=5,height=2,command=lambda: valor("+")).grid(row=5, column=0, padx=5,pady=10)
    tk.Button(raiz,text="-",width=5,height=2,command=lambda: valor("-")).grid(row=5, column=1, padx=5,pady=10)
    tk.Button(raiz,text="*",width=5,height=2,command=lambda: valor("*")).grid(row=5, column=2, padx=5,pady=10)
    tk.Button(raiz,text=":",width=5,height=2,command=lambda: valor("/")).grid(row=5, column=3, padx=5,pady=10)

def valor(num):
    entrada.insert(tk.END,str(num))
    
def calcular():
    resultado=eval(entrada.get())
    entrada.delete(0,tk.END)
    entrada.insert(tk.END,str(resultado))

def borrar():
    longitud=len(entrada.get())-1
    entrada.delete(longitud,tk.END)
        
raiz = tk.Tk()
raiz.title("Aprendiendo Tkinter")

barramenu=tk.Menu(raiz)
raiz.config(menu=barramenu)
calculadora=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Tipos",menu=calculadora)

calculadora.add_command(label="Básica", command=operaciones)
entrada=tk.Entry(raiz)
entrada.grid(row=0, column=1, padx=5,pady=10)
tk.Button(raiz,text="=",width=20,height=4,command=calcular).grid(row=6, column=1, padx=5,pady=10)
tk.Button(raiz,text="BORRAR",width=10,height=4,command=borrar).grid(row=6, column=2, padx=5,pady=10)
grafica()

calculadora.add_command(label="Avanzada")
calculadora.add_command(label="Progreso")

raiz.mainloop()
