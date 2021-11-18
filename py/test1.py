from tkinter import *
import string
from random import randint, choice
a='1ewM3cUqpBIc'
def generate_pasword():
     pasword_min=6
     pasword_max=12
     all_chars=string.ascii_letters+string.digits
     pasword="".join(choice(all_chars) for x in range(randint(pasword_min, pasword_max)))
     pasword_Entry.delete(0, END)
     pasword_Entry.insert(0, pasword)

def generate():
     pasword_min=6
     pasword_max=12
     all_chars=string.ascii_letters+string.digits
     pasword="".join(choice(all_chars) for x in range(randint(pasword_min, pasword_max)))
     pasword_Entry.delete(0, END)
     pasword_Entry.insert(0, pasword)
     b=0
     while pasword!=a:
          pasword="".join(choice(all_chars) for x in range(randint(pasword_min, pasword_max)))
          pasword_Entry.delete(0, END)
          pasword_Entry.insert(0, b)
          b=b+1
          if pasword==a:
               pasword_Entry.delete(0, END)
               pasword_Entry.insert(0, pasword)
               break


window = Tk()
window.title("Generateur de mot de passe")
window.geometry("1080x720")
window.config(bg='#4065a4')
frame=Frame(window, bg='#4065a4',bd=1)
width=300
heigth=300
image=PhotoImage(file='F:/1soundd/1sound/images/C5.png')
canvas = Canvas(frame, width=300, height=300, bg='#4065a4', bd=0)
canvas.create_image(width/2, heigth/2, image=image)
canvas.grid(row = 0, column = 0)
right_frame=Frame(frame,bg='#4065a4',bd=1)
 
label_title= Label(right_frame, text=" mot de passe", font=(" impact",20), bg='#4065a4', fg="white")
label_title.pack()

pasword_Entry= Entry(right_frame, font=(" impact",20), bg='#4065a4', fg="white")
pasword_Entry.pack()

generer_pasword_button= Button(right_frame, text="Générer", font=(" impact",20), bg='#4065a4', fg="white",command=generate_pasword)
generer_pasword_button.pack(fill='x')
generer_pasword_button= Button(right_frame, text="test", font=(" impact",20), bg='#4065a4', fg="white",command=generate)
generer_pasword_button.pack(fill='x')
right_frame.grid(row = 0, column = 1)

frame.pack(expand="yes")

menu_bar=Menu(window)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="nouveau", command=generate_pasword)
file_menu.add_command(label="quitter", command=window.quit)
menu_bar.add_cascade(label="fichier", menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()
