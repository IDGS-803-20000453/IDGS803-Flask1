from flask import Flask
from flask import request
#instancia al nombre del proyecto , despues levantamos el servidor
app= Flask(__name__)

#todo decorador lleva associado un metodo y un return
@app.route("/operasBas",methods=["GET","POST"])
def operasBas():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        op=request.form.get("op")

        if(op=="suma"):
         return "las suma es: {}".format(str(int(num1)+int(num2)))
        if(op=="resta"):
         return "la resta es: {}".format(str(int(num1)-int(num2)))
        if(op=="multiplicacion"):
         return "la multiplicacion es: {}".format(str(int(num1)*int(num2)))
       
       

    else:
        return '''
        <form action="/operasBas" method="POST">
        <label> N1: </label>
        <input type="text" name="num1" /> </br>
        <label> N2: </label>
        <input type="text" name="num2" /> </br>
        
        

    <div>
      <input type="radio" id="suma" name="op" value="suma">
      <label >Suma</label>
    </div>

    <div>
      <input type="radio" id="dewey" name="op" value="resta">
      <label >Resta</label>
    </div>

    <div>
      <input type="radio" id="louie" name="op" value="multiplicacion">
      <label >Multiplicacion</label>
    </div>



        <input type="submit" value="calcular" /> </br>
        </form>

        
        '''

if __name__=="__main__":
    app.run(debug=True)