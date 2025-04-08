from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText



filename = None

def warning_save():
    t = text.get(1.0, END)
    if t.strip():
        response = messagebox.askyesnocancel("Notepad", "Хотите сохранить изменения?")
        if response == None:
            return
        elif response:
            saveAs()

#Функция создания нового файла
def newFile():
    global filename
    filename = "Untitled"
    t = text.get(1.0, END)
    if t.strip():
        response = messagebox.askyesnocancel("Notepad", "Хотите сохранить изменения?")
        if response == None:
            return
        elif response:
            saveAs()
    text.delete(1.0, END)
    filename = None
    
    

#Функция сохранения файла
def saveFile():
    global filename
    t = text.get(1.0, END)
    with open(filename, "w") as f:
        f.write(t)
    
#Функция сохранения как
def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    t = text.get(1.0, END)
    
    try:
        f.write(t.rstrip())
    except:
        showerror(title='Oops!', message='Unable to save file...')

#Функция открытия файла
def openFile():
    f = filedialog.askopenfile(mode='r')
    if f is None:
        return
    t = f.read()
    text.delete(1.0, END)
    text.insert(1.0, t)
    
#Функция завершения программы
def exit_programm():
    if messagebox.askyesno("Text Editor", "Хотите сохранить изменения?"):
        saveAs()
        root.destroy()
        root.quit()
    else:
        root.destroy()
        root.quit()

root = Tk()
root.title("Text Editor by Chix ")
root.minsize(400, 400)
root.maxsize(800, 600)

#Панелька для нумерации
numbers = Text(root, width=4, bg="#1e1e1e", state=DISABLED, relief=FLAT)
numbers.grid(row=0, column=0, sticky="NS")

scroll = Scrollbar(root)
scroll.grid(row=0, column=2, sticky="NS")


text = Text(root, width=400, height=400, bg="#1e1e1e", fg="#d4d4d4", wrap=None)
text.grid(row=0, column=2, sticky="NSWE")

#text.pack()

menubar = Menu(root, bg="#252526", fg="white")
root.config(menu=menubar)

#Меню FILE
filemenu = Menu(menubar, tearoff=0, bg="#252526", fg="white")
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=exit_programm)



#Меню THEMES
themesmenu = Menu(menubar, tearoff=0)
themesmenu.add_command(label="Зеленый")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Themes", menu=themesmenu)


# Горячие клавиши
root.bind("<Control-s>", lambda e: saveAs())
root.bind("<Control-o>", lambda e: openFile())
root.bind("<Control-z>", lambda e: text.edit_undo())


root.protocol("WM_DELETE_WINDOW", exit_programm)
root.mainloop()
