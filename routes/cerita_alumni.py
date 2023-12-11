from flask import Blueprint, redirect, render_template, request
import requests

API_URL = "https://karirku-backend.meervix.com"
# API_URL = "http://127.0.0.1:8000"

cerita_alumni_blueprint = Blueprint('cerita_alumni', __name__, url_prefix='/cerita-alumni')

# Halaman home dari cerita alumni
@cerita_alumni_blueprint.route('/', methods=['GET'])
def cerita_alumni_index():
    all_cerita_alumni = requests.get(f'{API_URL}/cerita-alumni/all/')

    # Jika user login
    try:
        header = {
            'Authorization': f'Bearer {request.cookies.get("access_token")}'
        }

        user_info = requests.get(f'{API_URL}/user/', headers=header)
        
        from_user = []
        from_other = []

        for i in all_cerita_alumni.json():
            if user_info.json()['id'] == i['alumni']:
                from_user.append(i)
            else:
                from_other.append(i)

        data = {
            "from_user" : from_user,
            "from_other" : from_other
        }

        # print(user_info)

        return render_template('cerita_alumni/cerita_alumni_home.html', value=data, user=user_info.json())
    
    # Jika tidak login
    except:
        from_user = []
        from_other = all_cerita_alumni.json()

        data = {
            "from_user" : from_user,
            "from_other" : from_other
        }

        return render_template('cerita_alumni/cerita_alumni_home.html', value=data, user=None)

# Halaman detail cerita alumni
@cerita_alumni_blueprint.route('/detail/<path>/', methods=['GET'])
def cerita_alumni_detail(path):
    pesan = request.data
    try:

        # Getting info about cerita alumni
        get_cerita_alumni = requests.get(f'{API_URL}/cerita-alumni/detail/{path}/')

        if (get_cerita_alumni.status_code >= 400):
            return render_template('cerita_alumni/cerita_alumni_error.html')
        else:
            return render_template('cerita_alumni/cerita_alumni_detail.html', data=get_cerita_alumni.json(), pesan=pesan)
    except:
        return render_template('cerita_alumni/cerita_alumni_error.html')

# Halaman buat cerita alumni baru
@cerita_alumni_blueprint.route('/new/', methods=['GET'])
def cerita_alumni_new():
    try:

        # Getting info about user
        name = request.cookies.get('access_token')
        user_info = requests.get(f'{API_URL}/user/', headers={'Authorization': f"Bearer {name}"})

        if (user_info.json()['user_type'] != "alumni"):
            return render_template('cerita_alumni/cerita_alumni_error.html')
        else:
            return render_template('cerita_alumni/cerita_alumni_form.html', data=None, check=True)
    except:
        return render_template('cerita_alumni/cerita_alumni_error.html')

# Halaman sunting cerita alumni
@cerita_alumni_blueprint.route('/edit/<path>/', methods=['GET'])
def cerita_alumni_edit(path):
    try:
        name = request.cookies.get('access_token')

        # Getting information about user and ceritaAlumni
        user_info = requests.get(f'{API_URL}/user/', headers={'Authorization': f"Bearer {name}"})
        get_cerita_alumni = requests.get(f'{API_URL}/cerita-alumni/detail/{path}/')

        if (get_cerita_alumni.status_code >= 400):
            return render_template('cerita_alumni/cerita_alumni_error.html')
        elif (user_info.json()['id'] != get_cerita_alumni.json()['alumni']):
            return render_template('cerita_alumni/cerita_alumni_error.html')
        else:
            return render_template('cerita_alumni/cerita_alumni_form.html', data=get_cerita_alumni.json(), check=False)
    except:
        return render_template('cerita_alumni/cerita_alumni_error.html')

# tes
@cerita_alumni_blueprint.route('/test/', methods=['GET'])
def tes():
    return render_template('cerita_alumni/test.html')