from tkinter import *
import webbrowser
def boby_channelx():
     window1x = Tk()
     window1x.title("APPLICATIONS")
     window1x.geometry("1366x768")
     window1x.iconbitmap("F:/1soundd/1sound/images/C5.png")
     window1x.config(bg='#4065a4')
     label_title= Label(window1x, text="APPLICATION", font=(" impact",40), bg='#4065a4', fg="white")
     label_title.pack(fill='x')
     def boby_channel():
          webbrowser.open_new("file:///F:/1soundd/1sound/apk/a.exe")
     def boby_channe():
          webbrowser.open_new("file:///F:/1soundd/1sound/apk/Total Security/Utils/DesktopPlus/Utils/360searchlite.exe")
     def boby_chann():
          webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beepx2.wav")
     def boby_chann1():
          webbrowser.open_new("file:///F:/1soundd/1sound/apk/Bandicam/bdcam.exe")
     def boby_chann2():
          webbrowser.open_new("file:///F:/1soundd/1sound/apk/WinRAR - Copie/WinRAR.exe")
     def boby_chann3():
          webbrowser.open_new("file:///F:/1soundd/1sound/apk/Total Security/Utils/SysCleanerUI.exe")
     bt=Button(window1x, text="Gestion", font=("Segoe Script",15),bg="white", fg="#4065a4", command=boby_channel)
     bt.pack(fill='x')
     bt=Button(window1x, text="recherche", font=("Segoe Script",15), bg="white", fg="#4065a4", command=boby_channe)
     bt.pack(fill='x')
     bt=Button(window1x, text=".", font=("Segoe Script",15),bg="white", fg="#4065a4", command=boby_chann)
     bt.pack(fill='x')
     bt=Button(window1x, text="enregistreur d'ecran", font=("Segoe Script",15),bg="white", fg="#4065a4", command=boby_chann1)
     bt.pack(fill='x')
     bt=Button(window1x, text="Archives", font=("Segoe Script",15),bg="white", fg="#4065a4", command=boby_chann2)
     bt.pack(fill='x')
     bt=Button(window1x, text="Nettoyage", font=("Segoe Script",15),bg="white", fg="#4065a4", command=boby_chann3)
     bt.pack(fill='x')
     window1x.mainloop()
