from tkinter import *
import webbrowser


def boby_channel():
     webbrowser.open_new("http://ReleaseNotes.html")

# fenetre
window = Tk()
# affiche
window.title("You tube")
window.geometry("720x480")
window.config( bg='#41b77f')
frame = Frame(window, bg='#41b77f', bd='1')
label_title= Label(frame, text=" bienvenu sur l'application", font=(" impact",40), bg="#41b77f", fg="white")
label_title.pack()

label_stitle= Label(frame, text=" Salut a tous c'est N.O.T.H.O.° ", font=("Mongolian Baiti",25), bg="#41b77f", fg="white")
label_stitle.pack()
frame.pack(expand="yes")
bt=Button(frame, text = "ouvrir you tube ", font=("Segoe Script",15), bg="white", fg="#41b77f", command=boby_channel)
bt.pack(pady=25,padx=100)

window.mainloop()
