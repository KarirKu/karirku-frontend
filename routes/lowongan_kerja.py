from flask import Blueprint, redirect, render_template

lowongan_kerja_blueprint = Blueprint('lowongan_kerja', __name__, url_prefix='/lowongan-kerja')

@lowongan_kerja_blueprint.route('/', methods=['GET'])
def lowongan_kerja_index():
    return render_template('lowongan_kerja_list.html')

@lowongan_kerja_blueprint.route('/<string:lowongan_kerja_id>', methods=['GET'])
def lowongan_kerja_details(lowongan_kerja_id):
    return render_template('lowongan_kerja_details.html', lowongan_kerja_id=lowongan_kerja_id)
