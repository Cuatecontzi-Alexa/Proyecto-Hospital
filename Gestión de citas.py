import tkinter as tk
import os

def mostrar_saludo():
    limpiar_frame_contenido()
    tk.Label(frame_contenido, text="¡Hola! Bienvenido al Hospital ", font=("Comic Sans MS", 16), bg="#ffe6ec").pack(pady=20)

def abrir_registro():
    limpiar_frame_contenido()
    tk.Label(frame_contenido, text="Registrar Paciente", font=("Helvetica", 14, "bold"), bg="#ffe6ec").pack(pady=10)

    campos = {
        "Nombre": tk.Entry(frame_contenido, width=30),
        "Edad": tk.Entry(frame_contenido, width=30),
        "Telefono": tk.Entry(frame_contenido, width=30),
        "Dia de cita": tk.Entry(frame_contenido, width=30),
        "Hora": tk.Entry(frame_contenido, width=30),
        "Problema": tk.Entry(frame_contenido, width=30)
    }

    for label, entry in campos.items():
        tk.Label(frame_contenido, text=label + ":", bg="#ffe6ec", font=("Helvetica", 10)).pack()
        entry.pack()

    tk.Label(frame_contenido, text="Con quien:", bg="#ffe6ec", font=("Helvetica", 10)).pack()
    opcion_personal = tk.StringVar()
    opcion_personal.set("Doctor")
    tk.OptionMenu(frame_contenido, opcion_personal, "Doctor", "Enfermera").pack()

    def guardar():
        datos = [entry.get() for entry in campos.values()]
        con_quien = opcion_personal.get()

        if all(datos):
            with open("pacientes.txt", "a") as archivo:
                archivo.write(
                    f"Nombre: {datos[0]}\nEdad: {datos[1]}\nTelefono: {datos[2]}\nDia: {datos[3]}\nHora: {datos[4]}\nCon: {con_quien}\nProblema: {datos[5]}\n{'-'*40}\n"
                )
            for entry in campos.values():
                entry.delete(0, tk.END)

    tk.Button(frame_contenido, text="Guardar", font=("Helvetica", 10), command=guardar).pack(pady=10)

def iniciar_sesion():
    limpiar_frame_contenido()
    tk.Label(frame_contenido, text="Iniciar Sesión", font=("Helvetica", 14, "bold"), bg="#ffe6ec").pack(pady=10)

    tk.Label(frame_contenido, text="Usuario:", bg="#ffe6ec", font=("Helvetica", 10)).pack()
    entry_usuario = tk.Entry(frame_contenido)
    entry_usuario.pack()

    tk.Label(frame_contenido, text="Contrasena:", bg="#ffe6ec", font=("Helvetica", 10)).pack()
    entry_contrasena = tk.Entry(frame_contenido, show="*")
    entry_contrasena.pack()

    def verificar():
        usuario = entry_usuario.get().lower()
        contrasena = entry_contrasena.get()
        if usuario in ["doctor", "enfermera"] and contrasena == "123":
            mostrar_citas(usuario)
        else:
            tk.Label(frame_contenido, text="Datos incorrectos", fg="red", bg="#ffe6ec", font=("Helvetica", 10)).pack(pady=5)

    tk.Button(frame_contenido, text="Entrar", font=("Helvetica", 10), command=verificar).pack(pady=10)

def mostrar_citas(tipo_usuario):
    limpiar_frame_contenido()
    tk.Label(frame_contenido, text=f"Citas para {tipo_usuario.capitalize()}", font=("Helvetica", 14, "bold"), bg="#ffe6ec").pack(pady=10)

    try:
        with open("pacientes.txt", "r") as archivo:
            contenido = archivo.read()
            citas = contenido.strip().split("-" * 40)
            citas_filtradas = [c.strip() for c in citas if f"Con: {tipo_usuario.capitalize()}" in c]

            if citas_filtradas:
                for cita in citas_filtradas:
                    tk.Label(frame_contenido, text=cita, bg="#ffe6ec", font=("Helvetica", 10), justify="left", anchor="w").pack(padx=10, pady=5, fill="x")
            else:
                tk.Label(frame_contenido, text="No hay citas registradas.", bg="#ffe6ec", font=("Helvetica", 10)).pack(pady=10)
    except FileNotFoundError:
        tk.Label(frame_contenido, text="No hay archivo de citas aún.", bg="#ffe6ec", font=("Helvetica", 10)).pack(pady=10)

