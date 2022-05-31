from tkinter import*
from tkinter import font

from setuptools import Command


#cores
corbg = '#222729'
corbt = '#dfe9ed'

def aumentar():
    if int(label1['text']) < 10:
        label1['text'] = int(label1['text']) +1
    else:
        pass

def diminuir():
    if int(label1['text']) > -10:
        label1['text'] = int(label1['text']) -1
    else:
        pass                      

#Janela
janela = Tk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
#linkando com teclado
janela.bind('-',lambda event:diminuir())
janela.bind('+',lambda event:aumentar())






janela.title('Calculadora Lite')
janela.config(bg=corbg)


#widgets
bto1 = Button(janela, text='-', font='Calibri 15',bg=corbt, relief=RAISED, command=diminuir)
label1 = Label(janela, text='0', font='Calibri 15',bg=corbt, relief=RAISED)
bto3 = Button(janela, text='+', font='Calibri 15',bg=corbt, relief=RAISED, command=aumentar)


#
bto1.grid(row=0, column=0, sticky=NSEW)
label1.grid(row=0, column=1, sticky=NSEW)
bto3.grid(row=0, column=2, sticky=NSEW)

#exec
janela.mainloop()