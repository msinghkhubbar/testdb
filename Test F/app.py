from flask import Flask, render_template,url_for,flash, redirect
from test import *

app = Flask(__name__)


@app.route("/")
def home():
	data = select_col()
	data1 = ['mandeep','loves','jojo','a lot']
	return render_template('index.html', data=data, data1= data1, data2="what the fuck")

if __name__=='__main__':
	app.run(debug=True)
