from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        if request.form['username']:
            return render_template('index.html', username=request.form['username'])
        else:
            return render_template('index.html', username='null')
    return render_template('index.html', username='null')

if __name__ == "__main__":
    app.run(debug=True)
