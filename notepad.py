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
            text.delete(1.0, END)

#Функция создания нового файла
def newFile():
    global filename
    filename = "Untitled"
    warning_save()
    filename = None
    
    

#Функция сохранения файла
def saveFile():
    global filename
    if not filename:
        saveAs()
        return
    try:
        with open(filename, "w") as f:
            f.write(text.get(1.0, END))
    except Exception as e:
        messagebox.showerror("Error", f"Не удалось сохранить файл:\n{e}")

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
    warning_save() # cancel не работает
    root.destroy()
    root.quit()

root = Tk()
root.title("Text Editor by Chix ")
root.minsize(400, 400)
root.maxsize(800, 600)

#Панелька для нумерации
numbers = Text(root, width=4, bg="#1e1e1e", fg="#d4d4d4", state=DISABLED, relief=FLAT)
numbers.grid(row=0, column=0, sticky="NS")

def on_yscrollcommand(*args):
    scroll.set(*args)  # Синхронизация скролбара с текстовым полем
    numbers.yview_moveto(args[0])  # Синхронизация поля с номерами с текстовым полем



scroll = Scrollbar(root)
scroll.grid(row=0, column=2, sticky="NS")


text = Text(root, width=400, height=400, yscrollcommand=on_yscrollcommand, bg="#1e1e1e", fg="#d4d4d4", wrap=None)
text.grid(row=0, column=2, sticky="NSWE")

def scroll_command(*args):
    # Движение скролбара управляет отображением текста в обоих текстовых полях
    text.yview(*args)
    numbers.yview(*args)

scroll.config(command=scroll_command)

def insert_numbers():
    count_of_lines = text.get(1.0, END).count('\n') + 1
    
    numbers.config(state=NORMAL)
    numbers.delete(1.0, END)
    numbers.insert(1.0, '\n'.join(map(str, range(1, count_of_lines))))
    numbers.config(state=DISABLED)

insert_numbers()

def on_edit(event):
    # Срабатывает при изменениях в текстовом поле
    insert_numbers()
    text.edit_modified(0)  # Сбрасываем флаг изменения текстового поля


text.bind('<<Modified>>', on_edit)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

menubar = Menu(root, bg="#252526", fg="white")
root.config(menu=menubar)

#Меню FILE
filemenu = Menu(menubar, tearoff=0, bg="#252526", fg="white")
filemenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
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
root.bind("<Control-n>", lambda e: newFile)



root.protocol("WM_DELETE_WINDOW", exit_programm)
root.mainloop()
