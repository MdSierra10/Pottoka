from flask import Flask, render_template
from formularios.fomularios import Login, Register
#aqui se instancian las librerias

#se instancia un objeto de flask para crear las rutas
app=Flask(__name__)

#se hacen las rutas y se colocan los metodos
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login/", methods=["GET","POST"])
def Login():
    return render_template("login.html")

@app.route("/registro/" , methods=["GET","POST"])
def Registro():
    return "pagina de registro"

@app.route("/Principal/", methods=["GET"])
def inicio():
    return "Pagina Feed"

@app.route("/perfil/", methods=["GET"])
def Perfil():
    return "Pagina Perfil"

@app.route("/admin/", methods=["POST"])
def dashboard():
    return "Pagina Admin"
@app.route("/admin/estadistic", methods=["POST"])
def dashboardEstadistic():
    return "Pagina Admin"





