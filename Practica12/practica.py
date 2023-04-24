from logica import login
import tkinter as tk

def main():
    ventana = tk.Tk()
    app = login(ventana)
    ventana.mainloop()

if __name__ == '__main__':
    main()
    