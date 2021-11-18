import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.playlist = []

        self.create_frame()

    def create_frame(self):
        self.track = tk.LabelFrame(self, text = 'Song Track',font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.track.configure(width=410,height=300)
        self.track.grid(row=0,column=0)
root= tk.Tk()
root.geometry('600x400')
root.wm_title('Musique MP3 Player')
root.mainloop()


app= Player(master=root)
app.mainloop()