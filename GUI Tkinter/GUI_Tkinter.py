from tkinter import *
from tkinter import ttk

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

def newWindow(ind: int):
    window2 = Toplevel()
    window2.title('Настройки')
    #window2.geometry('300x200')
    tabs = ttk.Notebook(window2)
    texts = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
    textn = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
    tabn = ['tab0', 'tab1', 'tab2', 'tab3', 'tab4']
    cann = ['can0', 'can1', 'can2', 'can3', 'can4']

    for i in range(len(texts)):
        tabn[i] = Frame(tabs)
        textn[i] = PhotoImage(file = texts[i]).subsample(1)
        tabs.add(tabn[i], text = texts[i])
        cann[i] = Canvas(tabn[i], height = 600, width = 800)
        cann[i].create_image(0,0, image = textn[i], anchor = NW)
        cann[i].pack()

    tabs.grid(row = 0, column = 0)
    tabs.select(ind)
    window2.mainloop()


window = Tk()
window.title('Кликкер')
window.geometry('600x400') # указывается в пикселях

menu = Menu(window)
window.config(menu = menu)
m1 = Menu(menu)
menu.add_cascade(label = 'Tabs', menu = m1)
m1.add_command(label = 'Image1', accelerator = 'Command+A', command = lambda:newWindow(0))
m1.add_command(label = 'Image2', command = lambda:newWindow(1))
m1.add_command(label = 'Image3', command = lambda:newWindow(2))
m1.add_command(label = 'Image4', command = lambda:newWindow(3))
m1.add_command(label = 'Image5', command = lambda:newWindow(4))
m1.add_separator()


btn = Button(window, text = 'Нажми на меня', font = 'Arial 20', fg = 'red', bg = 'lightblue', width = 20, height = 3, relief = SUNKEN)
btn2 = Button(window, text = 'Открыть окно', font = 'Arial 20', fg = 'green', bg = 'lightyellow', width = 20, height = 3, command = lambda:newWindow(3)).pack()

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