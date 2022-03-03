"""

"""
from flask import Blueprint, render_template, current_app
from .utils import (
    route_wrapper,
    route_wrapper_partial_errors
)
import random
import datetime

table_routes_bp = Blueprint(
    'table_routes_bp',
    __name__,
    template_folder='templates'
)


@table_routes_bp.route('/table')
@route_wrapper
def table():
    current_app.logger.info('table')

    return render_template('table/table.html')


@table_routes_bp.route('/table/contents')
@route_wrapper_partial_errors
def table_contents():
    rows = []

    for _ in range(100):
        rows.append(
            {
                'title': random.choice(['Blazers', 'Lasers', 'Memo', 'Utopian']),
                'date': random.choice([
                    datetime.datetime.now(),
                    datetime.datetime(2020, 1, 1, 10, 5),
                    datetime.datetime(1999, 5, 6, 5, 14)
                ]).strftime('%-m/%-d/%y %-I:%M %p'),
                'comment': random.choice('abcdefghi') * 50,
                'count': random.choice(range(100))
            }
        )

    return render_template(
        'table/_table.html',
        rows=rows
    )

