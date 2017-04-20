from tkinter import *
root = Tk()
root.title("KUVALATOR")
root.geometry("500x500")
app = Frame(root)#РАМКА ДЛЯ РАЗМЕЩЕНИЯ других элементов
app.grid()#менеджер раазмещений
lab = Label(app, text = "вот она я !") #метка
lab.grid()

buttonfirst = Button(app,text = "1")
buttonfirst.grid()

buttontwo = Button(app,text = "2")
buttontwo.grid()

buttonthree = Button(app,text = "3")
buttonthree.grid()
buttonthree.configure(text = "И я тоже")

buttonfor = Frame(root, width = 50, height = 50, bg = "Yellow")
buttonfor.place(x = 100, y = 200, width = 25, height = 25,)
dgddgddjhdgjdgfjhffjdj
