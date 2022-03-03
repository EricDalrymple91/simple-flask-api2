import os
import time

WTF_CSRF_ENABLED = True
SECRET_KEY = 'simpleflaskapp2022'

VERSION = '1.0'  # Also in setup.py, utils.py:save_session_items

ENVIRONMENT = os.getenv('ENVIRONMENT', 'PROD')

FIRST_NAME = os.getenv('FIRST_NAME')

JSONIFY_PRETTYPRINT_REGULAR = True

CORS_HEADERS = 'Content-Type'

SESSION_TYPE = 'filesystem'

SESSION_PERMANENT = False

# SESSION_PERMANENT = True

# PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)

SESSION_FILE_THRESHOLD = 100

SEND_FILE_MAX_AGE_DEFAULT = 0

TEMPLATES_AUTO_RELOAD = True

SESSION_COOKIE_SAMESITE = "None"

# SESSION_COOKIE_SECURE = True

SERVER_TZ = time.tzname[time.daylight]
