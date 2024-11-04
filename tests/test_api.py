"""Authentication Service: test blueprint (use as example)."""

import unittest

from authsrv import command_handlers
from authsrv.service import ADMIN_AUTH_CODE, USER_PASS_CODE


APIROOT = '/api/v1'


class TestServiceMock(unittest.TestCase):
    """Test cases to check the mock."""

    def test_status(self):
        """Test liveness probe."""
        with command_handlers.create_app().test_client() as client:
            response = client.get(f'{APIROOT}/alive')
            self.assertEqual(response.status_code, 204)

    def test_admin_authorized(self):
        """Test admin authorization."""
        with command_handlers.create_app().test_client() as client:
            response = client.get(f'{APIROOT}/is_authorized/{ADMIN_AUTH_CODE}')
            self.assertEqual(response.status_code, 204)

    def test_user_authorized(self):
        """Test user authorization."""
        with command_handlers.create_app().test_client() as client:
            response = client.get(f'{APIROOT}/is_authorized/{USER_PASS_CODE}')
            self.assertEqual(response.status_code, 204)

    def test_other_not_authorized(self):
        """Test other authorization."""
        with command_handlers.create_app().test_client() as client:
            response = client.get(f'{APIROOT}/is_authorized/any_other_value')
            self.assertEqual(response.status_code, 404)
