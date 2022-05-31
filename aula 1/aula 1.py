from tkinter import*


#cor
CorBg = '#013654'


def imprimir():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        label1['text'] = float(entry1.get()) + float(entry2.get())
        
    else:
     label1['text'] = 'valor Inválido'

#janela
janela = Tk()
janela.geometry('600x400+100+500')
janela.config(bg=CorBg)
janela.minsize(width=600, height=400)
janela.maxsize(width=1024, height=768)

#widgets
label1 = Label(janela, text="Resultado", bg=CorBg, font='Ivy 15', relief=RAISED, foreground='white')
entry1 = Entry(janela, font='Ivy 15', bg=CorBg)
entry2 = Entry(janela, font='Ivy 15', bg=CorBg)
btn1 = Button(janela,text='Sair', font='Ivy 15', command=quit, bg=CorBg, foreground='white')
btn2 = Button(janela,text='Imprimir', font='Ivy 15', command=imprimir, bg=CorBg, foreground='white')


label1.pack()
entry1.pack()
entry2.pack()
btn1.pack()
btn2.pack()

janela.mainloop()
