#tenemos que descargar todas las librerias
from flask_wtf import FlaskForm
import flask_wtf
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


#cambio de nombre
class Login(FlaskForm):#recibe el formulario
    username  = StringField("Usuario", validators=[DataRequired("Usuario es Obligatorio")], 
    render_kw={"placeholder": "Usuario"})

    password = PasswordField("password", validators=[DataRequired("Password es obligatorio")],
    render_kw={"placeholder": "Password"})

    inicio = SubmitField("Iniciar Sesion", render_kw={"placeholder": "Iniciar sesión"})
     

class Register(FlaskForm):
    #todo lo que lleva registro
    name = StringField("Nombre", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Nombre"})
    email = StringField("Correo", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Correo"})
    password = PasswordField("password", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Contraseña"})
    telefono = StringField("Celular", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Telefono"})
    username = StringField("Usuario", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Usuario"})
    registrar = SubmitField("Registrar")

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

class UploadForm(FlaskForm):
    titulo = StringField("Titulo", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Titulo"})
    comentario = StringField("Nombre", validators=[DataRequired("Este campo es Obligatorio")], render_kw={"placeholder": "Comentario"})
    photo = FileField('selecciona imagen:', validators=[FileRequired()])
    submit = SubmitField('Subir')

#class admin(FlaskForm): Aqui se determinan los permisos
