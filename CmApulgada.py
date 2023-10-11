import tkinter as tk
def convertir_distancia():
    try:
        centimetro = float(entry_centimetro.get())
        pulgada = centimetro / 2.54
    
        label_resultado.config(text=f"El cambio de centimetros a pulgadas  es : {pulgada:.2f}")
    except ValueError:
        label_resultado.config(text=f"Pone bien los numeros pibe")
# Crear la ventana
ventana = tk.Tk()
ventana.title("Conversor de distancia")

# Crear y ubicar los elementos en la ventana
label_instrucciones = tk.Label(ventana, text="Ingrese la distancia en centimetros:")
label_instrucciones.pack()

entry_centimetro = tk.Entry(ventana)
entry_centimetro.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia,)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciar el bucle principal
ventana.mainloop()