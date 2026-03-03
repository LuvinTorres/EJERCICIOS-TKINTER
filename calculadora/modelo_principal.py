import tkinter as tk
from tkinter import messagebox

from modelo_usuario import Usuario
from modelo_numero import Numero
from modelo_calculadora import Calculadora


# ---------- FUNCION CALCULAR ----------

def calcular():

    try:
        usuario = Usuario(entry_nombre.get(), entry_id.get())

        num1 = Numero(int(entry_num1.get()))
        num2 = Numero(int(entry_num2.get()))

        calculadora.operacion = operacion_var.get()

        resultado = calculadora.hacer_operaciones(num1, num2)

        label_resultado.config(text=f"Resultado: {resultado}")

        calculadora.guardar_info(usuario,num1.get_numero(),num2.get_numero())

        

    except ValueError:
        messagebox.showerror("Error", "Ingrese numeros validos")



# ---------- VENTANA ----------

root = tk.Tk()
root.title("Calculadora Profesional")
root.geometry("600x600")
root.configure(bg="#1e1e2f")

calculadora = Calculadora("17/02/2026")

# ---------- TITULO ----------

tk.Label(root,text="CALCULADORA",font=("Arial", 18, "bold"),bg="#1e1e2f",fg="white").pack(pady=15)

# ---------- FRAME PRINCIPAL ----------

frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=20)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# ---------- USUARIO ----------

tk.Label(frame, text="Nombre", bg="#2c2c3e", fg="white").grid(row=0, column=0, pady=5, sticky="w")
entry_nombre = tk.Entry(frame, width=25)
entry_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame, text="ID", bg="#2c2c3e", fg="white").grid(row=1, column=0, pady=5, sticky="w")
entry_id = tk.Entry(frame, width=25)
entry_id.grid(row=1, column=1, pady=5)

# ---------- NUMEROS ----------

tk.Label(frame, text="Numero 1", bg="#2c2c3e", fg="white").grid(row=2, column=0, pady=5, sticky="w")
entry_num1 = tk.Entry(frame, width=25)
entry_num1.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Numero 2", bg="#2c2c3e", fg="white").grid(row=3, column=0, pady=5, sticky="w")
entry_num2 = tk.Entry(frame, width=25)
entry_num2.grid(row=3, column=1, pady=5)

# ---------- RADIO BUTTONS ----------

operacion_var = tk.StringVar()
operacion_var.set("suma")

tk.Label(frame, text="Operacion", bg="#2c2c3e", fg="white").grid(row=4, column=0, pady=10, sticky="w")

tk.Radiobutton(frame, text="Suma", variable=operacion_var,
               value="suma", bg="#2c2c3e", fg="white",
               selectcolor="#444").grid(row=4, column=1, sticky="w")

tk.Radiobutton(frame, text="Resta", variable=operacion_var,
               value="resta", bg="#2c2c3e", fg="white",
               selectcolor="#444").grid(row=5, column=1, sticky="w")

tk.Radiobutton(frame, text="Multiplicar", variable=operacion_var,
               value="multiplicar", bg="#2c2c3e", fg="white",
               selectcolor="#444").grid(row=6, column=1, sticky="w")

tk.Radiobutton(frame, text="Dividir", variable=operacion_var,
               value="dividir", bg="#2c2c3e", fg="white",
               selectcolor="#444").grid(row=7, column=1, sticky="w")

# ---------- BOTON ----------

tk.Button(frame,text="Calcular",command=calcular,bg="#4CAF50",fg="white",font=("Arial", 10, "bold"),width=20).grid(row=8, column=0, columnspan=2, pady=15)

# ---------- RESULTADO ----------

label_resultado = tk.Label(frame,text="Resultado:",font=("Arial", 12, "bold"),bg="#2c2c3e",fg="#00ffcc")
label_resultado.grid(row=9, column=0, columnspan=2, pady=10)


root.mainloop()