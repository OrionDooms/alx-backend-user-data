#!/usr/bin/env python3
"""BasicAuth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth that inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract_base64_authorization_header check If all the conditions are
        satisfied it return the part of the authorization_header that comes
        after basic."""
        if authorization_header is not None:
            if type (authorization_header) != str:
                return None
            if not authorization_header.startswith("Basic "):
                return None
            return authorization_header[len("Basic "):]
        else:
            return None
