from flask import Flask, render_template
from formularios.fomularios import Login, Register

#aqui se instancian las librerias
#cambio de nombre de archivo a formularios.py
#se instancia un objeto de flask para crear las rutas
app=Flask(__name__)
#se hacen las rutas y se colocan los metodos

@app.route("/home/")
def home():
    return render_template("base.html")

@app.route("/")
@app.route("/login/", methods=["GET", "POST"])
def Login():
    return render_template("login.html")

@app.route("/registro/" , methods=["GET", "POST"])
def Registro():
    return render_template("registro.html")

@app.route("/home/admin/", methods=["GET", "POST"])
def dashboard():
    return "Pagina Admin"

@app.route("/home/perfil/", methods=["GET"])
def Perfil():
    return "Pagina Perfil"

@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404

if __name__ == '__main__':
   	app.run()
