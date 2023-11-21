import tkinter as tk

raiz = tk.Tk()
raiz.title("Aprendiendo Tkinter")
barramenu=tk.Menu(raiz)
raiz.config(menu=barramenu)
calculadora=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Tipos",menu=calculadora)

calculadora.add_command(label="Básica")
calculadora.add_command(label="Avanzada")
calculadora.add_command(label="Progreso")

raiz.geometry("350x500")

raiz.mainloop()


