import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


APP_PORT = int(os.environ.get('PORT', 5000))
APP_HOST = os.environ.get(
    key='APP_HOST',
    default='https://define.me/'
)
TELEGRAM_TOKEN = os.environ.get(
    key='5711490877:AAHCU5uKeFXREXZrFCZlNsUX_5UVBBH1XTQ',
    default='5711490877:AAHCU5uKeFXREXZrFCZlNsUX_5UVBBH1XTQ'
)

DATABASE_URL = os.environ.get(
    key='DATABASE_URL',
    default='DB_URL'
)

JOB_INTERVAL = 60  # seconds


LOCAL_SETTINGS = os.path.join(PROJECT_ROOT, "local_settings.py")
if os.path.exists(LOCAL_SETTINGS):
    with open(LOCAL_SETTINGS) as f:
        local_settings_content = f.read()

    local_settings = {}
    exec(compile(local_settings_content, LOCAL_SETTINGS, "exec"), local_settings)

    for key, value in local_settings.items():
        globals()[key] = value

