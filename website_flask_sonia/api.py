from flask import Flask, render_template, request

app = Flask (__name__, template_folder="./scr/views")

@app.route("/", methods=["GET", "POST"])
def home():
    
    if(request.method == "GET"):
      return render_template("index.html")
    else:
      if (request.form["num1"] !="" and request.form["num2"] !=""):
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        
        if (request.form["opc"] == "soma"):
          soma = int(num1) + int(num2)
          return str(soma)

        elif (request.form["opc"] == "subt"):
          subt = int(num1) - int(num2)
          return str(subt)
        
        elif (request.form["opc"] == "mult"):
          mult = int(num1) * int(num2)
          return str(mult)

        else:
          divi = int(num1) // int(num2)
          return str(divi)
            
      else:
        return "Informe um valor Válido, Por favor insira os dois valores solicitados para calcular"
        
    #  return request.form["num1"] vai testar se o m[etodo POST está retornando corretamente 
    # return "Você está acessando via outro Verbo/método"
    # essa forma elimina necessidade de criar mais páginas html de erro

    #projeto feito de acordo com a monitoria do dia 28/01/2020 , monitor José Alisson. #Gratidão
    #Sonia Borges


@app.errorhandler(404)
def FileNotFoundError(error):
    return render_template("error.html")


app.run(port=5000, debug=True)