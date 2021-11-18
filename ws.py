from sqlite3.dbapi2 import Date
from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import time
import winsound
from datetime import datetime
import threading
from threading import Thread


def apropos():
    app=tk.Toplevel()
    app.geometry("700x500+0+0")
    app.resizable(0,0)
    app.title("HT-Apropos")
    Label(app,text="APROPOS",fg="white",bg="#4065a4",font=("times new roman",15,"bold"),bd=1).pack(side=TOP,fill=X)
    Label(app,text=" C . Y . B . E . R . X  à été programmer en python 3.9 par #Notho.\n Ses objectifs sont non défini pour le moment, mais il vous surviendrat tres certainement à vos besoins\n Genesis vous remerci!").place(x=50,y=250)
    winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\timer.wav",winsound.SND_ASYNC)
    app.mainloop()





class hanta(tk.Tk):


    def __init__(self, root):

        self.root=root
        self.root.geometry("1360x768+0+0")
        self.root.title("CyberX")
        title = Label(self.root,text=" =  = C . Y . B . E . R . X =  =  ",bd=9,relief=GROOVE,font=("Roman",40,"bold"),bg="black",fg="red").pack(side=TOP,fill=X)
        label2 = tk.Label(self.root, text="""this is ef_g closing this will not affect root""").place(x=500,y=90)

        #variables
        self.Id = StringVar()
        self.Nomc = StringVar()
        self.heure = StringVar()
        self.heur = IntVar()
        self.min = IntVar()
        self.Addresse = StringVar()
        self.Dett = IntVar()
        Temps_a = IntVar()
        self.DD = StringVar()
        self.tach = IntVar()
        self.tr = IntVar()
        self.nser = StringVar()
        self.vf = StringVar()
        self.vff = StringVar()
        self.Chercher_par = StringVar()
        self.Chercher = StringVar()
        #frame gauche
        f_g= Frame(self.root, width=350,height=700,bg="#4065a4",bd=4,relief=GROOVE).place(x=0,y=80)
        f_g1= Frame(f_g, width=342,height=40,bg="white",bd=4).place(x=3,y=85)
        Label(f_g1,text="= = M.E.N.U = =",fg="black",bg="white",font=("times new roman",15,"bold"),bd=0).place(x=120,y=93)
        f_g2= Frame(f_g, width=345,height=4,bg="red",bd=4).place(x=4,y=390)




        def NETf():
            ax=self.vf.get()
            bx=self.vff.get()
            if ax!="" and bx!="":
                self.vf.set(" ")
                self.vff.set(" ")
            else:
                if ax != '':
                    self.vf.set(" ")
                else:
                    self.vff.set(" ")




        def D_T():
            dt=''
            now = datetime.now()
            heur=now.strftime("%H:%M:%S")
            hr=str(heur[0])+str(heur[1])
            mn=str(heur[3])+str(heur[4])
            self.heur.set(hr)
            self.min.set(mn)
            self.heure.set(heur)
            heur=now.strftime("%d-%m-%Y %H:%M:%S")
            for i in range(10):
                dt=dt+str(heur[i])
            self.DD.set(dt)
            self.tach.set(0)
            heur=now.strftime("%H:%M:%S")
            tk.Label(f_g,text=("Heure("+heur+")"),fg="white",bg="#4065a4",font=("times new roman",10,"bold"),bd=0).place(x=200,y=420)
            heur=now.strftime("%H%M%S")
            cl=str("client")+str(heur)
            self.Nomc.set(cl)
            heur=now.strftime("%d%m%Y%H%M%S")
            self.Id.set(heur)
            self.nser.set("Serveur0")
            NETf()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)


        def convtim():
            heur = self.heur.get()
            min = self.min.get()
            tach = int(self.tach.get())
            e=0
            for i in range(60):
                e = e + heur
            e = e + min
            x=0
            for i in range(60):
                x= x + tach
            e= e + x
            d1=int(e/60)
            d2=float((e/60)-d1)
            t0=d2
            for i in range(60):
                d2=d2+t0
            d2=int(d2)
            s=str(d1)+"h"+str(d2)+"min"
            self.vf.set("")
            D="Fin de session: ("+s+")"
            self.vf.set(D)
            s=str(d1)+"h"+str(d2)+"m "
            return s

        tb_F = Frame(self.root,bd=1,relief=RIDGE,bg="white")

        tb_F.place(x=350,y=85,width=670,height=545) 


        scroll_x = Scrollbar(tb_F,orient=HORIZONTAL)
        scroll_y = Scrollbar(tb_F,orient=VERTICAL)

        self.st = ttk.Treeview(tb_F,column=("ID","Nomc","Temps_Acheter","Temps_restant","DD","Heure","Addresse","Servir_par","Dette"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command= self.st.xview)
        scroll_y.config(command= self.st.yview)

        self.st.heading("ID", text="ID")
        self.st.heading("Nomc", text="Nomc")
        self.st.heading("Temps_Acheter", text="Temps_Acheter")
        self.st.heading("Temps_restant", text="Temps_restant")
        self.st.heading("DD", text="DD")
        self.st.heading("Heure", text="Heure")
        self.st.heading("Addresse", text="Addresse")
        self.st.heading("Servir_par", text="Servir_par")
        self.st.heading("Dette", text="Dette")

        self.st['show']='headings'
        self.st.column("ID", width=100)
        self.st.column("Nomc", width=150)
        self.st.column("Temps_Acheter", width=50)
        self.st.column("Temps_restant", width=50)
        self.st.column("DD", width=100)
        self.st.column("Heure", width=90)
        self.st.column("Addresse", width=100)
        self.st.column("Servir_par", width=150)
        self.st.column("Dette", width=60)
        self.st.pack(fill=BOTH,expand=1)
        
        #bd
        f_gd= Frame(self.root, width=350,height=700,bg="#4065a4",bd=4,relief=GROOVE).place(x=1020,y=80)
        Label(f_gd,text="= = P.R.O.G.R.E.S.S.I.O.N = =",fg="black",bg="white",font=("times new roman",15,"bold"),bd=4).place(x=1025,y=83,width=350,height=40)


        def NETTOYER():
            self.Nomc.set("")
            self.heur.set("")
            self.min.set("")
            self.DD.set("")
            self.tach.set("")
            self.nser.set("")
            self.Id.set("")
            self.Addresse.set("")
            self.vf.set("")
            self.vff.set("")
            self.Chercher.set("")
            self.Chercher_par.set("")
            self.Dett.set("")
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)

        def affich_1():
            Chercher = self.Chercher.get()
            Chercher_par = self.Chercher_par.get()

            conn = sqlite3.connect("HANTA_DB.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Client WHERE "+Chercher_par+" LIKE '%"+Chercher+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.st.delete(*self.st.get_children())
                for row in rows:
                    self.st.insert('',END,values=row)
                conn.commit()
            conn.close()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)


        def afficher():
            conn = sqlite3.connect("HANTA_DB.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Client")
            rows= cur.fetchall()
            if len(rows)!=0:
                self.st.delete(*self.st.get_children())
                for row in rows:
                    self.st.insert('',END,values=row)
                conn.commit()
            conn.close()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)
            
        afficher()
        self.y = IntVar()
        self.y=100
        self.i = IntVar()
        self.i =1
        dic_pro={}
        self.val ={}
        self.p = {}
        

        def addcl():
            T_a=self.tach.get()
            Nomc=self.Nomc.get()
            T_r=self.tr.get()
            heur=self.heur.get()
            min=self.min.get()
            Addresse= self.Addresse.get()
            Servir_par=self.nser.get()
            Dette=self.Dett.get()
            id=self.Id.get()
            DD=self.DD.get()
            Heure=str(heur)+"h"+str(min)+"min"
            if (T_a !=0):
                if len(Servir_par) !=0:
                    if Dette != 0:
                        if len(Addresse) !=0:
                            conn = sqlite3.connect("HANTA_DB.db")
                            cur = conn.cursor()
                            create = "CREATE TABLE  IF NOT EXISTS Client ( ID VARCHAR(20) PRIMARY KEY,Nomc VARCHAR(20) ,Temps_Acheter INTEGER NOT NULL,Temps_restant INTEGER,DD DATE,Heure INTEGER,Addresse VARCHAR(20),Servir_par VARCHAR(30),Dette INTEGER);"
                            insert = "INSERT INTO Client VALUES (?,?,?,?,?,?,?,?,?)"
                            donnees = [(id,Nomc,T_a,T_r,DD,Heure,Addresse,Servir_par,Dette),]
                            cur.execute(create)
                            for donnee in donnees:
                                cur.execute(insert,donnee)
                            conn.commit()
                            conn.close()
                            convtim()
                            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\finish.wav",winsound.SND_ASYNC)
                            afficher()
                            
                            def bar():
                                
                                T_a = self.tach.get()
                                dic_pro[self.i] = ttk.Progressbar(f_gd,length=230,mode='indeterminate')
                                dic_pro[self.i].place(x=1113,y=self.y)

                                label2l=Label(f_gd,font=("times new roman",10,"bold"),bg="#4065a4",fg="white")
                                label2l.place(x=1323,y=self.y,width=35,height=23)

                                label2nl=Label(f_gd,font=("times new roman",10,"bold"),text=self.Nomc.get()+":",bg="#4065a4",fg="white")
                                label2nl.place(x=1024,y=self.y,width=95,height=23)
                                k=self.y - 25
                                kh=" DS: "+str(heur)+"h"+str(min)+"m "
                                khf= convtim()
                                khf = " FS: "+khf
                                Label(f_gd,font=("times new roman",10,"bold"),text=(kh,self.Id.get(),khf),bg="black",fg="red").place(x=1070,y=k,width=280,height=23)

                                T_a*=60

                                dic_pro[self.i]['value']=0
                                dic_pro[self.i]['maximum']=T_a+1

                                p=0
                                for i in range(1,T_a+1,1):
                                    dic_pro[self.i]['value']=i
                                    p=i
                                    p/=T_a
                                    p=int(p*100)
                                    self.root.update_idletasks()
                                    time.sleep(1)
                                    label2l.config(text=str(p)+"%")
                                dic_pro[self.i]['value']=T_a+1
                                winsound.PlaySound("Alarm01.wav",winsound.SND_ASYNC)                                
                            self.y=self.y + 50
                            self.i = self.i + 1
                            th1 = threading.Thread(target=bar)
                            th1.start()
                        else:                          
                            NETf()
                            d="Veillez inscrire l'addresse du client "+Nomc+" !!"
                            self.vf.set(d)
                    else:
                        conn = sqlite3.connect("HANTA_DB.db")
                        cur = conn.cursor()
                        create = "CREATE TABLE  IF NOT EXISTS Client ( ID VARCHAR(20) PRIMARY KEY,Nomc VARCHAR(20) ,Temps_Acheter INTEGER NOT NULL,Temps_restant INTEGER,DD DATE,Heure INTEGER,Addresse VARCHAR(20),Servir_par VARCHAR(30),Dette INTEGER);"
                        insert = "INSERT INTO Client VALUES (?,?,?,?,?,?,?,?,?)"
                        donnees = [(id,Nomc,T_a,T_r,DD,Heure,Addresse,Servir_par,Dette),]
                        cur.execute(create)
                        for donnee in donnees:
                            cur.execute(insert,donnee)
                        conn.commit()
                        print (cur.fetchone())
                        conn.close()
                        convtim()
                        winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\finish.wav",winsound.SND_ASYNC)
                        afficher()
                        
                        def bar():
                            
                            T_a = self.tach.get()
                            dic_pro[self.i] = ttk.Progressbar(f_gd,length=230,mode='determinate')
                            dic_pro[self.i].place(x=1113,y=self.y)

                            label2l=Label(f_gd,font=("times new roman",10,"bold"),bg="#4065a4",fg="white")
                            label2l.place(x=1323,y=self.y,width=35,height=23)

                            label2nl=Label(f_gd,font=("times new roman",10,"bold"),text=self.Nomc.get()+":",bg="#4065a4",fg="white")
                            label2nl.place(x=1024,y=self.y,width=95,height=23)
                            k=self.y - 25
                            kh=" DS: "+str(heur)+"h"+str(min)+"m "
                            khf= convtim()
                            khf = " FS: "+khf
                            Label(f_gd,font=("times new roman",10,"bold"),text=(kh,self.Id.get(),khf),bg="black",fg="red").place(x=1070,y=k,width=280,height=23)


                            T_a*=60

                            dic_pro[self.i]['value']=0
                            dic_pro[self.i]['maximum']=T_a+1

                            self.p[self.i]=0
                            for self.val[self.i] in range(1,T_a+1,1):
                                dic_pro[self.i]['value']=self.val[self.i]
                                self.p[self.i]=self.val[self.i]
                                self.p[self.i]/=T_a
                                self.p[self.i]=int(self.p[self.i]*100)
                                self.root.update_idletasks()
                                time.sleep(1)
                                label2l.config(text=str(self.p[self.i])+"%")                            
                            dic_pro[self.i]['value']=T_a+1
                            winsound.PlaySound("Alarm01.wav",winsound.SND_ASYNC)
                        th1 = threading.Thread(target=bar)
                        th1.start()
                        self.y=self.y + 50
                        self.i = self.i + 1                              
                else:
                    winsound.PlaySound("Windows Hardware Fail.wav",winsound.SND_ASYNC)
                    NETf()
                    self.vf.set("Veillez inscrire votre nom de service!!")             
            else:
                winsound.PlaySound("Windows Hardware Fail.wav",winsound.SND_ASYNC)
                NETf()
                self.vff.set("Le temps_acheter ne peut pas être null")

        def supp():
            Chercher = self.Chercher.get()
            Chercher_par = self.Chercher_par.get()
            conn = sqlite3.connect("HANTA_DB.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM Client WHERE "+Chercher_par+" LIKE '%"+Chercher+"%'")
            conn.commit()
            conn.close()
            afficher()
        
  
        #suite_framg
        Label(f_g,text="Date",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=420)
        Entry(f_g,textvariable=self.DD,font=("times new roman",10),bd=2).place(x=7,y=440)
        mf=Frame(f_g,relief=RIDGE,bg="#4065a4").place(x=200,y=440,width=125,height=17) 
        Entry(mf,textvariable=self.heur,font=("times new roman",10),bd=1,bg="white").place(x=200,y=440,width=30,height=19)
        Label(f_g,text="h",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=220,y=438,width=25)
        Entry(mf,textvariable=self.min,font=("times new roman",10),bd=1,bg="white").place(x=245,y=440,width=20,height=19)
        Label(f_g,text="min",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=264,y=438,width=30)

        Label(f_g,text="Nomc",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=475)
        Label(f_g,text="Temps_Acheter(h)",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=475)
        Entry(f_g,textvariable=self.Nomc,font=("times new roman",10),bd=2).place(x=7,y=495)
        Entry(f_g,textvariable=self.tach,font=("times new roman",10),bd=2).place(x=200,y=495)
        Label(f_g,text="Servir_par",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=530)
        Entry(f_g,textvariable=self.nser,font=("times new roman",10),bd=2).place(x=7,y=550)

        Label(f_g,text="ID",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=530)
        Entry(f_g,textvariable=self.Id,font=("times new roman",10),bd=2).place(x=200,y=550)
    
        Label(f_g,text="Addresse",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=575)
        Entry(f_g,textvariable=self.Addresse,font=("times new roman",10),bd=2).place(x=7,y=595)

        Label(f_g,text="Dette",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=575)
        Entry(f_g,textvariable=self.Dett,font=("times new roman",10),bd=2).place(x=200,y=595)

        #========Fram_down=======
        dt_F = Frame(self.root,bd=0,relief=RIDGE,bg="#4065a4")
        dt_F.place(x=347,y=630,width=675,height=100)

        Label(dt_F,text="Chercher par...",bg="#4065a4",fg="white",font=("times new roman",15)).grid(row=0,column=0,pady=10,padx=20,sticky="W")
        combo_search = ttk.Combobox(dt_F,textvariable=self.Chercher_par,font=("times new roman",10),width=15)
        combo_search['values']=("ID","Nomc","Temps_Acheter","Temps_restant","DD","Heure","Addresse","Servir_par","Dette")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="W")
        Entry(dt_F,textvariable=self.Chercher,font=("times new roman",10),width=15,bd=2,relief=GROOVE).grid(row=0,column=2,pady=10,padx=20,sticky="W")
        Button(dt_F,text="Rechercher",bg="#4065a4",fg="white",width=7,command=affich_1).grid(row=0,column=3,padx=5,pady=10)
        Button(dt_F,text="Afficher" ,bg="#4065a4",fg="white",width=7,command=afficher).grid(row=0,column=4,padx=5,pady=10)
        Button(dt_F, text="Supprimer" , bg="#4065a4",fg="white",command=supp).grid(row=0,column=5,padx=5,pady=10)                            
        #frame droite
        f_g2= Frame(f_g, width=342,height=35,bg="black",bd=4).place(x=3,y=635)
        Button(f_g2, text="Nouveau" , bg="red",fg="white",command=addcl).place(x=5,y=640)
        Button(f_g2, text="Nettoyer" , bg="red",fg="white",command=NETTOYER).place(x=83,y=640)
        Button(f_g2, text="Actualiser" , bg="red",fg="white",command=D_T).place(x=155,y=640) 
        Entry(f_g2,textvariable=self.vf,font=("times new roman",10),bd=0,bg="#4065a4",fg="red").place(x=30,y=690,width=290,height=15)
        Entry(f_g2,textvariable=self.vff,font=("times new roman",10),bd=0,bg="#4065a4",fg="red").place(x=30,y=675,width=250,height=15)
        D_T()













class hant(tk.Tk):
    root=tk.Tk()
    object= hanta(root)
    root.tk.call('wm','iconphoto', root._w,tk.PhotoImage(file='B2.png'))
    menu_bar=Menu(root)
    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Apropos",command=apropos)
    file_menu.add_command(label="Quitter", command=root.destroy)
    menu_bar.add_cascade(label="Options", menu=file_menu)
    root.config(menu=menu_bar)
    image2=PhotoImage(file='B.png')
    Label1=Label(root,image=image2,border=0,bg="#4065a4").place(x=3,y=140)
    winsound.PlaySound("Windows Notify Email.wav",winsound.SND_ASYNC)
    root.mainloop()
