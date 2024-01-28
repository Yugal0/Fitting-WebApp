from flask import Flask, render_template, request, jsonify
import os
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})

    
    file = request.files["file"]

    if file.filename=="":
        jsonify({'status': 'error', 'message': 'No selected file'})

    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return jsonify({'status': 'success', 'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
