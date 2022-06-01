from tkinter import*
from unittest import result
from setuptools import Command


#calculos
def calcular():
    if (entrarPeso.get().replace('.', '', 1).isdigit()) and (entrarAltura.get().replace('.', '', 1).isdigit()):
        Peso = float(entrarPeso.get())
        Altura = float(entrarAltura.get())
        IMC = Peso / (Altura * Altura)
        resultado['text'] = IMC

      
#config janela
janela = Tk()
janela.title('IMC calculator')
janela.geometry('400x115')
janela.minsize(width=400, height=150)
janela.maxsize(width=600, height=450)


#widgets
labelPeso = Label(janela, text='Peso:', font='Ivy 18')
labelAltura = Label(janela, text='Altura:', font='Ivy 18')
entrarPeso = Entry(janela, font='Ivy 18')
entrarAltura = Entry(janela, font='Ivy 18')
IMC = Button(janela, text='IMC', font='Ivy 18', command=calcular)
resultado = Label(janela,font='Ivy 18')


#
labelPeso.grid(row=0, column=0, sticky=NSEW)
labelAltura.grid(row=1 , column=0, sticky=NSEW)
entrarPeso.grid(row=0, column=1, sticky=NSEW)
entrarAltura.grid(row=1, column=1, sticky=NSEW)
resultado.grid(row=4, column=1, sticky=NSEW)
IMC.grid(row=3, column=1, sticky=NSEW)


#exec
janela.mainloop()

