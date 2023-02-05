from flask import Flask, render_template, request
class Controlador:
    def __init__(self):
        self.app = Flask(__name__) 
        
        @self.app.route("/cinepolisFlask")
        def multiplicar():
            return render_template("cinepolis.html") 
        
        @self.app.route("/valorPagar", methods=["POST"])
        def resultado():
            canBoletas = int(request.form.get("txtCanBoletas"))
            canComprador = int(request.form.get("txtCanComprador"))
            nombre = request.form.get("txtNombre")
            tarBoletas = request.form.get("rbtnTarBoletas")

            if canComprador > 7:
                return render_template("cinepolis.html", error_message="El número de compradores debe ser menor o igual a 7")

            valorPagar = Calculos.calcular_valor_pagar(canBoletas, tarBoletas)


            return render_template("cinepolisValor.html",nombre=nombre, valorPagar=valorPagar)

    
    def run(self):
        if __name__ == "__main__":
            self.app.run( debug=True)

class Calculos:
    @staticmethod
    def calcular_valor_pagar(canBoletas, tarBoletas):
        valorPagar = 12 * canBoletas
        if (canBoletas > 5):
            valorPagar = (valorPagar - (valorPagar * 0.15))
        elif (3 < canBoletas < 5):
            valorPagar = (valorPagar - (valorPagar * 0.10))
        elif (canBoletas < 3):
            valorPagar = valorPagar
        if (tarBoletas == "si"):
            valorPagar = (valorPagar - (valorPagar * 0.10))
        
        return valorPagar

controlador = Controlador()
controlador.run()
