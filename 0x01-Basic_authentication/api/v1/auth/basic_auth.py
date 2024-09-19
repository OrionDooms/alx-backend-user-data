#!/usr/bin/env python3
"""BasicAuth"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth that inherits from Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header check If all the conditions are
        satisfied it return the part of the authorization_header that comes
        after basic."""
        if authorization_header is not None:
            if type(authorization_header) != str:
                return None
            if not authorization_header.startswith("Basic "):
                return None
            return authorization_header[len("Basic "):]
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header Gives a valid Base64 string,
        the method will decode it and return a string."""
        if base64_authorization_header is not None:
            if type(base64_authorization_header) != str:
                return None
            try:
                data = base64.b64decode(base64_authorization_header)
                return data.decode('utf-8')
            except (base64.binascii.Error, UnicodeDecodeError):
                return None
        else:
            return None
