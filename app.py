import os
from flask import Flask, send_from_directory

from routes.lowongan_kerja import lowongan_kerja_blueprint
from routes.personalisasi_karier import personalisasi_karier_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

app.register_blueprint(lowongan_kerja_blueprint)
app.register_blueprint(personalisasi_karier_blueprint)

@app.route('/public/<path:path>/', methods=['GET'])
def static_files(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
    