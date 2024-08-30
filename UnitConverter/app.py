from flask import Flask, request
from flask import render_template
from dotenv import load_dotenv
from converter import Converter


load_dotenv("config.env")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('length.html')


@app.route("/length", methods=['POST', 'GET'])
def length():
    
    if request.method == 'POST':
        unit = request.form["unit"]
        unit_from = request.form["unit-from"]
        unit_to = request.form["unit-to"]
        return render_template('result.html', context={"result": Converter.length(unit, unit_from, unit_to)})       
    else:
        return render_template('length.html', context={"lengths": Converter.get_lengths()})
    

@app.route("/temperature" , methods=['POST', 'GET'])
def temperature():
    if request.method == 'POST':
        unit = request.form["unit"]
        unit_from = request.form["unit-from"]
        unit_to = request.form["unit-to"]
        return render_template('result.html', context={"result": Converter.temperature(unit, unit_from, unit_to)})
    else:
        return render_template('temperature.html', context={"temperature": Converter.get_temperatures()})
    

@app.route("/weight" , methods=['POST', 'GET'])
def weight():
    if request.method == 'POST':
        unit = request.form["unit"]
        unit_from = request.form["unit-from"]
        unit_to = request.form["unit-to"]
        return render_template('result.html', context={"result": Converter.weight(unit, unit_from, unit_to)})
    else:
        return render_template('weight.html', context={"weight": Converter.get_weights()})


if __name__ == '__main__':
    app.run()