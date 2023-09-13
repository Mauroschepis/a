import tkinter as tk
def convertir_temp():
    celcius=float(entry_celsius.get)
    fahrenheit=celcis *9/5 + 32
    label_resultado.config(tet=f"la temperatura e grados fahrenheit es :{fahrenheit:.2f}")
    
    ventana=tk.tk()
    ventana.title("conversor de tempratura")
    label_instrucciones=tk.label(ventana, text="ingrese la tempartura en grados celcsius")
    label_instrucciones.pack()
    entry_celsius=tk.entry(ventana)
    entry_celsius.pack()
    boton_convertir = tk.button(ventana, text="convertir", command=convertir_temp)
    boton_convertir.pack()
    label_resutaldo=tk.label (ventana, text="")
    label_resutaldo.pack
    ventana.mainloop()