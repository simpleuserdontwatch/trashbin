from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import getpass
import pathlib
root = Tk()
age2 = open('age.txt')
age3 = int(age2.read())
age2.close()
x,y = 0,0
happiness = 50
def feed():
    global happiness
    filepath = filedialog.askopenfilename()
    if filepath:
        os.remove(filepath)
        happiness += 1
        addpopup(m_list[3])
def caress():
    global happiness
    addpopup(m_list[1])
    happiness += 5
def razz():
    global happiness
    addpopup(m_list[2])
    happiness -= 5
def addpopup(message):
    popup = Toplevel(root)
    root.attributes('-topmost', True)
    popup.overrideredirect(1)
    f = Label(popup,text=message)
    f.pack()
    popup.geometry(f'{f.winfo_reqwidth()}x{f.winfo_reqheight()}+{root.winfo_x()}+{root.winfo_y()+48}')
    root.after(1500,popup.destroy)
def edit():
    os.startfile(str(pathlib.Path(__file__).parent.resolve())+"\\messages\\messages.txt")
def reload():
    global messages, m_list
    messages = open('messages/messages.txt')
    m_list = messages.read().splitlines()
    messages.close()
def save():
    with open('age.txt', 'a+') as f:
        f.truncate(0)
        f.write(str(age3))
def menu(e):
    popup = Toplevel(root)
    popup.title('Menu')
    popup.geometry(f'+{root.winfo_x()+48}+{root.winfo_y()+48}')
    popup.attributes('-toolwindow', True)
    ttk.Label(popup,text="Trash bin happiness").pack()
    ttk.Label(popup,image=chart_ico).pack()
    progress = ttk.Progressbar(popup,orient=HORIZONTAL, length=100, mode='determinate',value=happiness)
    progress.pack()
    hap = ttk.Label(popup,text=str(happiness)+'%')
    hap.pack()
    ttk.Label(popup,text="Age: "+str(age3)).pack()
    ttk.Label(popup,text="Actions").pack()
    ttk.Button(popup, text="Feed it.", command=feed).pack()
    ttk.Button(popup, text="Say a compliment.", command=caress).pack()
    ttk.Button(popup, text="Say a insult.", command=razz).pack()
    ttk.Label(popup,text="Misc.").pack()
    ttk.Button(popup, text="Edit messages.", command=edit).pack()
    ttk.Button(popup, text="Reload messages.", command=reload).pack()
    ttk.Button(popup, text="Save age.", command=save).pack()
    ttk.Button(popup, text="Close.", command=root.destroy).pack()
def drag(e):
    root.geometry(f'+{root.winfo_pointerx() - x}+{root.winfo_pointery() - y}')
def start_drag(e):
    global x, y
    x = e.x
    y = e.y
def drainH():
    global happiness
    if happiness > 1:
        happiness -= 0.5
    else:
        addpopup(':(')
    if happiness > 75:
        addpopup(':)')
    root.after(1500,drainH)
def age():
    global age
    age += 1
    addpopup(m_list[4].replace('{user}', getpass.getuser()))
    root.after(1800000,age)
root.geometry('48x48')
root.after(1500,drainH)
root.after(1800000,age)
root.overrideredirect(1)
root.attributes('-topmost', True)
trash = Image.open("skin/icon.png")
trash_ico = ImageTk.PhotoImage(trash)
chart = Image.open("images/chart.png")
chart_ico = ImageTk.PhotoImage(chart)
messages = open('messages/messages.txt')
m_list = messages.read().splitlines()
messages.close()
trashbin = Label(image=trash_ico)
trashbin.pack()
root.attributes('-transparentcolor','#f0f0f0')
addpopup(m_list[0].replace('{user}',getpass.getuser()))
trashbin.bind('<Button-3>',menu)
trashbin.bind('<Button-1>',start_drag)
trashbin.bind('<B1-Motion>',drag)

root.mainloop()