def sound():
     window1 = Tk()
     window1.title("COLLECTION")
     window1.geometry("1366x768")
     window1.iconbitmap("F:/1soundd/1sound/images/C5.png")
     window1.config(bg='#4065a4')
     label_title= Label(window1, text="COLLECTION", font=(" impact",40), bg='#4065a4', fg="white")
     label_title.pack(fill='x')
     def gims ():
          window1.destroy()
          windowG = Tk()
          windowG.title("MAITRE GIMS")
          windowG.geometry("1366x768")
          windowG.iconbitmap("F:/1soundd/1sound/images/C5.png")
          windowG.config(bg='#4065a4')
          label_title= Label(windowG, text="MAITRE GIMS FLEAU", font=(" impact",40), bg='#4065a4', fg="white")
          label_title.pack(fill='x')
          def beep1 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/01-Intro-2.mp3")         
          def beep2 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/02-Immortel.mp3")   
          def beep3 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/03-Côté-noir-feat.-Leto.mp3")
          def beep4 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims04-OATS.mp3")
          def beep5 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/05-Pendejo-feat.-Bosh.mp3")
          def beep6 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/06-Origami.mp3") 
          def beep7 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/07-Yolo.mp3")      
          def beep8 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/08-Oro-Jackson-feat.-Gato.mp3")
          def beep9 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/09-Twenny-twenny.mp3")
          def beep10 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/10-Og-na-og.mp3")
          def beep11 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/11-Sicario-feat.-Heuss-LEnfoiré.mp3")
          def beep12 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/12-Jusquici-tout-va-bien.mp3")
          def beep13 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/13-Jetez-pas-lœil.mp3")
          def beep14 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/14-Grosse-bleta-feat.-Kaaris.mp3")
          def beep15 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/15-Dans-ma-tête-feat.-Jaekers.mp3")
          def beep16 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/16-Cest-comme-ça.mp3")
          def beep17 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/gims/17-Thomas-Shelby.mp3")
          frame2=Frame(windowG, bg='#4065a4',bd='1')
          bt=Button(frame2, text="01-Intro-2", font=("time new roman",15), bg="white", fg="#4065a4", command=beep1)
          bt.pack(fill='x')
          bt=Button(frame2, text="02-Immortel", font=("time new roman",15), bg="white", fg="#4065a4", command=beep2)
          bt.pack(fill='x')
          bt=Button(frame2, text="03-Côté-noir-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep3)
          bt.pack(fill='x')
          bt=Button(frame2, text="04-OATS", font=("time new roman",15), bg="white", fg="#4065a4", command=beep4)
          bt.pack(fill='x')
          bt=Button(frame2, text="05-Pendejo-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep5)
          bt.pack(fill='x')
          bt=Button(frame2, text="06-Origami", font=("time new roman",15), bg="white", fg="#4065a4", command=beep6)
          bt.pack(fill='x')
          bt=Button(frame2, text="07-Yolo", font=("time new roman",15), bg="white", fg="#4065a4", command=beep7)
          bt.pack(fill='x')
          bt=Button(frame2, text="08-Oro-Jackson-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep8)
          bt.pack(fill='x')
          bt=Button(frame2, text="09-Twenny-twenny", font=("time new roman",15), bg="white", fg="#4065a4", command=beep9)
          bt.pack(fill='x')
          bt=Button(frame2, text="10-Og-na-og", font=("time new roman",15), bg="white", fg="#4065a4", command=beep10)
          bt.pack(fill='x')
          bt=Button(frame2, text="11-Sicario-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep11)
          bt.pack(fill='x')
          bt=Button(frame2, text="12-Jusquici-tout-va-bien", font=("time new roman",15), bg="white", fg="#4065a4", command=beep12)
          bt.pack(fill='x')
          bt=Button(frame2, text="13-Jetez-pas-lœil", font=("time new roman",15), bg="white", fg="#4065a4", command=beep13)
          bt.pack(fill='x')
          bt=Button(frame2, text="14-Grosse-bleta-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep14)
          bt.pack(fill='x')
          bt=Button(frame2, text="15-Dans-ma-tête-feat", font=("time new roman",15), bg="white", fg="#4065a4", command=beep15)
          bt.pack(fill='x')
          bt=Button(frame2, text="16-Cest-comme-ça", font=("time new roman",15), bg="white", fg="#4065a4", command=beep16)
          bt.pack(fill='x')
          bt=Button(frame2, text="17-Thomas-Shelby", font=("time new roman",15), bg="white", fg="#4065a4", command=beep17)
          bt.pack(fill='x')
          frame2.pack(expand="yes")
          windowG.mainloop()

          
     def zaho ():
          window1.destroy()
          window2 = Tk()
          window2.title("ZAHO")
          window2.geometry("1366x768")
          window2.iconbitmap("F:/1soundd/1sound/images/C5.png")
          window2.config(bg='#4065a4')
          label_title= Label(window2, text="				ZAHO 			", font=(" impact",40), bg='#4065a4', fg="white")
          label_title.pack(fill='x')      
          def beepz ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep3.wav")
          def beepZ2 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep7.wav")
          def beepZ3 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep7.wav")
          bt=Button(window2, text="01-Tourner la page", font=("time new roman",15), bg="white", fg="#4065a4", command=beepz)
          bt.pack()
          bt=Button(window2, text="01-Tourner la page", font=("time new roman",15), bg="white", fg="#4065a4", command=beepZ3)
          bt.pack()
          bt=Button(window2, text="0X-condansé", font=("time new roman",15), bg="white", fg="#4065a4", command=beepZ2)
          bt.pack()
          window2.mainloop()

     def mils3 ():
          window1.destroy()
          window2i = Tk()
          window2i.title("M.I.L.S.3")
          window2i.geometry("1366x768")
          window2i.iconbitmap("F:/1soundd/1sound/images/C5.png")
          window2i.config(bg='#4065a4')
          label_title= Label(window2i, text="M.I.L.S.3", font=(" impact",40), bg='#4065a4', fg="white")
          label_title.pack(fill='x')      
          def beepZ2 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep6.wav")
          bt=Button(window2i, text="0X-condansé", font=("time new roman",15), bg="white", fg="#4065a4", command=beepZ2)
          bt.pack(fill='x')
          window2i.mainloop()

     def bonnie ():
          window1.destroy()
          window2ix = Tk()
          window2ix.title("BONNIE X CLYDE")
          window2ix.geometry("1366x768")
          window2ix.iconbitmap("F:/1soundd/1sound/images/C5.png")
          window2ix.config(bg='#4065a4')
          label_title= Label(window2ix, text="BONNIE X CLYDE", font=(" impact",40), bg='#4065a4', fg="white")
          label_title.pack(fill='x')
          def beepz ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/bonnie X clide/BONNIE X CLYDE - The Unknown.mp3")
          def beepZ2 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep18.wav")
          bt=Button(window2ix, text="Unknow", font=("time new roman",15), bg="white", fg="#4065a4", command=beepz)
          bt.pack(fill='x')
          bt=Button(window2ix, text="0X-condansé", font=("time new roman",15), bg="white", fg="#4065a4", command=beepZ2)
          bt.pack(fill='x')
          window2ix.mainloop()


     def generiques ():
          window1.destroy()
          windowGi = Tk()
          windowGi.title("generiques")
          windowGi.geometry("1366x768")
          windowGi.iconbitmap("F:/1soundd/1sound/images/C5.png")
          windowGi.config(bg='#4065a4')
          label_title= Label(windowGi, text="GENERIQUES", font=(" impact",40), bg='#4065a4', fg="white")
          label_title.pack(fill='x')
          def beep1 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep1.wav")         
          def beep2 ():
          	   webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep4.wav")  
          def beep3 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep5.wav")
          def beep4 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep8.wav")
          def beep5 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep11.wav")
          def beep6 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep12.wav") 
          def beep7 ():
               webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beep13.wav")
          frame2i=Frame(windowGi, bg='#4065a4',bd='1')
          bt=Button(frame2i, text="          beep1          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep1)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep2          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep2)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep3          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep3)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep4          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep4)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep5          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep5)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep6          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep6)
          bt.pack(fill='x')
          bt=Button(frame2i, text="          beep7          ", font=("time new roman",15), bg="white", fg="#4065a4", command=beep7)
          bt.pack(fill='x')
          frame2i.pack(expand="yes")
          windowGi.mainloop()


     bt=Button(window1, text="MAITRE GIMS", font=("Segoe Script",15),bg="white", fg="#4065a4", command=gims)
     bt.pack(fill='x')
     bt=Button(window1, text="ZAHO", font=("Segoe Script",15), bg="white", fg="#4065a4", command=zaho)
     bt.pack(fill='x')
     bt=Button(window1, text="BONNIE X CLYDE", font=("Segoe Script",15),bg="white", fg="#4065a4", command=bonnie)
     bt.pack(fill='x')
     bt=Button(window1, text="M.I.L.S.3", font=("Segoe Script",15),bg="white", fg="#4065a4", command=mils3)
     bt.pack(fill='x')
     bt=Button(window1, text="GENERIQUES", font=("Segoe Script",15),bg="white", fg="#4065a4", command=generiques)
     bt.pack(fill='x')
     window1.mainloop()
def apropos():
     webbrowser.open_new("file:///F:/1soundd/1sound/beeps/beepint2.wav")
window = Tk()
window.title("ALL STARS")
window.geometry("1366x768")
window.iconbitmap("F:/1soundd/1sound/images/C5.png")
window.config(bg='#4065a4')
width=400
heigth=560
label_title= Label(window, text="              WELCOME            ", font=(" impact",40), bg='#4065a4', fg="white")
label_title.pack()
frame1=Frame(window, bg='#4065a4',bd='1')
frame=Frame(frame1, bg='#4065a4',bd='1')
label_title= Label(frame, text="              WELCOME            ", font=(" impact",40), bg='#4065a4', fg="white")
label_title.pack()
bt=Button(frame, text="               Applications            ", font=("Segoe Script",15), bg="white", fg="#4065a4", command=boby_channelx)
bt.pack(fill='x')
bt=Button(frame, text="               musiques               ", font=("Segoe Script",15), bg="white", fg="#4065a4", command=sound)
bt.pack(fill='x')
frame.pack(side="right")
frame.grid(row = 0, column = 1)

image=PhotoImage(file='F:/1soundd/1sound/images/C5.png')
canvas = Canvas(frame1, width='300', height='350', bg='#4065a4', bd=0)
canvas.create_image(width/3, heigth/3, image=image)
canvas.grid(row = 0, column = 0)

image1=PhotoImage(file='F:/1soundd/1sound/images/C5.png')
canvas1 = Canvas(frame1, width='300', height='350', bg='#4065a4', bd=0)
canvas1.create_image(width/3, heigth/3, image=image)
canvas1.grid(row = 0, column = 2)

image2=PhotoImage(file="F:/1soundd/1sound/images/tr.png")
canvas2 = Canvas(frame1, width='300', height='389', bg='#4065a4', bd=0)
canvas2.create_image(width/3, heigth/3, image=image2)
canvas2.grid(row = 1, column =0)

frame1.pack(expand="yes")

menu_bar=Menu(window)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Apropos", command=apropos)
file_menu.add_command(label="quitter", command=window.destroy)
menu_bar.add_cascade(label="fichier", menu=file_menu)
window.config(menu=menu_bar)
window.mainloop()
