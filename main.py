from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def inicio():
    return render_template("index.html")

@app.get("/conctactos")
def listaConctactos():
    return render_template("conctactos.html")

@app.get("/conctactos/<int:conctactosId>")
def editarConctactos(conctactosId):
    return render_template("editarconctactos.html",id=conctactosId)

@app.get("/edad/<int:edadId>")
def edadUsuario(edadId):
    return render_template("edad.html",id=edadId)



app.run(debug=True)
