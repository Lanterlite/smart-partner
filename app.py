print "SmartPartner Running..."

import Tkinter as tk
import os

# ==============================
# from PIL import Image, ImageTk, ImageSequence

# class App:
	# def __init__(self, parent):
		# self.parent = parent
		# self.canvas = tk.Canvas(parent, width=800, height=600, bd=0, highlightthickness=0, relief='ridge')
		# self.canvas.pack()
		# self.sequence = [ImageTk.PhotoImage(img)
							# for img in ImageSequence.Iterator(
								# Image.open(
								# './eye/normal.gif'))]
		# self.image = self.canvas.create_image(400,300, image=self.sequence[0])
		# self.animate(1)
	# def animate(self, counter):
		# self.canvas.itemconfig(self.image, image=self.sequence[counter])
		# self.parent.after(30, lambda: self.animate((counter+1) % len (self.sequence)))
# ==============================


def on_button(text):
	print(text)

root = tk.Tk()

root.iconbitmap('brown-favicon.ico')				# Change App Icon
root.title( "SmartPartner" ) 						# Change App Title
root.geometry('{}x{}'.format(1000, 750))			# Change Windows Size
root.resizable(width=False, height=False)			# Change Resizable Settings
root.configure(background='black')					# Change Background Color

input = tk.Entry(root, bg="#282B2B", fg="white", width=30)		# Create Entry
input.place(x=10, y=700)										# Change Background Color

label = tk.Label(text="This is Me", fg="white", bg="black")		# Create Label
label.place(x=10, y=650)										# Change Background Color

button = tk.Button(root, text="Get", command=on_button("test"))
button.pack()
# app = App(root)
root.mainloop()


# class SampleApp(tk.Tk):

    # def __init__(self):        
        # tk.Tk.__init__(self)
        # self.input = tk.Entry(self, bg="#282B2B", fg="white", width=30)		# Create Entry
        # self.input.place(x=10, y=700)										# Change Background Color

        # self.label = tk.Label(text="This is Me", fg="white", bg="black")		# Create Label
        # self.label.place(x=10, y=650)										# Change Background Color
        # self.entry = tk.Entry(self)
        # self.entry.place(x=100, y=700)									
        # self.button = tk.Button(self, text="Get", command=self.on_button)
        # self.button.pack()
        # self.entry.pack()

    # def on_button(self):
        # print(self.entry.get())

# w = SampleApp()
# w.mainloop()


# ==============================
# canvas = tk.Canvas(root)
# canvas.grid(row = 0, column = 0)
	# photo = tk.PhotoImage(file = './webview.gif')
	# canvas.create_image(0, 0, image=photo)
# frame2 = tk.PhotoImage(file='./webview.gif', format="gif -index 2")
# canvas.create_image(100, 100, image=frame2)

# ==============================
# def run_animation():
    # while True:
        # try:
            # global photo
            # global frame
            # global label
            # photo = tk.PhotoImage(
                # file = photo_path,
                # format = "gif - {}".format(frame)
			# )
			
            # frame2 = tk.PhotoImage(file="./webview.gif", format="gif -index 2")
            # label.configure(image = frame2)

            # frame = frame + 1

        # except Exception:
            # frame = 1
            # break

# photo_path = "./webview.gif"

# photo = tk.PhotoImage(
    # file = photo_path,
    # )
# label = tk.Label(
    # image = photo
    # )
# animate = tk.Button(
    # root,
    # text = "animate",
    # command = run_animation
    # )

# label.pack()
# animate.pack()


# ==============================
# from Tkinter import *

# class App:
    # def __init__(self,master):
        # self.var = IntVar()
        # frame = Frame(master)
        # frame.grid()
        # f2 = Frame(master,width=200,height=100)
        # f2.grid(row=0,column=1)
        # button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
        # button.grid(row=0,column=0)
        # msg2="""I feel bound to give them full satisfaction on this point"""
        # self.v= Message(f2,text=msg2)
    # def fx(self):
        # if self.var.get():
            # self.v.grid(column=1,row=0,sticky=N)
        # else:
            # self.v.grid_remove()

# top = Tk()
# app = App(top)            
# top.mainloop()

# =============================
# import os

# os.system('mode con: cols=100 lines=40')
# raw_input("Press any key to continue...")
# =============================
