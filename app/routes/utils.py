"""

"""
import os
from flask import current_app, render_template, request, session
from functools import wraps


def save_session_items():
    session['version'] = '1.0'  # Also in config.py, setup.py

    if 'first_name' not in session:
        first_name = os.getenv('FIRST_NAME', 'Test')
        last_name = os.getenv('LAST_NAME', 'Bot')
        session['first_name'] = first_name
        session['last_name'] = last_name

    return f'{session["first_name"]} {session["last_name"]}'


def route_wrapper(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        try:
            user = save_session_items()
            current_app.logger.info(f'{request.method} - {request.url} - {user}')

            return orig_func(*args, **kwargs)
        except Exception as error:
            error_msg = f'{type(error).__name__}: {error}'
            current_app.logger.error(f'{error_msg}')
            current_app.logger.exception(error)

            return render_template(
                'errors/500.html',
                error=error_msg
            )

    return wrapper


def route_wrapper_partial_errors(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        try:
            user = save_session_items()
            current_app.logger.info(f'{request.method} - {request.url} - {user}')

            return orig_func(*args, **kwargs)
        except Exception as error:
            error_msg = f'{type(error).__name__}: {error}'
            current_app.logger.error(f'{error_msg}')
            current_app.logger.exception(error)

            return render_template(
                'errors/_500.html',
                error=error_msg
            )

    return wrapper
