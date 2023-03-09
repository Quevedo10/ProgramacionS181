
class Usuario:
     def _init_(self, email, password):
         self.email = email
         self.password = password

def login(email_input, password_input):
     usuario = Usuario("antoniogtzv", "jano")
     if email_input == usuario.email and password_input == usuario.password:
         mensaje = "¡Inicio de sesión exitoso!"
         exitoso = True
     else:
         mensaje = "Correo o contraseña incorrectos. Intente nuevamente."
         exitoso = False
     return mensaje, exitoso

