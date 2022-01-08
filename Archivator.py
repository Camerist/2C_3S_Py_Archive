from typing import Sized
import zipfile
import os
from tkinter import Tk     #из tkinter импортировать Tk для Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import*
import tkinter.font as font     #добавляем библиотеку для настроек шрифта

def btn_click_1():
    Tk().withdraw() # нам не нужен полный графический интерфейс, поэтому не показываем корневое окно
    filename = askopenfilename() # показать диалоговое окно "Открыть" и вернуть путь к выбранному файлу

    print(filename);

    myzip=zipfile.ZipFile("test.zip",'w') #название файла, после архивации ( 'w' - программа понимает, что файл создаётся)
    myzip.write(filename) #Файл для архивации
    myzip.close()


def btn_click_2():
    extract_dir = 'P' #путь для файла из архива
    with zipfile.ZipFile('test.zip') as zf: #название архива
        zf.extractall(extract_dir)


root = Tk()
root['bg']='#8eacbb'
root.title('Archivator')
root.geometry('800x600')
root.config(bg='black')

img = PhotoImage (file = "./1.png")
label = Label(root, image= img)
label.place(x=0, y=0)

root.resizable(width=False, height=False)

canvas = Canvas(root, height=800, width=600)
canvas.pack()

frame=Frame(root, ) #bg=img
frame.place( relwidth=1, relheight=1)

myFont = font.Font(size=24)

btn = Button(frame,  text='Выбрать файл...', bg='darksalmon',border=0, command=btn_click_1)
btn.place(relx=.5, rely=.3, anchor="c", height=100, width=300, bordermode=OUTSIDE)

btn ['font'] = myFont

btn = Button(frame, text='Разархивировать', bg='darksalmon',border=0, command=btn_click_2)
btn.place(relx=.5, rely=.5, anchor="c", height=100, width=300, bordermode=OUTSIDE)

btn ['font'] = myFont

root.mainloop()
