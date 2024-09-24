import tkinter as tk

ventana = tk.Tk() # La segunda t va en mayúscula.

ventana.title("Mi primer ventana")
ventana.geometry("600x400+500+200") # ancho x alto, en string. x 500 + y200
ventana.minsize(width=400, height=200) # ancho x alto minimo
ventana.maxsize(width=800, height=600) # ancho x alto maximo
ventana.iconbitmap("gato.ico")
ventana.configure(bg="lightgrey")
ventana.resizable(False,False) # horizontal y vertical


ventana.mainloop()
