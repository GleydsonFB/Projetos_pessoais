from functions_interface import *
from tkinter import *
from tkinter import ttk
from database import *
from PIL import Image, ImageTk
import webbrowser

color_helper = Complementar_tree()
base = Database()
base.connect()
base.table_create()
dates = Issue_date()


class Main_window:
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
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.70)
        self.frame2 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame2.place(relx=0.08, rely=0.76, relwidth=0.84, relheight=0.22)
        self.frame3 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame3.place(relx=0.20, rely=0.38, relwidth=0.60, relheight=0.61)

    def button(self):
        self.category = Button(self.frame1, text='Gerenciar categorias', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Category_window)
        self.category.place(relx=0.225, rely=0.40, relwidth=0.55)
        self.category = Button(self.frame1, text='Consultar agenda', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'),
                               command=Schedule_window)
        self.category.place(relx=0.225, rely=0.50, relwidth=0.55)
        self.category = Button(self.frame1, text='Definir metas', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Goal_window)
        self.category.place(relx=0.225, rely=0.60, relwidth=0.55)
        self.category = Button(self.frame1, text='Escolher regras', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Rule_window)
        self.category.place(relx=0.225, rely=0.70, relwidth=0.55)
        self.category = Button(self.frame1, text='Feedback/FAQ', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'))
        self.category.place(relx=0.225, rely=0.80, relwidth=0.55)
        self.category = Button(self.frame1, text='LinkedIn do desenvolvedor', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=lambda: webbrowser.open('https://www.linkedin.com/in/gleydsonfreitas/', new=2))
        self.category.place(relx=0.225, rely=0.90, relwidth=0.55)

    def additional(self):
        self.label1 = Label(self.frame1,
                            text=f'BEM VINDO(A) AO \nAPLICATIVO QUE TE AJUDA A\nORGANIZAR SUA \nVIDA ACADÊMICA!',
                            fg=colors(5), bg=colors(2),
                            font=('Calibri', 15, 'bold'))
        self.label1.place(relx=0.05, rely=0.01)
        self.label2 = Label(self.frame1, text='Selecione uma das opções abaixo', fg=colors(5), bg=colors(2),
                            font=('Calibri', 12))
        self.label2.place(relx=0.12, rely=0.30)


class Schedule_window:
    def __init__(self):
        self.all_days, self.number_day, self.name_day = None, None, None
        self.frame1, self.label1, self.frame2 = None, None, None
        self.bt_left, self.bt_right = None, None
        window1 = Toplevel()
        self.window = window1
        self.screen()
        self.frame()
        self.label()
        self.days_month()
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title('Agenda de acompanhamento')
        self.window.configure(background=colors(1))
        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()
        self.window.geometry(f'{largura}x{altura}')
        self.window.state('zoomed')
        self.window.minsize(width=largura, height=altura)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)
        self.frame2 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame2.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def label(self):
        self.label1 = Label(self.frame1, text=f'Agenda de {dates.date_month()[0]}/{year}!', fg=colors(5),
                            font=('Calibri', 15, 'bold'),
                            bg=colors(2))
        self.label1.place(relx=0.35, relwidth=0.30)
        label2 = Label(self.frame1, text='Registre uma folga para o dia', fg=colors(5), font=('Calibri', 11, 'bold'),
                       bg=colors(2))
        label2.place(relx=0.70, rely=0.945)

    def button(self):
        #images for buttons
        load_img1 = Image.open('images/b_left_schudule.png')
        resize_img1 = load_img1.resize((40, 40))
        self.bt_left = ImageTk.PhotoImage(resize_img1)
        load_img2 = Image.open('images/b_right_schedule.png')
        resize_img2 = load_img2.resize((40, 40))
        self.bt_right = ImageTk.PhotoImage(resize_img2)

        #simple buttons
        button1 = Button(self.frame1, text='Registrar estudo', fg=colors(5), font=('Calibri', 11, 'bold'),
                         bg=colors(2), command=Registry_window)
        button1.place(relx=0.40, rely=0.945, relwidth=0.10)
        button2 = Button(self.frame1, text='Apagar estudo', fg=colors(5), font=('Calibri', 11, 'bold'),
                         bg=colors(2), command=Remove_elem_window)
        button2.place(relx=0.50, rely=0.945, relwidth=0.10)
        button5 = Button(self.frame1, text='Inserir folga', fg=colors(5), font=('Calibri', 9, 'bold'),
                         bg=colors(2))
        button5.place(relx=0.89, rely=0.945, relwidth=0.08)
        button6 = Button(self.frame1, text='Inserir comentário', fg=colors(5), font=('Calibri', 9, 'bold'),
                         bg=colors(2), command=Commentary_window)
        button6.place(relx=0.03, rely=0.945, relwidth=0.10)

        #custom buttons
        button3 = Button(self.window, image=self.bt_left, bg=colors(2), borderwidth=0)
        button3.place(relx=0.045, rely=0.042)
        button4 = Button(self.window, image=self.bt_right, bg=colors(2), borderwidth=0)
        button4.place(relx=0.925, rely=0.042)

    def days_month(self):
        self.all_days, self.number_day, self.name_day = [], [], []
        control, relx, rely = 0, 0.02, 0.02
        max_width = 100
        for days in range(1, dates.date_month()[1] + 1):
            self.number_day.append(days)
            self.name_day.append(days)
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

            #combo days for day offs
            list_day = dates.day_registry()
            combo1 = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
            combo1.set(list_day[dates.date_month()[2] - 1])
            combo1.place(relx=0.85, rely=0.95, relwidth=0.03)


