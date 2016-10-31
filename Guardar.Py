from Tkconstants import LEFT, RIGHT, SUNKEN, X
from Tkinter import StringVar
from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Button
from Tkinter import *
from Cerrar import Cerrar

campos = ('idLibros', 'Nombre')

def CrearFormGuardar(root, campos):
    formulario = Frame(root)
    div1 = Frame(formulario, width=100)
    div2 = Frame(formulario, padx=7, pady=2)
    formulario.pack(fill=X)
    div1.pack(side=LEFT)
    div2.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    for field in campos:
        lab = Label(div1, width=10, text=field)
        ent = Entry(div2, width=30, relief=SUNKEN)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textVariable=var)
        var.set('---')
        variables.append(var)
    return variables

if __name__ == '__main__':
    root = Tk()
    vars_guardar = CrearFormGuardar(root, campos)
    Button(root, text='Imprimir', command=(lambda: imprimir(vars_guardar))).pack(side=LEFT)
    Cerrar(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: imprimir(vars_guardar)))
    root.mainloop()