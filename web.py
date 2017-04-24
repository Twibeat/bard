# _*_ coding: utf-8 _*_ 
from flask import Flask, render_template, redirect, request, send_file
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['mid','midi'])
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

def run(input_dir, output_dir, iteration):
    pass

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)#파일이 없다는걸 알려야 할 듯
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            target = os.path.join(APP_ROOT, 'input_files/')
            if not os.path.isdir(target):
                os.mkdir(target)
            filename = secure_filename(file.filename)
            file.save(os.path.join("/".join([target, filename])))
            return 'good!'
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/input_files/<filename>', methods=['GET'])
def input_files(filename):
    target = os.path.join(APP_ROOT, 'input_files')
    file = os.path.join("/".join([target, filename]))
    return send_file(file)

app.run()
