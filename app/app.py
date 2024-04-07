from flask import Flask, request, render_template
from grade import grade

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
	data = request.form['data']
	rtn_data = grade(data)
	return render_template('check.html', rtn_data=rtn_data)

if __name__ == '__main__':
	app.run(debug=True)