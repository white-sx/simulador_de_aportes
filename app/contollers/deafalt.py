
from flask import render_template, request
from app import app
from app.models.api import calculate_atives, portifolio


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/index', methods=['POST'])
def index():
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
@app.route("/", methods=['POST'])
def calculate():
    print(request.form)
    list_avtives =  request.form.getlist('ativos')
    result = calculate_atives(portifolio)
    formresult = str(result)
    print(formresult)
    return render_template("index.html", result=result)
   
   
