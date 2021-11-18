from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
import sqlite3

class student():
	"""docstring for student"""
	def __init__(self, root):
		self.root = root
		self.root.title("NECXUS - GESTIONNAIRE")
		self.root.geometry("1366x178+0+0")

		title = Label(self.root,text=" = =  N  .  E  .  C  .  X  .  U  .  S  = = ",bd=9,relief=RIDGE,font=("Roman",50,"bold"),bg="black",fg="white")
		title.pack(side=TOP,fill=X)
		#========var=======
		self.Matricule = StringVar()
		self.Nom = StringVar()
		self.Email = StringVar()
		self.Prenom = StringVar()
		self.Age = StringVar()
		self.Addresse = StringVar()
		self.Genre = StringVar()
		self.Contact = StringVar()
		self.DDN = StringVar()
		self.Chercher_par = StringVar()
		self.Chercher = StringVar()
		self.vf = StringVar()
		#========MG=======
		M_F = Frame(self.root,bd=2,relief=GROOVE,bg="#4065a4")
		M_F.place(x=1,y=100,width=485,height=642)

		m_title = Label(M_F,text="GESTIONNAIRE",bg="#4065a4",fg="black",font=("times new roman",20,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)


		lbl_roll = Label(M_F,text="Matricule",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_roll.grid(row=1,column=0,pady=10,padx=5,sticky="W")
		txt_roll = Entry(M_F,textvariable=self.Matricule,font=("times new roman",10),bd=1)
		txt_roll.grid(row=1,column=1,pady=10,padx=5,sticky="W")


		lbl_Nom = Label(M_F,text="Nom",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Nom.grid(row=2,column=0,pady=10,padx=5,sticky="W")
		txt_Nom = Entry(M_F,textvariable=self.Nom,font=("times new roman",10),bd=1)
		txt_Nom.grid(row=2,column=1,pady=10,padx=5,sticky="W")

		lbl_preNom = Label(M_F,text="Prenom",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_preNom.grid(row=2,column=2,pady=10,padx=5,sticky="W")
		txt_preNom = Entry(M_F,textvariable=self.Prenom,font=("times new roman",10),bd=1)
		txt_preNom.grid(row=2,column=3,pady=10,padx=5,sticky="W")

		lbl_Age = Label(M_F,text="Age",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Age.grid(row=3,column=2,pady=10,padx=5,sticky="W")
		txt_Age = Entry(M_F,textvariable=self.Age,font=("times new roman",10),bd=1)
		txt_Age.grid(row=3,column=3,pady=10,padx=5,sticky="W")

		lbl_Email = Label(M_F,text="Email",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Email.grid(row=4,column=0,pady=10,padx=5,sticky="W")
		txt_Email = Entry(M_F,textvariable=self.Email,font=("times new roman",10),bd=1)
		txt_Email.grid(row=4,column=1,pady=10,padx=5,sticky="W")

		lbl_Genre = Label(M_F,text="Genre",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Genre.grid(row=5,column=0,pady=10,padx=5,sticky="W")
		combo_Genre = ttk.Combobox(M_F,textvariable=self.Genre,font=("times new roman",10),state="readonly")
		combo_Genre['values']=("Homme","Femme","Autre")
		combo_Genre.grid(row=5,column=1,pady=10,padx=5,sticky="W")

		vf_f= Frame(M_F,bd=1,bg="#4065a4")
		vf_f.place(x=5,y=350,width=460)
		lbl_vf = Label(vf_f,text="______________________________________",bg="#4065a4",fg="black",font=("times new roman",13,"bold"))
		lbl_vf.grid(row=0,column=0,pady=50,padx=5,sticky="W")
		txt_vf = Entry(vf_f,textvariable=self.vf,font=("times new roman",10),bd=1)
		txt_vf.grid(row=0,column=1,pady=50,padx=5,sticky="W")

		lbl_Contact = Label(M_F,text="Contact",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Contact.grid(row=1,column=2,pady=10,padx=5,sticky="W")
		txt_Contact = Entry(M_F,textvariable=self.Contact,font=("times new roman",10),bd=1)
		txt_Contact.grid(row=1,column=3,pady=10,padx=5,sticky="W")

		lbl_Dob = Label(M_F,text="DDN",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_Dob.grid(row=3,column=0,pady=10,padx=5,sticky="W")
		txt_Dob = Entry(M_F,textvariable=self.DDN,font=("times new roman",10),bd=1)
		txt_Dob.grid(row=3,column=1,pady=10,padx=5,sticky="W")

		lbl_address = Label(M_F,text="Addresse",bg="#4065a4",fg="white",font=("times new roman",13,"bold"))
		lbl_address.grid(row=4,column=2,pady=10,padx=5,sticky="W")
		txt_address = Entry(M_F,textvariable=self.Addresse,font=("times new roman",10),bd=1)
		txt_address.grid(row=4,column=3,pady=10,padx=5,sticky="W")

#======================BT

		b_f = Frame(M_F,bd=2,bg="black")
		b_f.place(x=5,y=580,width=460)

		adbt = Button(b_f,text="AJOUTER",width=11,command=self.add_st).grid(row=0,column=0,padx=10,pady=10)
		upbt = Button(b_f,text="METTRE A JOUR",width=12,command=self.afficher).grid(row=0,column=1,padx=10,pady=10)
		nbt = Button(b_f,text="NETTOYER",width=11).grid(row=0,column=2,padx=10,pady=10)
		dbt = Button(b_f,text="SUPRIMER",width=11).grid(row=0,column=3,padx=10,pady=10)

#========DTF=======
		dt_F = Frame(self.root,bd=1,relief=RIDGE,bg="#4065a4")
		dt_F.place(x=486,y=100,width=876,height=640)

		lbd_search = Label(dt_F,text="Chercher par...",bg="#4065a4",fg="white",font=("times new roman",20))
		lbd_search.grid(row=0,column=0,pady=10,padx=20,sticky="W")
		combo_search = ttk.Combobox(dt_F,textvariable=self.Chercher_par,font=("times new roman",13),width=10)
		combo_search['values']=("Matricule","Nom","Contact")
		combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="W")
		txt_search = Entry(dt_F,textvariable=self.Chercher,font=("times new roman",10),width=20, bd=1, relief=GROOVE)
		txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")
		sehbt = Button(dt_F,text="Rechercher",width=10,pady=5,command=self.affich_1).grid(row=0,column=3,padx=10,pady=10)
		shwdbt = Button(dt_F,text="Tout afficher",width=10,pady=5,command=self.afficher).grid(row=0,column=4,padx=10,pady=10)
		#========TbF=======
		tb_F = Frame(dt_F,bd=1,relief=RIDGE,bg="crimson")
		tb_F.place(x=20,y=70,width=850,height=555) 



		scroll_x = Scrollbar(tb_F,orient=HORIZONTAL)
		scroll_y = Scrollbar(tb_F,orient=VERTICAL)

		self.st = ttk.Treeview(tb_F,column=("Matricule","Nom","Prenom","Age","DDN","Genre","Email","contact","Addresse"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)

		scroll_x.config(command= self.st.xview)
		scroll_y.config(command= self.st.yview)

		self.st.heading("Matricule", text="Matricule")
		self.st.heading("Nom", text="Nom")
		self.st.heading("Prenom", text="Prenom")
		self.st.heading("Age", text="Age")
		self.st.heading("DDN", text="DDN")
		self.st.heading("Genre", text="Genre")
		self.st.heading("Email", text="Email")
		self.st.heading("Addresse", text="Addresse")
		self.st.heading("contact", text="Contact")

		self.st['show']='headings'
		self.st.column("Matricule", width=90)
		self.st.column("Nom", width=100)
		self.st.column("Prenom", width=100)
		self.st.column("Age", width=30)
		self.st.column("DDN", width=100)
		self.st.column("Genre", width=70)
		self.st.column("Email", width=100)
		self.st.column("Addresse", width=150)
		self.st.column("contact", width=90)
		self.st.pack(fill=BOTH,expand=1)

	def NETTOYER(self):
		self.Matricule.set("")
		self.Nom.set("")
		self.Email.set("")
		self.Prenom.set("")
		self.Age.set("")
		self.Addresse.set("")
		self.Genre.set("")
		self.Contact.set("")
		self.DDN.set("")
		self.Chercher_par.set("")
		self.Chercher.set("")
		self.vf.set("")		


	def affich_1(self):
		Chercher = str(self.Chercher.get())
		Chercher_par = str(self.Chercher_par.get())

		donnes=[(Chercher_par,Chercher,)]

		conn = sqlite3.connect("NECXUS_DB.db")
		cur = conn.cursor()
		cur.execute("SELECT * FROM students WHERE "+Chercher_par+" LIKE '%"+Chercher+"%'")
		rows = cur.fetchall()
		print(rows)
		if len(rows) != 0:
			self.st.delete(*self.st.get_children())
			for row in rows:
				self.st.insert('',END,values=row)
				print(row)
			conn.commit()
		conn.close()
		self.NETTOYER()



	def afficher(self):
		conn = sqlite3.connect("NECXUS_DB.db")
		cur = conn.cursor()
		cur.execute("select * from students")
		rows= cur.fetchall()
		if len(rows)!=0:
			self.st.delete(*self.st.get_children())
			for row in rows:
				self.st.insert('',END,values=row)
			conn.commit()
		conn.close()


	def add_st(self):
		Matricule = self.Matricule.get()
		Nom = self.Nom.get()
		Prenom = self.Prenom.get()
		Age = self.Age.get()
		Email = self.Email.get()
		Genre = self.Genre.get()
		DDN = self.DDN.get()
		Addresse = self.Addresse.get()
		Contact = self.Contact.get()
		vff='succes!!'
		String_vf=str('%s' %vff)
		if Nom != '':
			if Prenom != '':
				if Age != '':
					if Email != '':
						if Matricule != '':
							if len(Matricule) != 9:
								messagebox.showinfo("Erreur de remplissage","Le Matricule doit compter 9 caractères!!")
							else :
								if Addresse != '':
									if DDN != '':
										if ((len(DDN) !=10 or DDN[6] != '2') or(DDN[2] != '/' or DDN[5] !='/')) :
											messagebox.showinfo("Erreur de remplissage","La Date de naissance doit respectée le format <JJ/MM/AAAA>!\n EX: 01/01/2000")
										else :
											if Contact != '':
												if Genre != '':
													
													print(Nom)
													print(Age)
													print(Prenom)
													print(Matricule)
													print(Email)
													print(Genre)
													print(Contact)
													print(DDN)
													print(Addresse)
													#========CDB=======
													conn = sqlite3.connect("NECXUS_DB.db")
													cur = conn.cursor()
													create = "CREATE TABLE  IF NOT EXISTS students ( Matricule INTEGER PRIMARY KEY,Nom VARCHAR(20) ,Prenom VARCHAR(20),Age INTEGER,DDN DATE,Genre CHAR(6) ,Email VARCHAR(30),contact INTEGER,Addresse VARCHAR(20) );"
													insert = "INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?)"
													donnees = [(Matricule,Nom,Prenom,Age,DDN,Genre,Email,Contact,Addresse)]
													cur.execute(create)
													for donnee in donnees:
														cur.execute(insert,donnee)
													conn.commit()
													print (cur.fetchone())
													conn.close()
													String_vf=str('%s' %vff)
													self.vf.set(String_vf)
													self.afficher()

												else :
													messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
											else :
												messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
									else :
										messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
								else :
									messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
						else :
							messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
					else :
						messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
				else :
					messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
			else :
				messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")
		else :
			messagebox.showinfo("Alerte","Veillez remplir convenablement les champs!")

							


class student():

	root=Tk()
	obj= student(root)
	
	root.mainloop()
