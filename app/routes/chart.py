"""

"""
from flask import Blueprint, render_template, current_app, request
from .utils import (
    route_wrapper,
    route_wrapper_partial_errors
)
import time

chart_routes_bp = Blueprint(
    'chart_routes_bp',
    __name__,
    template_folder='templates'
)


@chart_routes_bp.route('/chart')
@route_wrapper
def chart():
    current_app.logger.info('chart')

    return render_template('chart/chart.html')


@chart_routes_bp.route('/chart/contents')
@route_wrapper_partial_errors
def chart_contents():
    # Mock some loading time
    time.sleep(1.5)

    # Create chart
    chart_data = {
        'type': 'pie',
        'data': {
            'datasets': [
                {
                    'data': [10, 20, 30, 50],
                    'backgroundColor': ['#9d2933', '#3ab09e', '#ffff66', '#b57edc']
                }
            ],
            'labels': ['A', 'B', 'C', 'D']
        },
        'options': {
            'plugins': {
                'legends': {
                    'display': True,
                    'position': 'bottom',
                    'align': 'bottom',
                    'labels': {
                        'color': 'white',
                        'font': {
                            'size': 16
                        }
                    }
                }
            }
        }
    }

    return render_template(
        'chart/_chart.html',
        chart_data=chart_data
    )
