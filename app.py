import os
from flask import Flask, send_from_directory

from routes.lowongan_kerja import lowongan_kerja_blueprint
from routes.cerita_alumni import cerita_alumni_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

app.register_blueprint(lowongan_kerja_blueprint)
app.register_blueprint(cerita_alumni_blueprint)

@app.route('/public/<path:path>/', methods=['GET'])
def static_files(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
    