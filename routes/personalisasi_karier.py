from flask import Blueprint, redirect, render_template

personalisasi_karier_blueprint = Blueprint('personalisasi_karier', __name__, url_prefix='/personalisasi-karier')

@personalisasi_karier_blueprint.route('/', methods=['GET'])
def personalisasi_karier_index():
    return render_template('personalisasi_karier.html')

@personalisasi_karier_blueprint.route('/kuis', methods=['GET'])
def kuis_index():
    return render_template('kuis.html')

