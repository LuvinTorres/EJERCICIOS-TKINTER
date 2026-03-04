from modelo_usuario import Usuario
from modelo_parqueadero import Parqueadero
from modelo_carro import Carro
import tkinter as ventana
from tkinter import messagebox

parqueadero = Parqueadero(1, "26/02/2026")

#Funciones-----------------------------------------------------------------------------------------------

def guardar():
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    tipo_cliente = entry_tipo_cliente.get()
    placa = entry_placa.get()
    marca = entry_marca.get()
    color = entry_color.get()
    hora = entry_hora.get()

    if "" in [nombre, cedula, tipo_cliente, placa, marca, color, hora]:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
    else:
        usuario = Usuario(nombre, cedula, tipo_cliente)
        carro = Carro(placa, marca, color)

        mensaje_parqueadero = parqueadero.registrar_entrada(usuario, carro, hora)

        messagebox.showinfo("Registro Exitoso", mensaje_parqueadero)

def borrar():
    entry_nombre.delete(0, ventana.END)
    entry_cedula.delete(0, ventana.END)
    entry_tipo_cliente.delete(0, ventana.END)
    entry_placa.delete(0, ventana.END)
    entry_marca.delete(0, ventana.END)
    entry_color.delete(0, ventana.END)
    entry_hora.delete(0, ventana.END)

def registrar_salida():
    hora = entry_hora.get()

    if hora == "":
        messagebox.showwarning("Error", "Ingrese la hora de salida")
    else:
        mensaje = parqueadero.registrar_salida(hora)
        messagebox.showinfo("Salida", mensaje)


def verificar_espacio():
    if parqueadero.hay_espacio():
        messagebox.showinfo("Espacio", "Hay espacio disponible")
    else:
        messagebox.showwarning("Espacio", "No hay espacio disponible")

def mostrar_registros():
    informacion = parqueadero.mostrar_info()

    if informacion == "":
        messagebox.showinfo("Registros", "No hay registros aún")
    else:
        messagebox.showinfo("Registros del Parqueadero", informacion)



#Codigo Principal-----------------------------------------------------------------------------------------

obj_ventana = ventana.Tk()

obj_ventana.title("PARQUEADERO")
obj_ventana.geometry("600x600")


titulo_label = ventana.Label(obj_ventana, text="                     PARQUEADERO                    ")
titulo_label.config(bg="#502C2C", font=("Times New Roman", 30), fg="#FFFFFF")
titulo_label.pack()

seccion1 = ventana.Frame(obj_ventana, bg="#6B0000")
seccion1.pack()

titulo_seccion1 = ventana.Label(seccion1, text="                     Datos de usuario                     ")
titulo_seccion1.config(bg="#6B0000", font=("Times New Roman", 20), fg="#ECF0F1")
titulo_seccion1.pack()

#-----------------------------------------------------------------------
label_nombre = ventana.Label(seccion1, text="                 Digite el nombre:                  " )
label_nombre.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_nombre.pack()

entry_nombre=ventana.Entry(seccion1)
entry_nombre.config(bg="black", font=("Helvetica", 13), fg="white")
entry_nombre.pack()
#-----------------------------------------------------------------------

label_cedula = ventana.Label(seccion1, text="                 Numero de cedula:                ")
label_cedula.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_cedula.pack()

entry_cedula=ventana.Entry(seccion1)
entry_cedula.config(bg="black", font=("Helvetica", 13), fg="white")
entry_cedula.pack()

#-----------------------------------------------------------------------

label_tipo_cliente= ventana.Label(seccion1, text="                     Tipo de cliente:                     ")
label_tipo_cliente.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_tipo_cliente.pack()

entry_tipo_cliente=ventana.Entry(seccion1)
entry_tipo_cliente.config(bg="black", font=("Helvetica", 13), fg="white")
entry_tipo_cliente.pack()

label_placa= ventana.Label(seccion1, text="                     Placa:                     ")
label_placa.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_placa.pack()

entry_placa=ventana.Entry(seccion1)
entry_placa.config(bg="black", font=("Helvetica", 13), fg="white")
entry_placa.pack()

label_marca= ventana.Label(seccion1, text="                     Marca:                     ")
label_marca.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_marca.pack()

entry_marca=ventana.Entry(seccion1)
entry_marca.config(bg="black", font=("Helvetica", 13), fg="white")
entry_marca.pack()

label_color= ventana.Label(seccion1, text="                     Color:                     ")
label_color.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_color.pack()

entry_color=ventana.Entry(seccion1)
entry_color.config(bg="black", font=("Helvetica", 13), fg="white")
entry_color.pack()

#-----------------------------------------------------------------------
label_hora = ventana.Label(seccion1, text="                     Hora (entrada o salida):                     ")
label_hora.config(bg="#6B0000", font=("Times New Roman", 13), fg="#ECF0F1")
label_hora.pack()

entry_hora = ventana.Entry(seccion1)
entry_hora.config(bg="black", font=("Helvetica", 13), fg="white")
entry_hora.pack()

#-----------------------------------------------------------------------------------

boton_enviar=ventana.Button(seccion1, text= "Guardar", command= guardar)
boton_enviar.config(bg= "black", font= ("Times New Roman", 8), fg= "#2ECC71")
boton_enviar.pack(pady=5)

boton_borrar = ventana.Button(seccion1, text="Borrar", command=borrar)
boton_borrar.config(bg= "black", font= ("Times New Roman", 8), fg= "#F1C40F")
boton_borrar.pack(pady=5)

boton_salida = ventana.Button(seccion1, text="Registrar Salida", command=registrar_salida)
boton_salida.config(bg="black", font=("Times New Roman", 8), fg="#F1C40F")
boton_salida.pack(pady=5)

boton_espacio = ventana.Button(seccion1, text="¿Hay espacio?", command=verificar_espacio)
boton_espacio.config(bg="black", font=("Times New Roman", 8), fg="#F1C40F")
boton_espacio.pack(pady=5)

boton_acumulado = ventana.Button(seccion1, text="Mostrar Registros", command=mostrar_registros)
boton_acumulado.config(bg="black", font=("Times New Roman", 8), fg="#F1C40F")
boton_acumulado.pack(pady=5)


obj_ventana.mainloop()


obj_ventana.mainloop()
