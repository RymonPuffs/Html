from flask import Flask, render_template, request


app = Flask(__name__)


#requests -> peticion
#response -> respuesta
#cliente -> cliente

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html', resultado=None, error=None)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form.get('primer_valor'))
        num2 = float(request.form.get('segundo_valor'))
        resultado = num1 + num2
        return render_template('calculadora.html', resultado=resultado)
    except (TypeError, ValueError):
        return render_template(
            'calculadora.html',
            resultado=None,
            error='Por favor ingresa dos números válidos.'
        )


if __name__ == '__main__':
    app.run(debug=True)