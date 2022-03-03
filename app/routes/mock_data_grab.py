"""

"""
from flask import Blueprint, render_template, current_app, request
from .utils import (
    route_wrapper,
    route_wrapper_partial_errors
)
import requests

mock_data_grab_routes_bp = Blueprint(
    'mock_data_grab_routes_bp',
    __name__,
    template_folder='templates'
)


@mock_data_grab_routes_bp.route('/mock-data-grab')
@route_wrapper
def mock_data_grab():
    current_app.logger.info('mock-data-grab')

    return render_template('mock_data_grab/grab.html')


@mock_data_grab_routes_bp.route('/mock-data-grab/contents')
@route_wrapper_partial_errors
def mock_data_grab_contents():
    return render_template('blank.html')


@mock_data_grab_routes_bp.route('/mock-data-grab/send', methods=['POST'])
@route_wrapper_partial_errors
def mock_data_grab_send():
    item = request.form['item'].upper()

    response = requests.get(f'https://jsonplaceholder.typicode.com/{item}')

    return render_template(
        'mock_data_grab/_grab.html',
        response=response.json()
    )
