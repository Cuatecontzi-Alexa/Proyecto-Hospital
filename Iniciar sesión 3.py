import tkinter as tk

def abrir_registro():
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registrar Paciente")
    ventana_registro.geometry("500x400")
    ventana_registro.configure(bg="#ffc0cb")

    tk.Label(ventana_registro, text="Nombre:", bg="#ffc0cb").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana_registro, width=30)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana_registro, text="Edad:", bg="#ffc0cb").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_edad = tk.Entry(ventana_registro, width=30)
    entry_edad.grid(row=1, column=1)

    tk.Label(ventana_registro, text="Telefono:", bg="#ffc0cb").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_telefono = tk.Entry(ventana_registro, width=30)
    entry_telefono.grid(row=2, column=1)

    tk.Label(ventana_registro, text="Dia de cita:", bg="#ffc0cb").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_dia = tk.Entry(ventana_registro, width=30)
    entry_dia.grid(row=3, column=1)

    tk.Label(ventana_registro, text="Hora:", bg="#ffc0cb").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_hora = tk.Entry(ventana_registro, width=30)
    entry_hora.grid(row=4, column=1)

    tk.Label(ventana_registro, text="Con quien:", bg="#ffc0cb").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    opcion_personal = tk.StringVar()
    opcion_personal.set("Doctor")
    tk.OptionMenu(ventana_registro, opcion_personal, "Doctor", "Enfermera").grid(row=5, column=1)

    tk.Label(ventana_registro, text="Problema:", bg="#ffc0cb").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_problema = tk.Entry(ventana_registro, width=30)
    entry_problema.grid(row=6, column=1)

    def guardar_paciente():
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        telefono = entry_telefono.get()
        dia = entry_dia.get()
        hora = entry_hora.get()
        con_quien = opcion_personal.get()
        problema = entry_problema.get()

        if nombre and edad and telefono and dia and hora and con_quien and problema:
            with open("pacientes.txt", "a") as archivo:
                archivo.write(f"Nombre: {nombre}, Edad: {edad}, Telefono: {telefono}, Dia: {dia}, Hora: {hora}, Con: {con_quien}, Problema: {problema}\n")

            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            entry_dia.delete(0, tk.END)
            entry_hora.delete(0, tk.END)
            entry_problema.delete(0, tk.END)

    tk.Button(ventana_registro, text="Guardar", command=guardar_paciente, width=20).grid(row=7, column=0, columnspan=2, pady=10)

def iniciar_sesion():
    ventana_login = tk.Toplevel(ventana_principal)
    ventana_login.title("Iniciar Sesion")
    ventana_login.geometry("300x250")
    ventana_login.configure(bg="#ffc0cb")

    tk.Label(ventana_login, text="Usuario:", bg="#ffc0cb").pack(pady=5)
    entry_usuario = tk.Entry(ventana_login)
    entry_usuario.pack()

    tk.Label(ventana_login, text="Contrasena:", bg="#ffc0cb").pack(pady=5)
    entry_contrasena = tk.Entry(ventana_login, show="*")
    entry_contrasena.pack()

    def verificar():
        usuario = entry_usuario.get().lower()
        contrasena = entry_contrasena.get()

        if usuario in ["doctor", "enfermera"] and contrasena == "123":
            mostrar_citas(usuario)
        else:
            tk.Label(ventana_login, text="Datos incorrectos", fg="red", bg="#ffc0cb").pack(pady=5)

    tk.Button(ventana_login, text="Entrar", command=verificar).pack(pady=10)

def mostrar_citas(tipo_usuario):
    try:
        with open("pacientes.txt", "r") as archivo:
            citas = [linea.strip() for linea in archivo if f"Con: {tipo_usuario.capitalize()}" in linea]

        ventana_citas = tk.Toplevel(ventana_principal)
        ventana_citas.title(f"Citas para {tipo_usuario.capitalize()}")
        ventana_citas.geometry("500x400")
        ventana_citas.configure(bg="#ffc0cb")

        if citas:
            for c in citas:
                tk.Label(ventana_citas, text=c, bg="#ffc0cb").pack(anchor="w", padx=10, pady=2)
        else:
            tk.Label(ventana_citas, text="No hay citas registradas.", bg="#ffc0cb").pack(pady=20)
    except FileNotFoundError:
        ventana_error = tk.Toplevel(ventana_principal)
        ventana_error.title("Error")
        tk.Label(ventana_error, text="No hay archivo de citas aún.", bg="#ffc0cb").pack(padx=20, pady=20)

ventana_principal = tk.Tk()
ventana_principal.title("Clínica")
ventana_principal.geometry("500x400")
ventana_principal.configure(bg="#ffc0cb")

tk.Label(ventana_principal, text="Bienvenido", font=("Arial", 18), bg="#ffc0cb").pack(pady=30)
tk.Button(ventana_principal, text="Iniciar Sesion", width=25, command=iniciar_sesion).pack(pady=10)
tk.Button(ventana_principal, text="Registrar Paciente", width=25, command=abrir_registro).pack(pady=10)

ventana_principal.mainloop()
