from flask import Blueprint, redirect, render_template

cerita_alumni_blueprint = Blueprint('cerita_alumni', __name__, url_prefix='/cerita-alumni')

@cerita_alumni_blueprint.route('/', methods=['GET'])
def cerita_alumni_index():
    return 'The project page'
