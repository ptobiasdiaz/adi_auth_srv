"""Authentication Service: entry points."""

from authsrv.service import ServiceMock as Service
from authsrv.blueprint import ApiMock as Api

from flask import Flask


def run_server():
    """Instance flask app and run it."""
    app = Flask(__name__, instance_relative_config=True)
    app.config['service'] = Service()
    app.register_blueprint(Api)
    return app.run(host='0.0.0.0', port=3001, debug=True)