class Category_window:
    def __init__(self):
        window2 = Toplevel()
        self.hex_col, self.frame1, self.listt = None, None, None
        self.var = StringVar()
        self.window = window2
        self.frame()
        self.tree_view()
        self.field()
        self.entry_button()
        self.screen()
        self.window.mainloop()

    def screen(self):
        self.window.title('Categorias')
        self.window.configure(background=colors(1))
        self.window.geometry('321x321+400+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bg=colors(1))
        self.frame1.place(relx=0.10, rely=0.10, relwidth=0.80, relheight=0.80)

    def tree_view(self):
        style = ttk.Style()
        style.theme_use('classic')
        style.configure("Treeview.Heading", background=colors(5), foreground=colors(1))
        style.configure('Treeview', foreground='black', fieldbackground=colors(1), font=('calibri', 12, 'bold'))
        style.map('Treeview', background=[('selected', colors(3))])
        style.configure('Scrollbar')
        self.listt = ttk.Treeview(self.frame1, height=3, columns=('Nome da categoria', 'vazio'), selectmode='browse',
                                  show='headings')
        self.listt.heading('#0', text='')
        self.listt.heading('Nome da categoria', text='Categorias cadastradas')
        self.listt.heading('vazio', text='')
        self.listt.column('#0', width=1, minwidth=1, stretch=NO)
        self.listt.column('Nome da categoria', width=230, minwidth=230, stretch=NO, anchor='c')
        self.listt.column('vazio', width=1, minwidth=1, stretch=NO)
        self.listt.place(relx=0.04, rely=0.35, relwidth=0.92, relheight=0.58)
        show_tree(self.listt)

        #scrollbar vertical
        scrollbar_list = Scrollbar(self.frame1, orient='vertical', command=self.listt.yview)
        scrollbar_list.place(relx=0.94, rely=0.35, relwidth=0.06, relheight=0.64)

        #scrollbar horizontal
        scrollbar_listh = Scrollbar(self.frame1, orient='horizontal', command=self.listt.xview)
        scrollbar_listh.place(relx=0.04, rely=0.93, relwidth=0.92, relheight=0.06)
        self.listt.configure(yscrollcommand=scrollbar_list.set, xscrollcommand=scrollbar_listh.set)

    def field(self):
        label = Label(self.frame1, text='Digite o nome da nova categoria', font=('Calibri', 10, 'bold'), fg=colors(5), bg=colors(1))
        label.place(relx=0.04, rely=0.10)
        label1 = Label(self.window, text='Gerenciamento de categorias', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(1))
        label1.place(relx=0.125, relwidth=0.75, rely=0.05)

    def entry_button(self):
        entry1 = Entry(self.frame1, textvariable=self.var, bg=colors(5))
        entry1.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.10)
        button2 = Button(self.frame1, text='Escolha a cor', command=color_helper.tree_color, bg=colors(2), fg=colors(5), font=('Calibri', 9, 'bold'))
        button2.place(relx=0.40, rely=0.20, relheight=0.10)
        button1 = Button(self.frame1, text='Insira', bg=colors(2), fg=colors(5), font=('Calibri', 9, 'bold'),
                         command=lambda: color_helper.tree_insert(12, self.var, entry1, self.window, self.listt))
        button1.place(relx=0.75, rely=0.20, relheight=0.10)
        button3 = Button(self.window, text='Remover selecionada', bg=colors(2), fg=colors(5), font=('Calibri', 9, 'bold'),
                         command=lambda: color_helper.delete_tree(self.listt, self.window))
        button3.place(relx=0.20, rely=0.90, relwidth=0.60)


