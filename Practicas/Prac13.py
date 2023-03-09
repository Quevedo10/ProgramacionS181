from tkinter import *
from generador import *
import string
import random

root=Tk()
root.title("Generador de Contraseñas")
root.geometry("300x400")
root.config(bg='black')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Generador de Contraseña',font=('times new roman',20,'bold'),bg='black',fg='white')
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text='Débil',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Media',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Fuerte',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Longitd Contraseña',font=Font,bg='black',fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

if random.choice.get()==1:
            passwordField.insert(0,random.sample(small_alphabets,password_length))

if random.choice.get()==2:
            passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

if random.choice.get()==3:
            passwordField.insert(0,random.sample(all,password_length))

generateButton=Button(root,text='Generar',font=Font,command=gen)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

root.mainloop()
