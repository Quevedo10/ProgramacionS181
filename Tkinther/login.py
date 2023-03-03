
from PracticaLogin import *

def validar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    # Aquí iría la validación del usuario y contraseña
    
    if usuario == 'upq.com' and contraseña == 'upq123':
        label_resultado.config(text="¡Bienvenido!")
    else:
        label_resultado.config(text="Por favor, revise sus datos")

