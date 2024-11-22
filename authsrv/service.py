"""Authentication Service: service (mock)."""

import hashlib


ADMIN_USERNAME = 'administrator'
ADMIN_PASS_HASH = hashlib.sha256('adminpass'.encode()).hexdigest()
ADMIN_AUTH_CODE = hashlib.sha256(f'{ADMIN_USERNAME}{ADMIN_PASS_HASH}'.encode()).hexdigest()
USER_USERNAME = 'user'
USER_PASS_HASH = hashlib.sha256('userpass'.encode()).hexdigest()
USER_PASS_CODE = hashlib.sha256(f'{USER_USERNAME}{USER_PASS_HASH}'.encode()).hexdigest()


class ServiceMock:
    """Mock implementation of the service."""

    def is_authorized(self, auth_code: str) -> bool:
        """Get the owner of a given token."""
        if auth_code == ADMIN_AUTH_CODE:
            return ["admin", "user"]
        elif auth_code == USER_PASS_CODE:
            return ["user"]
        return None
