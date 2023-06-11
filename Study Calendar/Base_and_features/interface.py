import database
from tkinter import *
from tkinter import ttk


window = Tk()


def colors(scale):
    match scale:
        case 1:
            return '#224459'
        case 2:
            return '#58788c'
        case 3:
            return '#819ba6'
        case 4:
            return '#a8bbbf'
        case 5:
            return '#c1d4d9'


class Window_main:
    def __init__(self):
        self.frame1, self.category, self.frame2 = None, None, None
        self.label1, self.label2, self.frame3 = None, None, None
        self.window = window
        self.frame()
        self.screen()
        self.button()
        self.additional()
        self.menu()
        self.window.mainloop()

    def screen(self):
        self.window.title('Organizador de estudos')
        self.window.configure(background='#224459')
        self.window.geometry('321x532')
        self.window.maxsize(width=321, height=532)
        self.window.minsize(width=321, height=532)
        self.window.resizable(False, False)

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.70)
        self.frame2 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame2.place(relx=0.08, rely=0.76, relwidth=0.84, relheight=0.22)
        self.frame3 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame3.place(relx=0.20, rely=0.45, relwidth=0.60, relheight=0.52)

    def button(self):
        self.category = Button(self.frame1, text='Gerenciar categorias', bd=2, bg=colors(4), fg=colors(1), font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.47, relwidth=0.50)
        self.category = Button(self.frame1, text='Consultar agenda', bd=2, bg=colors(4), fg=colors(1), font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.57, relwidth=0.50)
        self.category = Button(self.frame1, text='Definir regras', bd=2, bg=colors(4), fg=colors(1), font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.67, relwidth=0.50)
        self.category = Button(self.frame1, text='Enviar feedback', bd=2, bg=colors(4), fg=colors(1), font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.77, relwidth=0.50)
        self.category = Button(self.frame1, text='Conferir a FAQ', bd=2, bg=colors(4), fg=colors(1), font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.87, relwidth=0.50)

    def additional(self):
        self.label1 = Label(self.frame1, text=f'BEM VINDO(A) AO \nAPLICATIVO QUE TE AJUDA A\nORGANIZAR SUA \nVIDA ACADÊMICA!', fg=colors(5), bg=colors(2),
                            font=('Calibri', 15, 'bold'))
        self.label1.place(relx=0.05, rely=0.02)
        self.label2 = Label(self.frame1, text='Selecione uma das opções abaixo', fg=colors(5), bg=colors(2), font=('Calibri', 12))
        self.label2.place(relx=0.12, rely=0.37)

    def menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)

        def quit():
            self.window.destroy()

        menubar.add_cascade(label='Opções', menu=filemenu)
        menubar.add_cascade(label='Idioma', menu=filemenu2)
        filemenu.add_command(label='Sair', command=quit)
        filemenu2.add_command(label='Português')
        filemenu2.add_command(label='Inglês')



a = Window_main()