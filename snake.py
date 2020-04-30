from tkinter import *
from tkinter import messagebox
import random


root = Tk()


en_x_p=0
en_y_p=0
en_x_n=0
en_y_n=0
cuerpo=[]
posiciones={}
f_ca=0.0
c_ca=0.0
cuenta=0.0
hay_comida=True
comida_px=0
comida_py=0
comida=0
cabeza=[]
vel=500


def inicio():


	def pintar_snake(index, dire):
		global en_x_p
		global en_x_n
		global en_y_p
		global en_y_n
		global cuerpo
		global posiciones
		global cuenta

		px=cuerpo[index][1][0]
		py=cuerpo[index][1][1]
		Etiqueta=cuerpo[index][0]
		# dire=cuerpo[index][1][2] # cambie esta

		if dire=="en_y_n":
				
			Etiqueta.place(relx=px,rely=round(py-0.05,3), relheight=0.05, relwidth=0.05)
			cuerpo[index][1][0]=px
			cuerpo[index][1][1]=round(py-0.05,3)
			cuerpo[index][1][2]="en_y_n"

		elif dire=="en_y_p":

			Etiqueta.place(relx=px,rely=round(py+0.05,3), relheight=0.05, relwidth=0.05)
			cuerpo[index][1][0]=px
			cuerpo[index][1][1]=round(py+0.05,3)
			cuerpo[index][1][2]="en_y_p"

		elif dire=="en_x_n":

			Etiqueta.place(relx=round(px-0.05,3),rely=py, relheight=0.05, relwidth=0.05)
			cuerpo[index][1][0]=round(px-0.05,3)
			cuerpo[index][1][1]=py
			cuerpo[index][1][2]="en_x_n"

		elif dire=="en_x_p":

			Etiqueta.place(relx=round(px+0.05,3),rely=py, relheight=0.05, relwidth=0.05)
			cuerpo[index][1][0]=round(px+0.05,3)
			cuerpo[index][1][1]=py
			cuerpo[index][1][2]="en_x_p"


	def mover():
		global cuerpo
		global posiciones
		global vel

		
		for i,c in enumerate(cuerpo):
			px= c[1][0]
			py= c[1][1]
			p=(px,py)
			if p in posiciones:
				cruse=posiciones[p]
				pintar_snake(i,cruse)
				if i== len(cuerpo)-1:
					posiciones.pop(p)
			else:
				if c[1][1]<0:
					c[1][1]=1.05
					pintar_snake(i,c[1][2])
				if c[1][1]>1:
					c[1][1]=-0.1
					pintar_snake(i,c[1][2])
				if c[1][0]<0:
					c[1][0]=1.05
					pintar_snake(i,c[1][2])
				if c[1][0]>1:
					c[1][0]=-0.05
					pintar_snake(i,c[1][2])
				else:
					pintar_snake(i,c[1][2])

		cabeza=[cuerpo[0][1][0],cuerpo[0][1][1]]
		print(cabeza)

		if cuerpo[0][1][2]=="en_y_n":
				
			cuerpo[0][0].config(image=imagen_cabeza_ar)

		elif cuerpo[0][1][2]=="en_y_p":
			cuerpo[0][0].config(image=imagen_cabeza_ab)

		elif cuerpo[0][1][2]=="en_x_n":
			cuerpo[0][0].config(image=imagen_cabeza_iz)

		elif cuerpo[0][1][2]=="en_x_p":
			cuerpo[0][0].config(image=imagen_cabeza_dr)
				

		if cabeza==[comida_px,comida_py]:
			comida.destroy()
			ultima_direc=cuerpo[len(cuerpo)-1][1][2]
			
			if ultima_direc=="en_y_n":
				
				cuerpo.append([Label(frame,bg="black",bd=2,relief=GROOVE), [cuerpo[(len(cuerpo)-1)][1][0],cuerpo[len(cuerpo)-1][1][1]+0.05,cuerpo[len(cuerpo)-1][1][2]]])

			elif ultima_direc=="en_y_p":

				cuerpo.append([Label(frame,bg="black",bd=2,relief=GROOVE), [cuerpo[(len(cuerpo)-1)][1][0],cuerpo[len(cuerpo)-1][1][1]-0.05,cuerpo[len(cuerpo)-1][1][2]]])

			elif ultima_direc=="en_x_n":

				cuerpo.append([Label(frame,bg="black",bd=2,relief=GROOVE), [cuerpo[(len(cuerpo)-1)][1][0]+0.05,cuerpo[len(cuerpo)-1][1][1],cuerpo[len(cuerpo)-1][1][2]]])

			elif ultima_direc=="en_x_p":

				cuerpo.append([Label(frame,bg="black",bd=2,relief=GROOVE), [cuerpo[(len(cuerpo)-1)][1][0]-0.05,cuerpo[len(cuerpo)-1][1][1],cuerpo[len(cuerpo)-1][1][2]]])


			if len(cuerpo) in range(0,4):
				vel-=50
			elif len(cuerpo) in range(5,15):
				vel-=20
			elif len(cuerpo) > 15:
				vel-=5
			crear_comida()

		for x in cuerpo[1:]:
			mi_x=x[1][0]
			mi_y=x[1][1]

			if cabeza==[mi_x,mi_y]:
				messagebox.showerror("Perdiste","Chocaste")
				root.destroy()

			
	def crear_comida():
		global hay_comida
		global comida_px
		global comida_py
		global comida
		mi_lista=[]
		x=0

		while x<=1:
			mi_lista.append(x+0.050)
			x+=0.050

		comida_px=round(random.choice(mi_lista),3)
		comida_py=round(random.choice(mi_lista),3)

		comida=Label(frame,bg="red",bd=2,relief=GROOVE)
		comida.place(relx=comida_px, rely=comida_py, relwidth=0.040, relheight=0.040)
		hay_comida=False


	def mueve_arriba():
		global cuerpo
		global en_y_n
		global posiciones
		global vel

		if en_y_n==1:

			mover()
			root.after(vel,mueve_arriba)
							

	def mueve_abajo():
		global vel
		global en_y_p

		if en_y_p==1:

			mover()
			root.after(vel,mueve_abajo)

	def mueve_izq():
		global vel
		global en_x_n

		if en_x_n==1:
			mover()
			root.after(vel,mueve_izq)


	def mueve_der():
		global en_x_p
		global vel

		if en_x_p==1:
			mover()
			root.after(vel,mueve_der)


	def Arriba(event):
		global en_x_p
		global en_x_n
		global en_y_p
		global en_y_n
		global cuerpo
		global posiciones


		if en_y_p==0 :
			en_x_p=0
			en_y_p=0
			en_x_n=0
			en_y_n=1
			f_ca=cuerpo[0][1][0]
			c_ca=cuerpo[0][1][1]
			posiciones[f_ca,c_ca]="en_y_n"
			mueve_arriba()


	def Abajo(event):
		global en_x_p
		global en_x_n
		global en_y_p
		global en_y_n
		global cuerpo
		global posiciones

		if en_y_n==0:
			en_x_p=0
			en_y_p=1
			en_x_n=0
			en_y_n=0
			f_ca=cuerpo[0][1][0]
			c_ca=cuerpo[0][1][1]
			posiciones[f_ca,c_ca]="en_y_p"
			mueve_abajo()

	def Izq(event):
		global en_x_p
		global en_x_n
		global en_y_p
		global en_y_n
		global posiciones
		global cuerpo

		if en_x_p==0:

			en_x_p=0
			en_y_p=0
			en_x_n=1
			en_y_n=0
			f_ca=cuerpo[0][1][0]
			c_ca=cuerpo[0][1][1]
			posiciones[f_ca,c_ca]="en_x_n"
			mueve_izq()
		

	def Der(event):
		global en_x_p
		global en_x_n
		global en_y_p
		global en_y_n
		global cuerpo
		global posiciones

		if en_x_n==0:
			en_x_p=1
			en_y_p=0
			en_x_n=0
			en_y_n=0
			f_ca=cuerpo[0][1][0]
			c_ca=cuerpo[0][1][1]
			posiciones[f_ca,c_ca]="en_x_p"
			mueve_der()

	if hay_comida==True:
		crear_comida()

	def callback(event):
	   frame.focus_set()
	   mueve_arriba()

	frame.bind("<Up>",Arriba)
	frame.bind("<Down>",Abajo)
	frame.bind("<Left>",Izq)
	frame.bind("<Right>",Der)
	frame.bind("<Button-1>", callback)


mi_menu=Menu(root)

menu_nuevo=Menu(mi_menu, tearoff=0)
menu_nuevo.add_command(label="Nuevo", command=inicio)

mi_menu.add_cascade(label="Juego",menu=menu_nuevo)

imagen_cabeza_ar=PhotoImage(file="head_ar.png")
imagen_cabeza_ab=PhotoImage(file="head_ab.png")
imagen_cabeza_iz=PhotoImage(file="head_iz.png")
imagen_cabeza_dr=PhotoImage(file="head_dr.png")

root.config(menu=mi_menu)

frame = Frame(root, relief=GROOVE, bd=5)
frame.place(relx=0,rely=0, relwidth= 1, relheight=1)


for x in range(0,1) :
	cuerpo.append([Label(frame,bg="black",bd=2,relief=GROOVE), [0.5, 1+cuenta,"en_y_n"]])
	cuenta+=0.05


root.geometry("500x500")

root.mainloop()
