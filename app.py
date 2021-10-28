import sqlite3
import hashlib
import os 
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, session, url_for
from werkzeug.wrappers import CommonRequestDescriptorsMixin, request
from werkzeug.utils import redirect
from formularios.formularios import Login, Register, UploadForm
from datetime import date
from datetime import datetime
from werkzeug.utils import secure_filename


#aqui se instancian las librerias
#cambio de nombre de archivo a formularios.py
#se instancia un objeto de flask para crear las rutas
app=Flask(__name__)
app.secret_key = os.urandom(20)

usu=''
#se hacen las rutas y se colocan los metodosr

@app.route("/home/configuracion/", methods=["GET","POST"])
def Config():
    return "Pagina de configuracion"


@app.route("/")
def dirigir():
    return redirect("/login/")


@app.route("/login/", methods=["GET", "POST"])
def loguearse():
    frm = Login()
    if frm.validate_on_submit():
        session["username"] = frm.username.data
        username = frm.username.data
        password = frm.password.data
        #Aqui se aplica el hash para cifrar la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        with sqlite3.connect("/home/oscarmena/mysite/pottoka.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT username FROM login WHERE username = ? AND password = ? ", [username, pass_enc])
            if cursor.fetchone():
                return redirect("/home/")
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
        with sqlite3.connect("/home/oscarmena/mysite/pottoka.db") as con:
            now = datetime.now()
            fecha = str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" - "+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
            cursor = con.cursor() #para manipular la base de datos
            cursor.execute("INSERT INTO login VALUES (?,?,?,?,?,?,?)", [username, name, email, pass_enc, telefono, fecha, 0])
            con.commit()
            return redirect("/login/")

    return render_template("registro.html", frm = frm )
    

@app.route("/home/admin/", methods=["GET", "POST"])
def dashboard():
    return "Pagina Admin"


@app.route("/home/", methods=["GET", "POST"])
def home():

    with sqlite3.connect("/home/oscarmena/mysite/pottoka.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("SELECT * FROM login")
        rows = cursor.fetchall()
        cursor.execute("SELECT * FROM comentarios")
        rows2 = cursor.fetchall()
        return render_template("home.html", rows = rows, rows2 = rows2)


@app.route("/subir/", methods=["GET", "POST"])
def subir():
    form = UploadForm()  # carga request.from y request.file
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        img = "assets/" + filename
        titulo = form.titulo.data
        comentario = form.comentario.data
        f.save(app.root_path + "/static/assets/" + filename)

        with sqlite3.connect("/home/oscarmena/mysite/pottoka.db") as con:
            now = datetime.now()
            fecha = str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" - "+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
            username = session["username"]
            usu=username
            cursor = con.cursor() #para manipular la base de datos
            cursor.execute("INSERT INTO comentarios VALUES (?,?,?,?,?)", [username, comentario, fecha, img, titulo])
            con.commit()
            rows = cursor.fetchall()
            return redirect("/perfil/")

    return render_template('subir.html', form=form)

@app.route("/perfil/", methods=["GET", "POST"])
@app.route("/perfil/<usu>", methods=["GET", "POST"])
def perfil(usu = None):
    with sqlite3.connect("/home/oscarmena/mysite/pottoka.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("SELECT * FROM comentarios")
        rows = cursor.fetchall()
        if (usu == None):
            usu = session["username"]
        return render_template("perfil.html", rows = rows, usu = usu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html")

