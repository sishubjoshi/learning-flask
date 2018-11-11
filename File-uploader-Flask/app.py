from flask import Flask, render_template, request
import os
app = Flask(__name__, static_folder='images')
BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(BASE_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    print('tjos is shit!!!')
    print(request.files.getlist('file'))
    print('yypypypypypyypypypyp')
    for file in request.files.getlist('file'):
        print(file)
        fileName = file.filename
        destination = "/".join([target, fileName])
        print(destination)
        file.save(destination)
        print(fileName)
    return render_template('congo.html', img=fileName)


if __name__ == "__main__":
    app.run(debug=True)