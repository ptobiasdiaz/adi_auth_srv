"""Authentication Service: blue print of the API."""
from flask import Blueprint, current_app, Response

ApiMock = Blueprint('authorization_service', __name__)
API_ROOT = '/api/v1'


@ApiMock.route(f'{API_ROOT}/alive', methods=('GET',))
def live_probe() -> Response:
    """Use to make probes."""
    return Response('', status=204)

@ApiMock.route(f'{API_ROOT}/is_authorized/<auth_code>', methods=('GET',))
def is_authorized(auth_code: str) -> Response:
    """Check auth_code."""
    return Response('', status=204) if current_app.config['service'].is_authorized(auth_code) else Response('Not found', status=404)
