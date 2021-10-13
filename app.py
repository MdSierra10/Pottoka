#from flask import Flask
#from formularios.fomularios import Login, Register
#aqui se instancian las librerias

#se hacen las rutas
@app.route("/")
@app.route("/login/")
def Login():
    return "Pagina De LOgin"
@app.route("/registro/")
def Registro():
    return "pagina de registro"
@app.route("/home/")
def inicio():
    return "Pagina Feed"
@app.route("/home/perfil/")
def Perfil():
    return "Pagina Perfil"
@app.route("/home/admin/")
def inicio():
    return "Pagina Admin"





