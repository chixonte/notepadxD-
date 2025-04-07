from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfilename(mode='w', defaulttextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='Oops!', message='Unable to save file...')

def openFile():
    try:
        f = filedialog.askopenfile(mode='r')
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
    except:
        print("Не выбран файл!")
        messagebox.showinfo("Text Editor by Chix", "Файл не был выбран!")

    

root = Tk()
root.title("Text Editor by Chix")
root.minsize(400, 400)
root.maxsize(800, 600)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

themesmenu = Menu(menubar, tearoff=0)
themesmenu.add_command(label="Зеленый")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Themes", menu=themesmenu)


root.mainloop()
