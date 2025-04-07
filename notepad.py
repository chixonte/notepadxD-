from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

filename = None

#Функция создания нового файла
def newFile():
    global filename
    filename = "Untitled"
    t = text.get(0.0, END)
    if messagebox.askyesnocancel("Notepad", "Хотите сохранить изменения?"):
        saveAs()
    text.delete(0.0, END)
    
    

#Функция сохранения файла
def saveFile():
    global filename
    t = text.get(0.0, END)
    with open(filename, "w") as f:
        f.write(t)
    
#Функция сохранения как
def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    t = text.get(0.0, END)
    
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
    text.delete(0.0, END)
    text.insert(0.0, t)
    
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

text = ScrolledText(root, width=400, height=400, bg="#1e1e1e", fg="#d4d4d4")
text.pack()

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









root.protocol("WM_DELETE_WINDOW", exit_programm)
root.mainloop()
