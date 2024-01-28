from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello, World!')

@app.route('/page1')
def date_11():
    return render_template("index.html",message="GGs")

if __name__ == '__main__':
    app.run(debug=True)
