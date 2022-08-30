from os import getenv

from main import create_app
from config import config_selector

app = create_app()
configs = config_selector[getenv("FLASK_ENV")]

if __name__ == "__main__":
    app.run(host=configs.FLASK_RUN_HOST, port=configs.FLASK_RUN_PORT, debug=configs.DEBUG)
