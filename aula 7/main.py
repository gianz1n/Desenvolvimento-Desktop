from tkinter import *
import funcoes
from funcoes import *

# criação da janela, frame e suas configuraçõesw
root = Tk()
root.geometry("1280x768")

frame1 = Frame()
frame1.configure(bg="#5CE1E6")
ig = PhotoImage(file="back.png")
eye = PhotoImage(file="olhoaberto.png")
cad = PhotoImage(file='cadeado2.png')
pes = PhotoImage(file='pessoa2.png')

#img's
imagem_de_fundo = Label(frame1, text='Hello', foreground='black', image=ig).pack()
cadeado = Label(frame1, text='Hello', foreground='black', image=cad).pack()
pessoa = Label(frame1, text='Hello', foreground='black', image=pes).pack()

#bind's
root.bind('<Return>', lambda event:(funcoes.Cadastro.dados_login(entryUsername, entryPassword)))

# label
username = Label(frame1, text="Username",  font='Arial 13', foreground='Gray', bg="#FFFFFF")
username.place(x=465, y=290)
# Linha 01
linhaName = Label(frame1, text="________________________",  font='Arial 13', foreground='Gray', bg="#FFFFFF")
linhaName.place(x=465, y=345)

password = Label(frame1, text="Password",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
password.place(x=465, y=390)
# linha 02
linhaPassword = Label(frame1, text="________________________",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
linhaPassword.place(x=465, y=445)
# Botão Login
login = Button(frame1, text="Login", font='Arial 15', bg="#EE6187", foreground='white', bd=0, padx=97, pady=17, cursor="hand2", command=lambda: funcoes.Cadastro.dados_login(entryUsername, entryPassword))
login.place(x=512, y=525)

# Entry Username
entryUsername = Entry(frame1, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27)
entryUsername.place(x=467, y=335)
# Entry Password
entryPassword = Entry(frame1, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27, show="*")
entryPassword.place(x=467, y=435)
# showpassword
cv1=IntVar(value=0)
c1 = Checkbutton(frame1,text='Show Password', font='Arial 10',variable=cv1, onvalue=1,offvalue=0, bg="#FFFFFF", foreground="#303030", bd=0, command=lambda: funcoes.Cadastro.mostrar_senha(cv1, entryPassword))
c1.place(x=467, y=480)

frame1.pack()
root.resizable(False, False)
root.mainloop()