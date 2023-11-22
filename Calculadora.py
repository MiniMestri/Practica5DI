import tkinter as tk

def grafica():
    tk.Button(raiz,text="1",width=5,height=2).grid(row=1, column=0, padx=5,pady=10)
    tk.Button(raiz,text="2",width=5,height=2).grid(row=1, column=1, padx=5,pady=10)
    tk.Button(raiz,text="3",width=5,height=2).grid(row=1, column=2, padx=5,pady=10)
    tk.Button(raiz,text="4",width=5,height=2).grid(row=2, column=0, padx=5,pady=10)
    tk.Button(raiz,text="5",width=5,height=2).grid(row=2, column=1, padx=5,pady=10)
    tk.Button(raiz,text="6",width=5,height=2).grid(row=2, column=2, padx=5,pady=10)
    tk.Button(raiz,text="7",width=5,height=2).grid(row=3, column=0, padx=5,pady=10)
    tk.Button(raiz,text="8",width=5,height=2).grid(row=3, column=1, padx=5,pady=10)
    tk.Button(raiz,text="9",width=5,height=2).grid(row=3, column=2, padx=5,pady=10)
    tk.Button(raiz,text="0",width=10,height=2).grid(row=4, column=1, padx=5,pady=10)
    
def basica():
    tk.Entry(raiz).grid(row=0, column=1, padx=5,pady=10)
    grafica()
    
raiz = tk.Tk()
raiz.title("Aprendiendo Tkinter")
barramenu=tk.Menu(raiz)
raiz.config(menu=barramenu)
calculadora=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Tipos",menu=calculadora)

calculadora.add_command(label="Básica", command=basica)
calculadora.add_command(label="Avanzada")
calculadora.add_command(label="Progreso")

raiz.mainloop()
