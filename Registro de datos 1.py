import tkinter as tk

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    if nombre and edad:
        with open("datos_guardados.txt", "a") as archivo:
            archivo.write(f"Nombre: {nombre}, Edad: {edad}\n")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)

def mostrar_datos():
    try:
        with open("datos_guardados.txt", "r") as archivo:
            datos = archivo.readlines()
        ventana_mostrar = tk.Toplevel(ventana)
        ventana_mostrar.title("Lista de Datos Guardados")
        ventana_mostrar.configure(bg="#ffc0cb") 
        for linea in datos:
            tk.Label(ventana_mostrar, text=linea.strip(), bg="#ffc0cb").pack()
    except FileNotFoundError:
        ventana_mostrar = tk.Toplevel(ventana)
        ventana_mostrar.title("Lista de Datos Guardados")
        ventana_mostrar.configure(bg="#ffc0cb")
        tk.Label(ventana_mostrar, text="No hay datos guardados.", bg="#ffc0cb").pack()

def reiniciar_datos():
    with open("datos_guardados.txt", "w") as archivo:
        archivo.write("") 
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Guardar Nombre y Edad")
ventana.configure(bg="#ffc0cb") 

tk.Label(ventana, text="Nombre:", bg="#ffc0cb").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Edad:", bg="#ffc0cb").grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.grid(row=2, column=0, columnspan=2, pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar Lista Final", command=mostrar_datos)
boton_mostrar.grid(row=3, column=0, columnspan=2, pady=5)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar_datos)
boton_reiniciar.grid(row=4, column=0, columnspan=2, pady=5)

ventana.mainloop()
