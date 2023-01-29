from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    nombre = "Zlatan"
    lista1=["Español","Ingles","Quimica"]
    return render_template("index.html",nombre=nombre,lista1=lista1)

@app.route('/usuarios')
def usuario():
    return render_template("archivo2.html")

if __name__=="__main__":
    app.run(debug=True)
