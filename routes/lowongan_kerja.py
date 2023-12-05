from flask import Blueprint, redirect, render_template

lowongan_kerja_blueprint = Blueprint('lowongan_kerja', __name__, url_prefix='/lowongan-kerja')

@lowongan_kerja_blueprint.route('/', methods=['GET'])
def lowongan_kerja_index():
    return render_template('lowongan_kerja_list.html')
