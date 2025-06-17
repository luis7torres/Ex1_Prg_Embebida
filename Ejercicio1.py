from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
import time

# Crear ventana
v0=Tk()
v0.title("Control GPIO")
v0.geometry("600x400+200+200")

# Declarar imagen
img_on=PhotoImage(file="/home/luistorres/on.gif")
img_off=PhotoImage(file="/home/luistorres/off.gif")

def actualizar():
                 pf=open("/home/luistorres/estado.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if(campof=="1"):
                                                 btn_on=Button(v0,image=img_on).place(x=200,y=50)
                                                 v0.after(1000,actualizar)

                                 if(campof=="0"):
                                                 btn_off=Button(v0,image=img_off).place(x=200,y=50)
                                                 v0.after(1000,actualizar)

# Llamar funcion recursiva
actualizar()

# Zona de funciones
def encender():
               
               print("Encender gpio...")
               os.system("sudo /./home/luistorres/on.sh")
               # Deseleccionamos el checkbox de apagado en caso de que esté seleccionado
               cb_apagado.set(0)
               


def apagar():
               
               print("Apagar Gpio...")
               os.system("sudo /./home/luistorres/off.sh")
               # Deseleccionamos el checkbox de encendido en caso de que esté seleccionado
               cb_encendido.set(0)


def limpiar():
              horai.set("")
              minini.set("")
              horaf.set("")
              minf.set("")

def save():
           hi=str(horai.get())
           mi=str(minini.get())
           hf=str(horaf.get())
           mf=str(minf.get())
           tab=" "
           dia="*"
           mes="*"
           aa="*"
           user="root"
           path1="/home/luistorres/on.sh"
           path2="/home/luistorres/off.sh"
           cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(aa)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
           cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(aa)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
           # Full permisos 777
           os.system("sudo chmod -R 777 /etc/cron.d/tarea1")
           os.system("sudo chmod -R 777 /etc/cron.d/tarea2")
           pf1=open("/etc/cron.d/tarea1","w")
           pf1.write(cadena1)
           pf1.write("\n")
           pf1.close()

           pf2=open("/etc/cron.d/tarea2","w")
           pf2.write(cadena2)
           pf2.write("\n")
           pf2.close()

           #pausa estrategica
           time.sleep(0.1)
           os.system("sudo chmod -R 755 /etc/cron.d/tarea1")
           os.system("sudo chmod -R 755 /etc/cron.d/tarea2")
           messagebox.showinfo("INFO",message="Tiempo Aplicado con Exito")

           limpiar()

def tiempo():
             print("Programando tiempo...")
             v1=Toplevel()
             text2_v1=font.Font(family="Arial",size=12)

             v1.title("Configurar tiempo de los ON/OFF de los GPIO")
             v1.geometry("300x300+300+200")
             label_hi=Label(v1,text="Hora Inicial:",font=text2_v1).place(x=50,y=50)
             label_mi=Label(v1,text="Minuto Inicial:",font=text2_v1).place(x=50,y=80)
             label_hf=Label(v1,text="Hora Final:",font=text2_v1).place(x=50,y=110)
             label_mf=Label(v1,text="Minuto Final:",font=text2_v1).place(x=50,y=140)

             #zona de variable
             global horai,minini,horaf,minf
             horai=StringVar()
             minini=StringVar()
             horaf=StringVar()
             minf=StringVar()

             txt_horai=Entry(v1,textvariable=horai,width=10).place(x=160,y=50)
             txt_minini=Entry(v1,textvariable=minini,width=10).place(x=160,y=80)
             txt_horaf=Entry(v1,textvariable=horaf,width=10).place(x=160,y=110)
             txt_minf=Entry(v1,textvariable=minf,width=10).place(x=160,y=140)

             btn_save=Button(v1,text="Save",command=save).place(x=160,y=200)

             v1.mainloop()
           

def seleccionar_encendido():
                            if cb_encendido.get():
                                                  cb_apagado.set(0)
                                                  # Llamamos la funcion de encender
                                                  encender()
                                                  print("ENCENDIDO esta activado")



def seleccionar_apagado():
                            if cb_apagado.get():
                                                  cb_encendido.set(0)
                                                  # Llamamos la funcion de apagar
                                                  apagar()
                                                  print("APAGADO esta activado")
                            


         

text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=12)

# Variables creadas para el funcionamiento de los ckeckboxes de encendido y apagado
cb_encendido=IntVar()
cb_apagado=IntVar()

# Zona de etiquetas
label_t=Label(v0,text="CONTROL GPIO MICROPROCESADOR",font=text1).place(x=50,y=5)


# Zona de botones
btn_on=Button(v0,text="ON",command=encender).place(x=50,y=100)
btn_off=Button(v0,text="OFF",command=apagar).place(x=50,y=150)
btn_tiempo=Button(v0,text="tiempo",command=tiempo).place(x=350,y=50)

# Zona de los checkboxes
chk_encendido=Checkbutton(v0,text="Encendido",variable=cb_encendido,command=seleccionar_encendido).place(x=45,y=200)
chk_apagado=Checkbutton(v0,text="Apagado",variable=cb_apagado,command=seleccionar_apagado).place(x=45,y=250)

v0.mainloop()









                                                 
