"""
python app/app.py
http://0.0.0.0:8080/

Colors: https://www.color-hex.com/color-names.html
Icons: https://fontawesome.com/v4.7.0/icons/
"""
from flask import Flask, render_template, session, request, current_app
from flask_assets import Environment, Bundle
from flask_session import Session
from flask_cors import CORS
import logging
import time
from routes.table import table_routes_bp
from routes.mock_data_grab import mock_data_grab_routes_bp
from routes.chart import chart_routes_bp
from routes.utils import save_session_items

app = Flask(__name__)

# Configurations
app.logger.setLevel(logging.INFO)
CORS(app)
app.config.from_object('config')
assets = Environment(app)
Session(app)

# Blueprints
app.register_blueprint(table_routes_bp)
app.register_blueprint(mock_data_grab_routes_bp)
app.register_blueprint(chart_routes_bp)


# CSS
css = Bundle(
    'css/core.css',
    output='gen/packed.css'
)

assets.register('css_all', css)

# JS
js = Bundle(
    'js/core.js',
    output='gen/packed.js'
)

assets.register('js_all', js)


# Home page
@app.route("/")
def homepage():
    save_session_items()

    return render_template('index.html')


# Session debug helpers
@app.route('/session/cookies/jar')
def get_cookies():
    save_session_items()

    current_app.logger.info(request.cookies)
    current_app.logger.info(list(request.headers.items()))

    return render_template(
        'display_message.html',
        title='Cookies Jar',
        message=str(list(request.headers.keys()))
    )


@app.route('/session/clear')
def clear_session():
    session.clear()

    return render_template('clear_session.html')


@app.route('/timezone')
def server_timezone():
    tz = time.tzname

    return render_template(
        'display_message.html',
        title='Server Timezone',
        message=f'{tz} --- UTC? -> {tz[0] == "UTC"}',
    )


# Error routes
@app.errorhandler(404)
def page_not_found(_):
    return render_template('errors/404.html'), 404


@app.route('/errors/500')
def internal_server_error_generic():
    return render_template('errors/500_generic.html'), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080, threaded=True)
