from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return "!!!Hola Mundo!!!!!-Otra cosa"

@app.route("/hola")
def hola():
    return "<h1>Saludo desde Hola</h1>"

@app.route("/nueva")
def nueva():
    return "<h1>Saludo desde Nueva</h1>"

if __name__=="__main__":
    app.run(debug=True)