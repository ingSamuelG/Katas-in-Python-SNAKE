from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(width=1200, height=800)
posx=0.5
posy=0.5
en_x_p=0
en_y_p=0
en_x_n=0
en_y_n=0

def mueve_arriba():
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n


	if en_y_n==1 and 1>posy>0:
		posy-=0.010
		snake.place(relx=posx, rely=posy)
		print("posicion Y: ",posy)
		print("posicion X: ",posx)
		root.after(100,mueve_arriba)
		en_x_p=0
		en_y_p=0
		en_x_n=0
		en_y_n=1
	elif 0>posy or posy>1:
		respuesta=messagebox.askquestion("Perdiste", "Perdiste al chocar con el Borde deseas intentarlo de nuevo")
		if respuesta=="no":
			root.destroy()
				



def mueve_abajo():
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_y_p==1 and 1>posy>0:
		posy+=0.010
		snake.place(relx=posx, rely=posy)
		print("posicion Y: ",posy)
		print("posicion X: ",posx)		
		root.after(100,mueve_abajo)
		en_x_p=0
		en_y_p=1
		en_x_n=0
		en_y_n=0
	elif 0>posy or posy>1:
		respuesta=messagebox.askquestion("Perdiste", "Perdiste al chocar con el Borde deseas intentarlo de nuevo")
		if respuesta=="no":
			root.destroy()

def mueve_izq():
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_x_n==1 and 1>posx>0:
		posx-=0.010
		snake.place(relx=posx, rely=posy)
		print("posicion Y: ",posy)
		print("posicion X: ",posx)
		root.after(100,mueve_izq)
		en_x_p=0
		en_y_p=0
		en_x_n=1
		en_y_n=0
	elif 0>posx or posx>1:
		respuesta=messagebox.askquestion("Perdiste", "Perdiste al chocar con el Borde deseas intentarlo de nuevo")
		if respuesta=="no":
			root.destroy()


def mueve_der():
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_x_p==1 and 1>posx>0:
		posx+=0.010
		snake.place(relx=posx, rely=posy)
		print("posicion Y: ",posy)
		print("posicion X: ",posx)
		root.after(100,mueve_der)
		en_x_p=1
		en_y_p=0
		en_x_n=0
		en_y_n=0
	elif 0>posx or posx>1:
		respuesta=messagebox.askquestion("Perdiste", "Perdiste al chocar con el Borde deseas intentarlo de nuevo")
		if respuesta=="no":
			root.destroy()



def Arriba(event):
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_y_p==0 :
		snake.place(relx=posx, rely=posy)
		print("posicion Y: ",posy)
		print("posicion X: ",posx)
		en_x_p=0
		en_y_p=0
		en_x_n=0
		en_y_n=1
		mueve_arriba()

def Abajo(event):
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_y_n==0:
		# posy+=0.010
		snake.place(relx=posx, rely=posy)
		en_x_p=0
		en_y_p=1
		en_x_n=0
		en_y_n=0
		mueve_abajo()

def Izq(event):
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_x_p==0:
		# posx-=0.010
		snake.place(relx=posx, rely=posy)
		en_x_p=0
		en_y_p=0
		en_x_n=1
		en_y_n=0
		mueve_izq()

def Der(event):
	global posx
	global posy
	global en_x_p
	global en_x_n
	global en_y_p
	global en_y_n

	if en_x_n==0:
		# posx+=0.010
		snake.place(relx=posx, rely=posy)
		en_x_p=1
		en_y_p=0
		en_x_n=0
		en_y_n=0
		mueve_der()	

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)



frame = Frame(root, bg="blue")
frame.place(relx=0.05, rely=0.05,relwidth=0.9, relheight=0.9)


snake=Label(frame,bg="black",bd=2,relief=GROOVE)


# PantallaScore=Entry(frame, width=40)
# PantallaScore.grid(row=100,column=100)


frame.bind("<Up>",Arriba)
frame.bind("<Down>",Abajo)
frame.bind("<Left>",Izq)
frame.bind("<Right>",Der)
frame.bind("<Button-1>", callback)


root.mainloop()
