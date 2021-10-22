import sqlite3
import hashlib
import os 
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template
from werkzeug.wrappers import CommonRequestDescriptorsMixin
from formularios.formularios import Login, Register

#aqui se instancian las librerias
#cambio de nombre de archivo a formularios.py
#se instancia un objeto de flask para crear las rutas
app=Flask(__name__)
app.secret_key = os.urandom(20)
#se hacen las rutas y se colocan los metodosr

@app.route("/home/", methods=["GET","POST"])
def home():
    return render_template("base.html")
@app.route("/home/configuracion/", methods=["GET","POST"])
def Config():
    return "Pagina de configuracion"
@app.route("/home/perfil/", methods=["GET","POST"])
def Perfil():
    return "Pagina Perfil"

@app.route("/")
@app.route("/login/", methods=["GET", "POST"])
def loguearse():
    frm = Login()
    if frm.validate_on_submit():
        email = frm.email.data
        password = frm.password.data
        #Aqui se aplica el hash para cifrar la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        with sqlite3.connect("pottoka.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT email = ?, password = ? FROM user ", [email, pass_enc])
        if cursor.fetchone():
            return render_template("base.html")
        else:
            return "PASSWORD/CORREO ERRADOS"
    return render_template("login.html", frm = frm)







@app.route("/registro/" , methods=["GET", "POST"])
def Registro():
    frm = Register()
    if frm.validate_on_submit():
        name = frm.name.data
        email = frm.email.data
        password = frm.password.data
        telefono = frm.telefono.data
        username = frm.username.data
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()
        
        #conexion a base de datos de registro
        with sqlite3.connect("pottoka.db") as con:
            cursor = con.cursor()#para manipular la base de datos
            cursor.execute("INSERT INTO user (name, email, password, telefono, username) VALUES (?,?,?,?,?)", 
            [name, email, password, telefono, username ])
        con.commit()
    return render_template("registro.html", frm = frm )

@app.route("/home/admin/", methods=["GET", "POST"])
def dashboard():
    return "Pagina Admin"






@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404

if __name__ == '__main__':
   	app.run()
