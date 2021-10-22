#tenemos que descargar todas las librerias
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired
#cambio de nombre
class Login(FlaskForm):#recibe el formulario
    email  = StringField("Email", validators=[DataRequired("Correo es Obligatorio")], 
    render_kw={"placeholder": "Email"})

    contraseña = PasswordField("Contraseña", validators=[DataRequired("Password es obligatorio")],
    render_kw={"placeholder": "Password"})

    inicio = SubmitField("Iniciar Sesion", render_kw={"placeholder": "Iniciar sesión"})
     

class Register(FlaskForm):
    #todo lo que lleva registro
    nombre = StringField("Nombre", render_kw={"placeholder": "Nombre"})
    correo = StringField("Correo", render_kw={"placeholder": "Correo"})
    contraseña = PasswordField("Contraseña", render_kw={"placeholder": "Contraseña"})
    telefono = StringField("Celular", render_kw={"placeholder": "Telefono"})
    registrar = SubmitField("Registrar")
    usuario = StringField("Usuario", render_kw={"placeholder": "Usuario"})