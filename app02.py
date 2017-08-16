import Tkinter as tk
# import ObjectManagement as om
import sys
sys.path.append('./modules')
import ObjectManagement as om

# import PostButton from './ObjectManagement'
# import GetOneButton from './ObjectManagement'
# import GetAllButton from './ObjectManagement'
# import DeleteOneButton from './ObjectManagement'

# class Demo1:
	# def __init__(self, master):
		# self.master = master
		# self.frame = tk.Frame(self.master)
		# self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
		# self.button1.pack()
		# self.frame.pack()
	# def new_window(self):
		# self.newWindow = tk.Toplevel(self.master)
		# self.app = Demo2(self.newWindow)

# class Demo2:
	# def __init__(self, master):
		# self.master = master
		# self.frame = tk.Frame(self.master)
		# self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
		# self.quitButton.pack()
		# self.frame.pack()
	# def close_windows(self):
		# self.master.destroy()

		
# ==================================
# Show GIF Animation
# ==================================
from PIL import Image, ImageTk, ImageSequence

class Animation:
	def __init__(self, parent):
		self.parent = parent
		self.canvas = tk.Canvas(parent, width=800, height=600, bd=0, highlightthickness=0, relief='ridge')
		self.canvas.pack()
		self.sequence = [ImageTk.PhotoImage(img)
							for img in ImageSequence.Iterator(
								Image.open(
								'./eye/normal.gif'))]
		self.image = self.canvas.create_image(400,300, image=self.sequence[0])
		self.animate(1)
	def animate(self, counter):
		self.canvas.itemconfig(self.image, image=self.sequence[counter])
		self.parent.after(30, lambda: self.animate((counter+1) % len (self.sequence)))
# ==================================
		
# ==================================
# Show Input Text 
# ==================================
import time
# from threading import Thread
import threading
import nltk
# nltk.download()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class InputText(tk.Frame):
			
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.input = tk.Entry(parent, bg="#282B2B", fg="white", width=30)		# Create Entry
		self.input.place(x=10, y=700)											# Change Background Color
		self.parent.bind('<Return>', self.func)
		
		self.all_label = []
		self.y = []
		for i in range(0, 5):
			self.y.append(650 - (20*i))
			self.all_label.append(tk.Label(text="", fg="white", bg="black"))
			self.all_label[i].place(x=10, y=self.y[i])
		self.count = 0
		self.aiTurn = False
		self.aiTextColor = '#1e90ff'
		self.userTextColor = 'yellow'
		
	def func(self, event):
		if self.input.get():													# if input is not ""
			# self.userWords()
			# self.aiWords()
			self.t1 = threading.Thread(target=self.userWords, args = ())
			self.t1.start()
			self.t1.join()
			# self.go_off = threading.Event()
	
	def userWords(self):
		self.result = self.input.get()
		self.input.delete(0, 'end')
		self.input['state'] = 'disabled'
		for i in range(0, 5):
			self.y[i] = self.y[i] - 20
			self.all_label[i].place(x=10, y=self.y[i])
			if self.y[i] <= 550:
				self.y[i] = 650
				self.all_label[i].place(x=10, y=self.y[i])
				self.all_label[i]['fg'] = self.userTextColor
				self.all_label[i]['text'] = self.result
		# self.go_off.set()
		self.aiTurn = True;
		# self.t2 = threading.Thread(target=self.aiWords, args = ())
		self.t2 = threading.Thread(target=self.aiTokenize, args = ())
		self.t2.start()
		self.t2.join()
			
	def aiWords(self):
		# while self.go_off.isSet():
		# while self.aiTurn == True:
		if self.aiTurn == True:
			# time.sleep(1)
			data = []
			data = om.getAll()
			for i in range(0, len(data)):
				# if 'author' in data[i] and self.input.get() in data[i]['author']:
				if 'author' in data[i] and data[i]['author'] == self.result:
					self.result = data[i]['author']
					i = len(data)
					self.result = self.result + " found!"
					for j in range(0, 5):
						self.y[j] = self.y[j] - 20
						self.all_label[j].place(x=10, y=self.y[j])
						if self.y[j] <= 550:
							self.y[j] = 650
							self.all_label[j].place(x=10, y=self.y[j])
							self.all_label[j]['fg'] = self.aiTextColor
							self.all_label[j]['text'] = self.result
			# self.go_off.clear()
			self.input['state'] = 'normal'
			self.aiTurn = False
			
	def aiTokenize(self):
		if self.aiTurn == True:
			# time.sleep(1)
			tokens = nltk.word_tokenize(self.result)
			tagged = nltk.pos_tag(tokens)
			for j in range(0, 5):
				self.y[j] = self.y[j] - 20
				self.all_label[j].place(x=10, y=self.y[j])
				if self.y[j] <= 550:
					self.y[j] = 650
					self.all_label[j].place(x=10, y=self.y[j])
					self.all_label[j]['fg'] = self.aiTextColor
					selectedWord = [(word) for word, tag in tagged if tag in ('NN', 'VB')]
					self.all_label[j]['text'] = selectedWord
					print [(word, tag) for word, tag in tagged if tag in ('NN', 'VB')]
					print tagged
			# self.go_off.clear()
			self.input['state'] = 'normal'
			self.aiTurn = False

