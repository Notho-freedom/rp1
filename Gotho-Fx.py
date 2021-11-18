from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("GOTHO-Fx")
root.resizable(False,False)

Label(text="GOTHO-Fx",bg="black",fg="white",font=("calibri",33),width=300,height=2).pack()

#menu card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)


Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Comic sans MS",15,"bold"),text="Dosa........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Comic sans MS",15,"bold"),text="Cookies.....Rs.63/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Comic sans MS",15,"bold"),text="Tea.........Rs.7/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Comic sans MS",15,"bold"),text="Coffee......Rs.100/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Comic sans MS",15,"bold"),text="Juice.......Rs.20/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Comic sans MS",15,"bold"),text="Pancakes....Rs.15/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Comic sans MS",15,"bold"),text="Eggs........Rs.7/plate",fg="black",bg="lightgreen").place(x=10,y=260)

root.mainloop()