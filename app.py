import os
from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

from routes.lowongan_kerja import lowongan_kerja_blueprint
from routes.informasi_karier import informasi_karier_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

app.register_blueprint(lowongan_kerja_blueprint)
app.register_blueprint(informasi_karier_blueprint)

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
    # Example user data - in a real app, this would come from a database or other data source
    user_info = {
        "username": "JohnDoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "phone_number": "123-456-7890",
        "profile_pic_url": "https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg",
        "education": "Bachelor's in Computer Science",
        "experience": "5 years in software development"
    }
    return render_template('profile.html', user=user_info)

if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)

    