# ==================================

# ==================================
# Show Label Text
# ==================================
class LabelText(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.label = tk.Label(text=changeLabel(), fg="white", bg="black")		# Create Label
		self.label.place(x=10, y=650)											# Change Background Color
# ==================================

# ==================================
# Show Update Button
# ==================================
class ChangeLabelButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Change Label", command=changeLabel())	# Create Button
		self.button.place(x=700, y=700)												# Change Button Position
		self.button.config(height=1, width=10)										# Change Button Size
# ==================================

# ==================================
# Update One Data
# ==================================
import pprint
import json
from pymongo import MongoClient		

def changeLabel():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	
	def getFromInput(self):
		return 
	def getFromDB(self):
		data = []
		for post in collection.find():
			data.append(post)
		for i in range(0,len(data)):
			if 'author' in data[i]:
				dataVal = data[i]['author']['Miko']
				i = 2
				return dataVal
		else:
			return "Hello"
# ==================================

# ==================================
# Main Application
# ==================================
class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.animation = Animation(self.parent)
		self.input = InputText(self.parent)
		# self.label = LabelText(self.parent)
		self.post_button = om.PostButton(self.parent)
		# self.getone_button = om.GetOneButton(self.parent)
		# self.getall_button = om.GetAllButton(self.parent)
		# self.delone_button = om.DeleteOneButton(self.parent)
		# self.updateone_button = om.UpdateOneButton(self.parent)		
# ==================================		

def donothing():
	filewin = tk.Toplevel(root)
	button = tk.Button(filewin, text="Do nothing button")
	button.pack()

def f2():
	def post():
		object = []
		object.append(userWords.get())
		object.append(aiWords.get())
		om.postOne(object)
		print object

	parent = tk.Toplevel(root)
	parent.geometry('{}x{}'.format(300, 100))
	userWords = tk.Entry(parent, bg="#282B2B", fg="white", width=30)
	userWords.pack()
	aiWords = tk.Entry(parent, bg="#282B2B", fg="white", width=30)
	aiWords.pack()
	button = tk.Button(parent, text="Post Data", command=post)
	button.pack()


if __name__ == "__main__":
	print "SmartPartner Running..."

	root = tk.Tk()
	app = MainApplication(root)
	app.parent.iconbitmap('brown-favicon.ico')				# Change App Icon
	app.parent.title( "SmartPartner" ) 						# Change App Title
	app.parent.geometry('{}x{}'.format(1000, 770))			# Change Windows Size
	app.parent.resizable(width=False, height=False)			# Change Resizable Settings
	app.parent.configure(background='black')				# Change Background Color

	menubar = tk.Menu(app.parent)
	
	filemenu = tk.Menu(menubar, tearoff=0)
	filemenu.add_command(label="New", command=f2)
	filemenu.add_command(label="Open", command=donothing)
	filemenu.add_command(label="Save", command=donothing)
	filemenu.add_command(label="Save as...", command=donothing)
	filemenu.add_command(label="Close", command=donothing)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=app.parent.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	
	editmenu = tk.Menu(menubar, tearoff=0)
	editmenu.add_command(label="Undo", command=donothing)
	editmenu.add_separator()
	editmenu.add_command(label="Cut", command=donothing)
	editmenu.add_command(label="Copy", command=donothing)
	editmenu.add_command(label="Paste", command=donothing)
	editmenu.add_command(label="Delete", command=donothing)
	editmenu.add_command(label="Select All", command=donothing)
	menubar.add_cascade(label="Edit", menu=editmenu)
	
	helpmenu = tk.Menu(menubar, tearoff=0)
	helpmenu.add_command(label="Help Index", command=donothing)
	helpmenu.add_command(label="About...", command=donothing)
	menubar.add_cascade(label="Help", menu=helpmenu)

	app.parent.config(menu=menubar)
	app.mainloop()
