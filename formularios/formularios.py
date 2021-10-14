#tenemos que descargar todas las librerias
from flask_wtf import FlaskForm
from wtforms import   SubmitField
#from wtforms.validators import DataRequired, NumberRange
#cambio de nombre
class Login():#recibe el formulario
    contra = ()
    email = ()
    inicio = SubmitField("Iniciar Sesion")

class Register():
    #todo lo que lleva registro
    nombre = ""#se instancian las cualidades de cada Field
    apellidos = ""
    telefono = ""
    registro = SubmitField("Registrarse")