class Registry_window:
    def __init__(self):
        window3 = Toplevel()
        self.frame1 = None
        self.var = StringVar()
        self.window = window3
        self.screen()
        self.frame()
        self.insert_time()
        self.label()
        self.window.mainloop()

    def screen(self):
        self.window.title('Registrar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5)
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def insert_time(self):
        #for tests
        listt = ['English', 'Physic', 'Programing']

        #combo and entry
        combo = ttk.Combobox(self.frame1, values=listt, state='readonly', background=colors(5))
        combo.set(listt[0])
        combo.place(relx=0.25, rely=0.18, relwidth=0.50)
        entry = Entry(self.frame1, textvariable=self.var, bg=colors(5))
        entry.place(relx=0.375, rely=0.38, relwidth=0.25)
        button = Button(self.frame1, text='Inserir', command=lambda: max_char(5, self.var, entry, self.window),
                        bg=colors(2), fg=colors(5), font=('Calibri', 13, 'bold'))
        button.place(relx=0.375, rely=0.80, relwidth=0.25)

        #date registry
        list_day = dates.day_registry()
        combo1 = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
        combo1.set(list_day[dates.date_month()[2] - 1])
        combo1.place(relx=0.25, rely=0.60, relwidth=0.15)

    def label(self):
        label1 = Label(self.frame1, text='Escolha a categoria', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label1.place(relx=0.25, relwidth=0.50, rely=0.05)
        label2 = Label(self.frame1, text='Defina o tempo estudado', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label2.place(relx=0.125, rely=0.25, relwidth=0.75)
        label3 = Label(self.frame1, text='Determine a data do estudo', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label3.place(relx=0.15, rely=0.45)
        label4 = Label(self.frame1, text=f'/{dates.date_month()[0]}/{year}', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label4.place(relx=0.40, rely=0.60)


class Commentary_window:
    def __init__(self):
        window3 = Toplevel()
        self.frame1 = None
        self.var = StringVar()
        self.window = window3
        self.screen()
        self.frame()
        self.insert_comment()
        self.label()
        self.window.mainloop()

    def screen(self):
        self.window.title('Comentar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5)
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def insert_comment(self):
        #combo and entry
        day_list = dates.day_registry()
        combo = ttk.Combobox(self.frame1, values=day_list, state='readonly', background=colors(5))
        combo.set(dates.day_registry()[day - 1])
        combo.place(relx=0.425, rely=0.18, relwidth=0.15)
        comment_text = Text(self.frame1, bg=colors(5), font=('calibri', 10), foreground='green')
        comment_text.place(relx=0.10, rely=0.38, relwidth=0.80, relheight=0.41)
        button = Button(self.frame1, text='Inserir',
                        command=lambda: max_comment(254, comment_text.get(1.0, 'end-1c'), comment_text, self.window, combo.get(), dates.date_month()[0], year),
                        bg=colors(2), fg=colors(5), font=('Calibri', 13, 'bold'))
        button.place(relx=0.375, rely=0.80, relwidth=0.25)

    def label(self):
        label1 = Label(self.frame1, text='Escolha o dia para registrar o comentário', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label1.place(relx=0.00, rely=0.05)
        label2 = Label(self.frame1, text='Faça seu comentário', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label2.place(relx=0.125, rely=0.25, relwidth=0.75)


class Remove_elem_window:
    def __init__(self):
        window4 = Toplevel()
        self.frame1 = None
        self.var = StringVar()
        self.window = window4
        self.screen()
        self.frame()
        self.label_button()
        self.tree_view()
        self.window.mainloop()

    def screen(self):
        self.window.title('Apagar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5) + 322
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def label_button(self):
        label = Label(self.frame1, text='escolha o dia do mês', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label.place(relx=0.25, rely=0.06, relwidth=0.50)
        label1 = Label(self.frame1, text=f'/{dates.date_month()[0]}/{year}', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label1.place(relx=0.40, rely=0.20)
        list_day = dates.day_registry()
        combo1 = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
        combo1.set(list_day[dates.date_month()[2] - 1])
        combo1.place(relx=0.25, rely=0.20, relwidth=0.15)
        button = Button(self.frame1, text='Buscar', bg=colors(2), fg=colors(5), font=('Calibri', 10, 'bold'))
        button.place(relx=0.40, rely=0.30, relwidth=0.20)

    def tree_view(self):
        style = ttk.Style()
        style.theme_use('classic')
        style.configure("Treeview.Heading", background=colors(3), foreground=colors(1))
        style.configure('Treeview', fieldbackground=colors(5), font=('calibri', 12, 'bold'))
        style.map('Treeview', background=[('selected', colors(1))])
        style.configure('Scrollbar')
        treeview = ttk.Treeview(self.frame1, height=3, columns=('Duração', 'Categoria'), selectmode='browse',
                                show='headings')
        treeview.heading('#0', text='')
        treeview.heading('Duração', text='Duração')
        treeview.heading('Categoria', text='Categoria')
        treeview.column('#0', width=1, minwidth=1, stretch=NO)
        treeview.column('Duração', width=50, minwidth=50, stretch=NO)
        treeview.column('Categoria', width=211, minwidth=210, stretch=NO, anchor='c')
        treeview.place(relx=0.04, rely=0.40, relwidth=0.92, relheight=0.50)
        button_tree = Button(self.frame1, text='Remover registro', bg=colors(2), fg=colors(5), font=('Calibri', 10, 'bold'))
        button_tree.place(relx=0.30, rely=0.905, relwidth=0.40)


class Goal_window:
    def __init__(self):
        window5 = Toplevel()
        self.frame1 = None
        self.var, self.category, self.month, self.year = StringVar(), StringVar(), StringVar(), StringVar()
        self.window = window5
        self.screen()
        self.frame()
        self.label()
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title('Definir metas')
        self.window.configure(background=colors(1))
        self.window.geometry(f'300x300+400+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=300, height=300)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    def label(self):
        label1 = Label(self.frame1, text='Escolha a categoria', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label1.place(relx=0.10, rely=0.05)
        label2 = Label(self.frame1, text='Tempo de estudo mensal', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label2.place(relx=0.10, rely=0.30)
        label3 = Label(self.frame1, text='em minutos', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label3.place(relx=0.21, rely=0.45)
        label4 = Label(self.frame1, text='Escolha o mês e o ano', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label4.place(relx=0.10, rely=0.60)

    def button(self):
        content_combo = insert_combo()
        combo = ttk.Combobox(self.frame1, values=content_combo, state='readonly', background=colors(5), textvariable=self.category)
        combo.place(relx=0.10, rely=0.20)
        entry = Entry(self.frame1, bg=colors(5), textvariable=self.var)
        entry.place(relx=0.10, rely=0.45, relwidth=0.10)
        mon = month_combo()
        combo2 = ttk.Combobox(self.frame1, values=mon, state='readonly', background=colors(5), textvariable=self.month)
        combo2.set(mon[month - 1])
        combo2.place(relx=0.10, rely=0.70, relwidth=0.30)
        yea = year_combo()
        combo3 = ttk.Combobox(self.frame1, values=yea, state='readonly', background=colors(5), textvariable=self.year)
        combo3.set(yea[year - 2023])
        combo3.place(relx=0.45, rely=0.70, relwidth=0.20)
        button = Button(self.frame1, text='Registrar meta', bg=colors(2), fg=colors(5),
                        font=('Calibri', 12, 'bold'), command=lambda: insert_goal(self.var, entry, self.window, self.month.get(), self.year.get()
                                                                                  , self.category.get()))
        button.place(relx=0.30, relwidth=0.40, rely=0.85)


class Rule_window:
    def __init__(self):
        window5 = Toplevel()
        self.frame1, self.frame_rules, self.frame_conditions, self.frame4 = None, None, None, None
        self.var, self.category, self.month, self.year = StringVar(), StringVar(), StringVar(), StringVar()
        self.window = window5
        self.screen()
        self.frame()
        self.label()
        self.window.mainloop()

    def screen(self):
        self.window.title('Estabelecer regras')
        self.window.configure(background=colors(1))
        self.window.geometry(f'600x600+725+50')
        self.window.maxsize(width=600, height=600)
        self.window.minsize(width=600, height=600)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)
        self.frame_rules = Frame(self.frame1, bd=1, bg=colors(5), highlightbackground=colors(2), highlightthickness=2)
        self.frame_rules.place(relx=0.02, rely=0.04, relwidth=0.45, relheight=0.92)
        self.frame_conditions = Frame(self.frame1, bd=1, bg=colors(5), highlightbackground=colors(2), highlightthickness=2)
        self.frame_conditions.place(relx=0.53, rely=0.04, relwidth=0.45, relheight=0.92)
        self.frame4 = Frame(self.frame1, bd=1, bg=colors(1), highlightbackground=colors(2), highlightthickness=2)
        self.frame4.place(relx=0.45, rely=0.04, relwidth=0.09, relheight=1)

    def label(self):
        label = Label(self.window, text='Regras e condições',  bg=colors(2), fg=colors(5), font=('Calibri', 12, 'bold'))
        label.place(relx=0.375, rely=0.045, relwidth=0.25, relheight=0.03)
        label_rule1 = Label(self.frame_rules, text='Escolha o modelo de estudo ideal', bg=colors(5), fg=colors(2),
                            font=('Calibri', 11, 'bold'))
        label_rule1.place(relx=0.02)
        label_condition1 = Label(self.frame_conditions, text='Defina a efetividade do estudo', bg=colors(5), fg=colors(2),
                                 font=('Calibri', 11, 'bold'))
        label_condition1.place(relx=0.10, relwidth=0.80)

a = Main_window()
base.disconnect()