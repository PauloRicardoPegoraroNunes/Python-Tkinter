from tkinter import *


janela = Tk()
janela.title('Calculator')
janela['bg'] = 'white'

def soma():
    v1 =int(valor1.get())
    v2 = int(valor2.get())
    soma = v1+v2
    lb['text'] = soma

def limpa():
    lb['text'] = 'Resultado sera exibido aqui'

def sub():
    v1 =int(valor1.get())
    v2 = int(valor2.get())
    sub = v1-v2
    lb['text'] = sub
def div():
    v1 =int(valor1.get())
    v2 = int(valor2.get())
    div = v1/v2
    lb['text'] = div

def mult():
    v1 =int(valor1.get())
    v2 = int(valor2.get())
    mult = v1*v2
    lb['text'] = mult


valor1 = Entry(janela)
valor1.place(x=50,y=300)
valor2 = Entry(janela)
valor2.place(x=50,y=350)

bt = Button(janela, width=20, text='Soma', command=soma)
bt.place(x=50, y=100)

sub = Button(janela, width=20, text='Subtração', command=sub)
sub.place(x=50, y=140)

mult = Button(janela, width=20, text='Multiplicação', command=mult)
mult.place(x=50, y=180)

div = Button(janela, width=20, text='Divisão', command=div)
div.place(x=50, y=220)








limpa = Button(janela, width=20, text='limpa', command=limpa)
limpa.place(x=50, y=30)


lb = Label(janela, text='Resultado sera exibido aqui')
lb.place(x=50, y=400)

janela.geometry('300x500+500+500')


janela.mainloop()
