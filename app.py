import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, make_response

from routes.lowongan_kerja import lowongan_kerja_blueprint
from routes.informasi_karier import informasi_karier_blueprint
from routes.personalisasi_karier import personalisasi_karier_blueprint
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

app.register_blueprint(lowongan_kerja_blueprint)
app.register_blueprint(informasi_karier_blueprint)
app.register_blueprint(personalisasi_karier_blueprint)

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

@app.route('/profile')
def profile():
    access_token = request.cookies.get('access_token')

    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get('https://karirku-backend.meervix.com/user/', headers=headers)

        if response.status_code == 200:
            user_info = response.json()
            return render_template('profile.html', user=user_info)
        else:
            return redirect('/logout')
    else:
        return "Access token not found", 401

@app.route('/edit-profile')
def edit_profile():
    access_token = request.cookies.get('access_token')

    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get('https://karirku-backend.meervix.com/user/', headers=headers)

        if response.status_code == 200:
            user_info = response.json()
            return render_template('edit-profile.html', user=user_info)
        else:
            return redirect('/logout')
    else:
        return "Access token not found", 401
    
@app.route('/logout')
def logout():
    response = make_response(redirect('/'))

    response.set_cookie('access_token', '', expires=0)
    response.set_cookie('refresh_token', '', expires=0)

    return response

if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)

    