import datetime
from tkinter import messagebox
from tkinter import *
from tkinter import colorchooser
from database import *

date = datetime.datetime.now()
month = date.month
year = date.year
day = date.day
bd = Database()


def date_month():
    match month:
        case 1:
            return 'janeiro', 31, day
        case 2:
            return 'fevereiro', 28, day
        case 3:
            return 'março', 31, day
        case 4:
            return 'abril', 30, day
        case 5:
            return 'maio', 31, day
        case 6:
            return 'junho', 30, day
        case 7:
            return 'julho', 31, day
        case 8:
            return 'agosto', 31, day
        case 9:
            return 'setembro', 30, day
        case 10:
            return 'outubro', 31, day
        case 11:
            return 'novembro', 30, day
        case 12:
            return 'dezembro', 31, day


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


def max_char(limit, arg, field, parent):
    arg = arg.get()
    if len(arg) >= limit:
        messagebox.showerror('Erro', f'O campo em questão só permite {limit} caracteres', parent=parent)
        field.delete(0, END)


def show_tree(treeview):
    bd.connect()
    total = bd.simple_select('CATEGORY', 'id_cat')
    if total == 0:
        pass
    else:
        items = bd.show_cat()
        for cate in range(0, total):
            treeview.tag_configure(f'{items[cate - 1][1]}', background=colors(1), foreground=items[cate - 1][1])
            treeview.insert('', 'end', values=(items[cate - 1][0], 'a', 'a'), tags=(f'{items[cate - 1][1]}',))
    bd.disconnect()


class Complementar_tree:
    def __init__(self):
        self.hex_col, self.selection = None, None

    def tree_color(self):
        color = colorchooser.askcolor()
        self.hex_col = color[1]

    def tree_insert(self, limit, arg, field, parent, treeview):
        arg = arg.get()
        if len(arg) >= limit:
            messagebox.showerror('Erro', f'O campo em questão só permite {limit} caracteres.', parent=parent)
            field.delete(0, END)
        elif self.hex_col is None:
            messagebox.showerror('Erro', f'Não foi escolhida uma cor para a categoria.', parent=parent)
        else:
            treeview.tag_configure(f'{self.hex_col}', background=colors(1), foreground=self.hex_col)
            treeview.insert('', 'end', values=(arg, 'a', 'a'), tags=(f'{self.hex_col}',))
            bd.connect()
            bd.insert_cat(arg, self.hex_col)
            self.hex_col = None
            bd.disconnect()

    def delete_tree(self, treeview, parent):
        try:
            self.selection = treeview.selection()[0]
        except IndexError:
            messagebox.showerror('Erro', 'Nenhuma categoria selecionada para exclusão.', parent=parent)
        else:
            treeview.delete(self.selection)
            bd.connect()
            bd.delete_cat(self.selection)
            bd.disconnect()
            self.selection = None
