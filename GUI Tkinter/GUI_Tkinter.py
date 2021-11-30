from tkinter import *

click = 0
def clickerP(event):
    global click
    click += 1
    lbl.configure(text = click)
    pass

def clickerM(event):
    global click
    click -= 1
    if click <= 0:
        click = 0
        lbl.configure(text = 'Вы пришли в начало начал..')
    else:
        lbl.configure(text = click)

def textToLbl(event):
    text = ent.get()
    lbl.configure(text = text)
    ent.delete(0, END)

def choice():
    cho = str(var.get()) # value 1, 2 or 3
    ent.insert(END, cho+', ') # добавить в textbox

window = Tk()
window.title('Название окна')
window.geometry('600x400') # указывается в пикселях

btn = Button(window, text = 'Нажми на меня', font = 'Arial 20', fg = 'red', bg = 'lightblue', width = 20, height = 3)
lbl = Label(window, text = 'Клик: ')
ent = Entry(window, fg = 'blue', width = 20, font = 'Arial 20')
var = IntVar() # StringVar() - текст
var.set(3) # выбирает третью кнопку
r1 = Radiobutton(window, text = 'Первый', variable = var, value = 1, command = choice)
r2 = Radiobutton(window, text = 'Второй', variable = var, value = 2, command = choice)
r3 = Radiobutton(window, text = 'Третий', variable = var, value = 3, command = choice)

btn.bind('<Button-1>', clickerP) # -1 - нажатие ЛКМ, -2 - СКМ, -3 - ПКМ
btn.bind('<Button-3>', clickerM)
ent.bind('<Return>', textToLbl) # нажатие на enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side = LEFT)
r2.pack(side = LEFT)
r3.pack(side = LEFT)
window.mainloop()