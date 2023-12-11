from flask import Blueprint, redirect, render_template, request
import requests

informasi_karier_blueprint = Blueprint('informasi_karier', __name__, url_prefix='/informasi-karier')

@informasi_karier_blueprint.route('/', methods=['GET'])
def list_informasi_karier():
    # Fetch the list of tasks from the Django backend API
    url = 'https://karirku-backend.meervix.com/informasi-karier/all/'
    response = requests.get(url)
    kariers = response.json() if response.ok else []
    return render_template('informasi_karier_list.html', kariers=kariers)

@informasi_karier_blueprint.route('/new', methods=['GET'])
def add_informasi_karier():
    return render_template('informasi_karier_new.html')