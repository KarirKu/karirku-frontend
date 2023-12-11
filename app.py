import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

from routes.lowongan_kerja import lowongan_kerja_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

app.register_blueprint(lowongan_kerja_blueprint)

@app.route('/public/<path:path>/', methods=['GET'])
def static_files(path):
    return send_from_directory('public', path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)

    