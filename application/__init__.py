import Tkinter as tk
# import ObjectManagement as om
import sys
# sys.path.append('./controllers')
import os
from controllers import controller
from settings import *
# from views import view


root = tk.Tk()
app = controller.MainApplication(root)
eyes_path = 'application/static/images/'
eyes_name = 'brown-favicon.ico'
full_path = os.path.abspath(os.path.join(eyes_path, eyes_name))
app.parent.iconbitmap(full_path)										# Change App Icon
app.parent.title( "SmartPartner" ) 										# Change App Title
app.parent.geometry('{}x{}'.format(1000, 770))							# Change Windows Size
app.parent.resizable(width=False, height=False)							# Change Resizable Settings
app.parent.configure(background='black')								# Change Background Color

menubar = tk.Menu(app.parent)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=controller.f2)
filemenu.add_command(label="Open", command=controller.donothing)
filemenu.add_command(label="Save", command=controller.donothing)
filemenu.add_command(label="Save as...", command=controller.donothing)
filemenu.add_command(label="Close", command=controller.donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app.parent.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=controller.donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=controller.donothing)
editmenu.add_command(label="Copy", command=controller.donothing)
editmenu.add_command(label="Paste", command=controller.donothing)
editmenu.add_command(label="Delete", command=controller.donothing)
editmenu.add_command(label="Select All", command=controller.donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=controller.donothing)
helpmenu.add_command(label="About...", command=controller.donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.parent.config(menu=menubar)
# app.mainloop()

