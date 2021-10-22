#tenemos que descargar todas las librerias
from flask_wtf import FlaskForm
import flask_wtf
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired
#cambio de nombre
class Login(FlaskForm):#recibe el formulario
    email  = StringField("Email", validators=[DataRequired("Correo es Obligatorio")], 
    render_kw={"placeholder": "Email"})

    password = PasswordField("password", validators=[DataRequired("Password es obligatorio")],
    render_kw={"placeholder": "Password"})

    inicio = SubmitField("Iniciar Sesion", render_kw={"placeholder": "Iniciar sesión"})
     

class Register(FlaskForm):
    #todo lo que lleva registro
    name = StringField("Nombre", render_kw={"placeholder": "Nombre"})
    email = StringField("Correo", render_kw={"placeholder": "Correo"})
    password = PasswordField("password", render_kw={"placeholder": "Contraseña"})
    telefono = StringField("Celular", render_kw={"placeholder": "Telefono"})
    registrar = SubmitField("Registrar")
    username = StringField("Usuario", render_kw={"placeholder": "Usuario"})

class Perfil(FlaskForm):

    #Para editar el perfil
    genero = StringField("Genero")
    bio = StringField("Biografia de perfil")
    image_header = StringField("Imagen")
    #Para hacer actualizacion en el email o correo
    email = StringField("Email")
    #editar numero de telefono
    telefono = StringField("Telefono")

class Post(FlaskForm):
    contenido = StringField("Imagen")
    imagen = StringField("Imagen")

class Comment(FlaskForm):
    comentario = StringField("Comentario")

#class admin(FlaskForm): Aqui se determinan los permisos
