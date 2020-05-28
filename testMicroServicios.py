# coding: utf-8
import xlsxwriter
from flask import Flask
app = Flask(__name__)

@app.route('/hola')
def hello_world():
	f = open('EB.CONTRACT.BALANCES20200430.txt', 'r')
    return 'Hello, World!'