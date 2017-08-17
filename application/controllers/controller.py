import Tkinter as tk
# import ObjectManagement as om
import sys
import os
# from application import app
# from application import root

from application.models import model as om
from application.settings import *

from application.views import view
# from application.views import InputText

# ==================================
# Main Application
# ==================================
class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.animation = view.Animation(self.parent)
		self.input = view.InputText(self.parent)
		# self.label = LabelText(self.parent)
		# self.post_button = om.PostButton(self.parent)
		# self.getone_button = om.GetOneButton(self.parent)
		# self.getall_button = om.GetAllButton(self.parent)
		# self.delone_button = om.DeleteOneButton(self.parent)
		# self.updateone_button = om.UpdateOneButton(self.parent)		
# ==================================	

def donothing():
	filewin = tk.Toplevel()
	button = tk.Button(filewin, text="Do nothing button")
	button.pack()

	
import nltk

def f2():

	# def __init__(self, parent, *args, **kwargs):
		# parent = tk.Toplevel()
		# parent.geometry('{}x{}'.format(300, 100))
		# self.input = tk.Entry(parent, bg="#282B2B", fg="white", width=30)		# Create Text Box
		# self.input.place(x=10, y=700)											# Change Background Color
		# self.parent.bind('<Return>', self.post)

	def post(self):
		# object = []
		# object.append(userWords.get())
		# object.append(aiWords.get())
		# om.postOne(object)
		
		tokens = nltk.word_tokenize(userWords.get())
		tagged = nltk.pos_tag(tokens)
		selectedWord = [word for word, tag in tagged if tag in ('NN', 'VB')]
		allWords = [word for word, tag in tagged]

		isText = [word for word, tag in tagged if tag in ('VBZ')]
		print allWords
		try:
			# GET THE VBZ (IS) INDEX
			isIndex = 0
			for i in range(0, len(allWords)):
				if allWords[i] == isText[0]:
					isIndex = i
			try:
				print allWords[isIndex - 1].lower() + ' : ' + allWords[isIndex + 1].lower()
				om.postOne(allWords, isIndex)
				
			except:
				do_nothing = 1
			# print isText[0]
			
		except:
			do_nothing = 1
		# selectedWord = [word for word in tagged if tag in ('NN', 'VB')]
		print 'tagged: ' + str(tagged)
		print 'selected_word: ' + str(selectedWord)

		# object = {}
		# object[''](userWords.get())
		# object.append(aiWords.get())
		# om.postOne(object)
		# print object

	parent = tk.Toplevel()
	parent.geometry('{}x{}'.format(300, 100))
	userWords = tk.Entry(parent, bg="#282B2B", fg="white", width=30)
	# userWords.place(x=10, y=700)											
	parent.bind('<Return>', post)
	userWords.pack()
	# aiWords = tk.Entry(parent, bg="#282B2B", fg="white", width=30)
	# aiWords.pack()
	button = tk.Button(parent, text="Post Data", command=post)
	button.pack()