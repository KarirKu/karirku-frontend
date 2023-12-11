from flask import Blueprint, redirect, render_template, request, url_for
import requests

personalisasi_karier_blueprint = Blueprint('personalisasi_karier', __name__, url_prefix='/personalisasi-karier')

@personalisasi_karier_blueprint.route('/', methods=['GET'])
def personalisasi_karier_index():
    access_token = request.cookies.get('access_token')
    
    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get('https://karirku-backend.meervix.com/user/', headers=headers)
        
        if response.status_code == 200:
            user_info = response.json()
        else:
            return redirect('/logout') 
    return render_template('personalisasi_karier.html', user=user_info)

@personalisasi_karier_blueprint.route('/kuis', methods=['GET'])
def kuis_index():
    return render_template('kuis.html')

@personalisasi_karier_blueprint.route('/kuis', methods=['POST'])
def submit():
    answers = request.form
    
    scores = {
        'Perangkat Lunak': 0,
        'Kecerdasan Artifisial': 0,
        'Projek': 0,
        'UI/UX': 0,
        'Infrastruktur dan Keamanan Siber': 0
    }

    for key, value in answers.items():
        scores[value] += 1

    top_career = max(scores, key=scores.get)
   
    return redirect(url_for('personalisasi_karier.personalisasi_karier_index'))
