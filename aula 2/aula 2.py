from tkinter import*
from tkinter import font


#cores
corbg = '#222729'
corbt = '#dfe9ed'

#Janela
janela = Tk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

janela.title('Calculadora Lite')
janela.config(bg=corbg)




#widgets
bto1 = Button(janela, text='Botao1', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)
bto2 = Button(janela, text='Botao2', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)
bto3 = Button(janela, text='Botao3', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)
bto4 = Button(janela, text='Botao4', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)
bto5 = Button(janela, text='Botao5', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)
bto6 = Button(janela, text='Botao6', font='Calibri 15',bg=corbt, relief=RAISED, overrelief=RIDGE)


#
bto1.grid(row=0, column=0, sticky=NSEW)
bto2.grid(row=0, column=1, sticky=NSEW)
bto3.grid(row=0, column=2, sticky=NSEW)
bto4.grid(row=1, column=0, sticky=NSEW)
bto5.grid(row=1, column=1, sticky=NSEW)
bto6.grid(row=1, column=2, sticky=NSEW)


#exec
janela.mainloop()