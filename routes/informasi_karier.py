from flask import Blueprint, redirect, render_template, request
import requests

informasi_karier_blueprint = Blueprint('informasi_karier', __name__, url_prefix='/informasi-karier')

@informasi_karier_blueprint.route('/', methods=['GET'])
def list_informasi_karier():
    # Fetch the list of tasks from the Django backend API
    url_user = 'https://karirku-backend.meervix.com/user/'
    cookies = {'Authorization': 'Bearer ' + request.cookies.get('access_token')}
    user_response = requests.get(url_user, headers=cookies)
    user = user_response.json()

    url_list_karier = 'https://karirku-backend.meervix.com/informasi-karier/all/'
    karier_response = requests.get(url_list_karier)
    kariers = karier_response.json() if karier_response.ok else []

    context = {
        'user': user,
        'kariers': kariers
    }

    return render_template('informasi_karier_list.html', kariers=kariers, user=user)

@informasi_karier_blueprint.route('/new', methods=['GET'])
def add_informasi_karier():
    return render_template('informasi_karier_new.html')

@informasi_karier_blueprint.route('/edit/<string:informasi_karier_id>', methods=['GET'])
def informasi_karier_edit(informasi_karier_id):
    return render_template('informasi_karier_edit.html', informasi_karier_id=informasi_karier_id)