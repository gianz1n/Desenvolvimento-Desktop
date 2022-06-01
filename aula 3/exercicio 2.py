from tkinter import*
from unittest import result

def converter():
    c = int(entrarC.get())
    f = ((c*9)/(5))+32

    resultado['text'] = (END,f)


janela = Tk()
janela.geometry("340x250")
janela.config(bg="#42324f")
janela.title('Conversor de Celsius para fahrenheit')
 
l1 = Label(janela,text="Conversor de Celsius para Fahrenheit",font=("Arial", 15),fg="white",bg="#42324f")
l2= Label(janela,text="Temperatura em C: ",font=("Arial", 10,"bold"),fg="white",bg="#42324f")
l3= Label(janela,text="A temperatura em Fahrenheit é: ",font=("Arial", 10,"bold"),fg="white",bg="#42324f")
resultado  = Label(janela, text="Resultado", font=("Arial", 10,"bold"),fg="white",bg="#42324f")
 

 
entrarC= Entry(janela,font=('Arial',10))
 
btn1 = Button(janela,text="Converter",font=("Arial", 10),command=converter)

 

 
l1.grid()
l2.grid()
entrarC.grid()
l3.grid()
btn1.grid()
resultado.grid()

 
janela.mainloop()