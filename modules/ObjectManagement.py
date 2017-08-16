import Tkinter as tk

# ==================================
# Show Post Button
# ==================================
class PostButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Post", command=postOne)		# Create Button
		self.button.place(x=200, y=700)										# Change Button Position
		self.button.config(height=1, width=10)								# Change Button Size
# ==================================

# ==================================
# Post Data
# ==================================		
from pymongo import MongoClient		
import datetime

def postOne(object):
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	post = {
		"userWords": object[0], 
		"aiWords": object[1], 
	}
	collection.insert_one(post).inserted_id
	print "Post Success!"

# ==================================
# Show Get-One Button
# ==================================
class GetOneButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Get One", command=getOne)		# Create Button
		self.button.place(x=300, y=700)										# Change Button Position
		self.button.config(height=1, width=10)								# Change Button Size
# ==================================

# ==================================
# Get One Data
# ==================================		
import pprint

def getOne():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	pprint.pprint(collection.find_one({"author": "Mike"}))
	print "Get One Success!"
# ==================================				

# ==================================
# Show Get-All Button
# ==================================
class GetAllButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Get All", command=getAll)		# Create Button
		self.button.place(x=400, y=700)										# Change Button Position
		self.button.config(height=1, width=10)								# Change Button Size
# ==================================

# ==================================
# Get All Data
# ==================================		
import pprint

def getAll():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	data = []
	for post in collection.find():
		data.append(post)
	print "Get All Success!"
	return data
	
# ==================================		

# ==================================
# Show Delete Button
# ==================================
class DeleteOneButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Delete", command=delOne)		# Create Button
		self.button.place(x=500, y=700)										# Change Button Position
		self.button.config(height=1, width=10)								# Change Button Size
# ==================================

# ==================================
# Delete One Data
# ==================================		
import pprint

def delOne():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	collection.delete_many({"author": "Mike"})
	print "Delete One Success!"
# ==================================

# ==================================
# Show Update Button
# ==================================
class UpdateOneButton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.button = tk.Button(parent, text="Update", command=updateOne)	# Create Button
		self.button.place(x=600, y=700)										# Change Button Position
		self.button.config(height=1, width=10)								# Change Button Size
# ==================================

# ==================================
# Update One Data
# ==================================		
import pprint

def updateOne():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['smartpdb']
	collection = db['AnswerCollection']
	collection.update_one({"author": "Mike"}, {'$set': {"author": "Miko"}}, upsert=False)
	print "Update One Success!"
# ==================================