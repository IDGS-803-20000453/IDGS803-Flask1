from flask import Flask, request

app = Flask(__name__)

@app.route("/operaciones_basicas", methods=["GET","POST"])
def operaciones_basicas():
    resultado = None
    numero_1=""
    numero_2=""
    if request.method == "POST":
        numero_1 = request.form.get("numero_1")
        numero_2 = request.form.get("numero_2")
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = int(numero_1) + int(numero_2)
        elif operacion == "resta":
            resultado = int(numero_1) - int(numero_2)
        elif operacion == "multiplicacion":
            resultado = int(numero_1) * int(numero_2)
        elif operacion == "division":
            if int(numero_2) != 0:
                resultado = int(numero_1) / int(numero_2)
            else:
                resultado = "No se puede dividir entre cero"
    return '''
    <h1>Operaciones Básicas</h1>
    <form method="post">
        <label> Número 1: </label>
        <input type="text" name="numero_1" value='{}'/> </br>
        <label> Número 2: </label>
        <input type="text" name="numero_2" value='{}'/> </br>
        <div>
            <input type="radio" id="suma" name="operacion" value="suma">
            <label for="suma">Suma</label>
        </div>
        <div>
            <input type="radio" id="resta" name="operacion" value="resta">
            <label for="resta">Resta</label>
        </div>
        <div>
            <input type="radio" id="multiplicacion" name="operacion" value="multiplicacion">
            <label for="multiplicacion">Multiplicación</label>
        </div>
        <div>
            <input type="radio" id="division" name="operacion" value="division">
            <label for="division">División</label>
        </div>
        <input type="submit" value="calcular" />
    </form>
    <br>
    <p>{}</p>
    '''.format(numero_1 or '', numero_2 or '', resultado or '')

if __name__ == "__main__":
    app.run(debug=True)