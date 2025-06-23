import tkinter as tk

def abrir_registro():
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registrar Paciente")
    ventana_registro.geometry("500x400") 
    ventana_registro.configure(bg="#ffc0cb") 

    tk.Label(ventana_registro, text="Nombre:", bg="#ffc0cb").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Edad:", bg="#ffc0cb").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_edad = tk.Entry(ventana_registro)
    entry_edad.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Teléfono:", bg="#ffc0cb").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_telefono = tk.Entry(ventana_registro)
    entry_telefono.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Día de cita:", bg="#ffc0cb").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_dia = tk.Entry(ventana_registro)
    entry_dia.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Hora:", bg="#ffc0cb").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_hora = tk.Entry(ventana_registro)
    entry_hora.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Doctor:", bg="#ffc0cb").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_doctor = tk.Entry(ventana_registro)
    entry_doctor.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Problema:", bg="#ffc0cb").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_problema = tk.Entry(ventana_registro)
    entry_problema.grid(row=6, column=1, padx=10, pady=5)

    def guardar_paciente():
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        telefono = entry_telefono.get()
        dia = entry_dia.get()
        hora = entry_hora.get()
        doctor = entry_doctor.get()
        problema = entry_problema.get()

        if nombre and edad and telefono and dia and hora and doctor and problema:
            with open("pacientes.txt", "a") as archivo:
                archivo.write(f"Nombre: {nombre}, Edad: {edad}, Teléfono: {telefono}, Día: {dia}, Hora: {hora}, Doctor: {doctor}, Problema: {problema}\n")
            
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            entry_dia.delete(0, tk.END)
            entry_hora.delete(0, tk.END)
            entry_doctor.delete(0, tk.END)
            entry_problema.delete(0, tk.END)

    tk.Button(ventana_registro, text="Guardar", command=guardar_paciente).grid(row=7, column=0, columnspan=2, pady=10)

ventana_principal = tk.Tk()
ventana_principal.title("Clínica")
ventana_principal.geometry("500x400") 
ventana_principal.configure(bg="#ffc0cb") 

tk.Label(ventana_principal, text="Bienvenido", font=("Arial", 14), bg="#ffc0cb").pack(pady=10)

tk.Button(ventana_principal, text="Iniciar Sesión", width=20).pack(pady=5) 
tk.Button(ventana_principal, text="Registrar Paciente", command=abrir_registro, width=20).pack(pady=5)

ventana_principal.mainloop()