def reiniciar_citas():
    limpiar_frame_contenido()
    if os.path.exists("pacientes.txt"):
        with open("pacientes.txt", "w") as archivo:
            archivo.write("")
    if os.path.exists("gestion_citas.txt"):
        with open("gestion_citas.txt", "w") as archivo:
            archivo.write("")
    tk.Label(frame_contenido, text="¡Citas borradas exitosamente!", font=("Helvetica", 12), bg="#ffe6ec").pack(pady=20)

def gestion_citas():
    limpiar_frame_contenido()
    tk.Label(frame_contenido, text="Gestión de Citas", font=("Helvetica", 14, "bold"), bg="#ffe6ec").pack(pady=10)

    entradas = {}

    campos = ["Nombre del Paciente", "Enfermedad", "Doctor", "Hora", "Habitación", "Camilla"]
    for campo in campos:
        tk.Label(frame_contenido, text=campo + ":", bg="#ffe6ec", font=("Helvetica", 10)).pack()
        entrada = tk.Entry(frame_contenido, width=30)
        entrada.pack()
        entradas[campo] = entrada

    def guardar_cita():
        datos = [entradas[campo].get() for campo in campos]
        if all(datos):
            with open("gestion_citas.txt", "a") as archivo:
                archivo.write(
                    f"Nombre: {datos[0]}\n Enfermedad: {datos[1]}\n Doctor: {datos[2]}\n Hora: {datos[3]}\n Habitación: {datos[4]} \n Camilla: {datos[5]}\n"
                )
            for entrada in entradas.values():
                entrada.delete(0, tk.END)
            mostrar_citas_guardadas()

    tk.Button(frame_contenido, text="Guardar Cita", font=("Helvetica", 10), command=guardar_cita).pack(pady=10)

    def mostrar_citas_guardadas():
        if os.path.exists("gestion_citas.txt"):
            with open("gestion_citas.txt", "r") as archivo:
                citas = archivo.readlines()
                for cita in citas:
                    if cita.strip():
                        tk.Label(frame_contenido, text=cita.strip(), bg="#ffe6ec", justify="left", anchor="w", font=("Helvetica", 9)).pack(padx=10, pady=3, fill="x")

    mostrar_citas_guardadas()

def limpiar_frame_contenido():
    for widget in frame_contenido.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Hospital")
ventana_principal.geometry("900x500")
ventana_principal.configure(bg="#ffe6ec")

frame_menu = tk.Frame(ventana_principal, width=200, bg="#ffb6c1")
frame_menu.pack(side="left", fill="y")

tk.Label(frame_menu, text="Menú", font=("Comic Sans MS", 16), bg="#ffb6c1").pack(pady=20)
tk.Button(frame_menu, text="Saludo", font=("Helvetica", 10), width=20, command=mostrar_saludo).pack(pady=10)
tk.Button(frame_menu, text="Iniciar Sesión", font=("Helvetica", 10), width=20, command=iniciar_sesion).pack(pady=10)
tk.Button(frame_menu, text="Registrar Cita", font=("Helvetica", 10), width=20, command=abrir_registro).pack(pady=10)
tk.Button(frame_menu, text="Gestion de Citas", font=("Helvetica", 10), width=20, command=gestion_citas).pack(pady=10)
tk.Button(frame_menu, text="Reiniciar Citas", font=("Helvetica", 10), width=20, command=reiniciar_citas).pack(pady=10)

frame_contenido = tk.Frame(ventana_principal, bg="#ffe6ec")
frame_contenido.pack(expand=True, fill="both")

mostrar_saludo()

ventana_principal.mainloop()

