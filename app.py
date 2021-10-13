from flask import Flask, render_template
from formularios.formularios import Login, Register
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

@app.route("/admin/", methods=["POST"])
def dashboard():
    return "Pagina Admin"

@app.route("/admin/estadistic", methods=["POST"])
def dashboardEstadistic():
    return"Nada"

@app.route("/perfil/", methods=["GET"])
def Perfil():
    return "Pagina Perfil"


@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404


if __name__ == '__main__':
   	app.run()
