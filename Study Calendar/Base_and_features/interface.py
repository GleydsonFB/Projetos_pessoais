import tkinter
import datetime
import database
from tkinter import *
from tkinter import ttk

date = datetime.datetime.now()
month = date.month
year = date.year


def date_month():
    match month:
        case 1:
            return 'janeiro', 31
        case 2:
            return 'fevereiro', 28
        case 3:
            return 'março', 31
        case 4:
            return 'abril', 30
        case 5:
            return 'maio', 31
        case 6:
            return 'junho', 30
        case 7:
            return 'julho', 31
        case 8:
            return 'agosto', 31
        case 9:
            return 'setembro', 30
        case 10:
            return 'outubro', 31
        case 11:
            return 'novembro', 30
        case 12:
            return 'dezembro', 31


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
        window = Tk()
        self.frame1, self.category, self.frame2 = None, None, None
        self.label1, self.label2, self.frame3 = None, None, None
        self.window = window
        self.frame()
        self.screen()
        self.button()
        self.additional()
        self.window.mainloop()

    def screen(self):
        self.window.title('Organizador de estudos')
        self.window.configure(background=colors(1))
        self.window.geometry('321x532+50+50')
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
        self.category = Button(self.frame1, text='Gerenciar categorias', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Window_category)
        self.category.place(relx=0.25, rely=0.47, relwidth=0.50)
        self.category = Button(self.frame1, text='Consultar agenda', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'),
                               command=Window_schedule)
        self.category.place(relx=0.25, rely=0.57, relwidth=0.50)
        self.category = Button(self.frame1, text='Definir regras', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.67, relwidth=0.50)
        self.category = Button(self.frame1, text='Enviar feedback', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.77, relwidth=0.50)
        self.category = Button(self.frame1, text='Conferir a FAQ', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.25, rely=0.87, relwidth=0.50)

    def additional(self):
        self.label1 = Label(self.frame1,
                            text=f'BEM VINDO(A) AO \nAPLICATIVO QUE TE AJUDA A\nORGANIZAR SUA \nVIDA ACADÊMICA!',
                            fg=colors(5), bg=colors(2),
                            font=('Calibri', 15, 'bold'))
        self.label1.place(relx=0.05, rely=0.02)
        self.label2 = Label(self.frame1, text='Selecione uma das opções abaixo', fg=colors(5), bg=colors(2),
                            font=('Calibri', 12))
        self.label2.place(relx=0.12, rely=0.37)

    #def menu(self):
        #menubar = Menu(self.window)
        #self.window.config(menu=menubar)
        #filemenu = Menu(menubar, tearoff=0)
        #filemenu2 = Menu(menubar, tearoff=0)

        #def quit():
            #self.window.destroy()

        #menubar.add_cascade(label='Opções', menu=filemenu)
        #menubar.add_cascade(label='Idioma', menu=filemenu2)
        #filemenu.add_command(label='Sair', command=quit)
        #filemenu2.add_command(label='Português')
        #filemenu2.add_command(label='Inglês')


class Window_schedule:
    def __init__(self):
        self.all_days, self.number_day, self.name_day = None, None, None
        self.frame1, self.label1, self.frame2 = None, None, None
        window1 = tkinter.Toplevel()
        self.window = window1
        self.screen()
        self.frame()
        self.label()
        self.days_month()
        self.window.mainloop()

    def screen(self):
        self.window.title('Agenda de acompanhamento')
        self.window.configure(background=colors(1))
        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()
        self.window.geometry(f'{largura}x{altura}')
        self.window.state('zoomed')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)
        self.frame2 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame2.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def label(self):
        self.label1 = Label(self.frame1, text=f'Agenda de {date_month()[0]}/{year}!', fg=colors(5),
                            font=('Calibri', 15, 'bold'),
                            bg=colors(2))
        self.label1.place(relx=0.35, relwidth=0.30)

    def days_month(self):
        self.all_days, self.number_day, self.name_day = [], [], []
        control, relx, rely = 0, 0.02, 0.02
        max_width = 100
        for day in range(1, date_month()[1] + 1):
            self.number_day.append(day)
            self.name_day.append(day)
        for number in range(len(self.number_day)):
            self.all_days.append(number)
            self.all_days[number] = Frame(self.frame2, bd=1, bg=colors(4))
        while True:
            if control >= len(self.all_days):
                break
            else:
                if max_width >= 2:
                    self.name_day[control] = Label(self.frame2, text=f'Dia {self.number_day[control]}', fg=colors(5),
                                                   bg=colors(3),
                                                   font=('Calibri', 10, 'bold'))
                    self.name_day[control].place(relx=relx + 0.035, rely=rely - 0.015, relheight=0.02)
                    self.all_days[control].place(relx=relx, rely=rely + 0.015, relwidth=0.10, relheight=0.20)
                    max_width -= 14
                    relx += 0.12
                    control += 1
                else:
                    max_width = 100
                    rely += 0.24
                    relx = 0.02


class Window_category:
    def __init__(self):
        window2 = tkinter.Toplevel()
        self.frame1, self.list, self.scrollbar_list = None, None, None
        self.window = window2
        self.frame()
        self.tree_view()
        self.screen()
        self.window.mainloop()

    def screen(self):
        self.window.title('Categorias')
        self.window.configure(background=colors(1))
        self.window.geometry('321x321+400+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)

    def frame(self):
        self.frame1 = Frame(self.window, bg=colors(2), bd=1, highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.10, rely=0.10, relwidth=0.80, relheight=0.80)

    def tree_view(self):
        self.list = ttk.Treeview(self.frame1, height=3, columns=('Nome da categoria', 'Meta'), selectmode='browse',
                                 show='headings')
        self.list.heading('#0', text='')
        self.list.heading('#1', text='Categorias')
        self.list.heading('#2', text='Metas')
        self.list.column('#0', width=1, minwidth=1, stretch=NO)
        self.list.column('#1', width=130, minwidth=130, stretch=NO)
        self.list.column('#2', width=90, minwidth=90, stretch=NO)
        self.list.place(relx=0.04, rely=0.4, relwidth=0.92, relheight=0.58)
        #self.scrollbar_list = Scrollbar(self.frame1, orient='vertical')
        #self.scrollbar_list.place(relx=0.94, rely=0.40, relwidth=0.06, relheight=0.579)


a = Window_main()
