"""Authentication Service: test mock (use as example)."""

import unittest

from authsrv.service import ServiceMock as Service


class TestServiceMock(unittest.TestCase):
    """Test cases to check the mock."""

    def test_owner_of_admin_auth_code(self):
        """Test admin auth_code."""
        self.assertTrue(Service().is_authorized('ba1114fef0780a254623bf0071412db49fdd3b112e4bc65074f5792f3d34da6e'))

    def test_owner_of_user_auth_code(self):
        """Test user auth_code."""
        self.assertTrue(Service().is_authorized('b19437b7a4cfc58b1e5c6e5d21b2f709c953f32cb1989e3c529037fb08bd252c'))

    def test_wrong_auth_token(self):
        """Test wrong auth_code."""
        self.assertFalse(Service().is_authorized('cee8b7eab780747855f971965266f4c1509257e001ff8161fb44578f06578403'))
