#!/usr/bin/env python3
"""BasicAuth"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials method will correctly extract a the
        user email and password from the decoded Base64 authorization."""
        auth64 = decoded_base64_authorization_header
        if not auth64 or type(auth64) != str:
            return None, None

        elif ':' in auth64:
            email, sep, password = auth64.partition(':')
            return email, password
        else:
            return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials check if both the email and password
        are correct, and return the User instance"""
        if type(user_email) == str or type(user_pwd) == str:
            if not user_email or not user_pwd:
                return None
            if not User.search({'email': user_email}) or len(
                    User.search({'email': user_email})) == 0:
                return None
            clients = User.search({'email': user_email})
            client = clients[0]
            if not client.is_valid_password(user_pwd):
                return None
            return client
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user it uses the methods authorization_header,
        extract_base64_authorization_header, extract_user_credentials,
        decode_base64_authorization_header, user_object_from_credentials
        to check the user credentials"""
        user = self.authorization_header(request)
        base64_auth = self.extract_base64_authorization_header(user)
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        client = self.extract_user_credentials(decoded_auth)
        user_email, user_pwd = client
        if not user or not base64_auth or not decoded_auth or not client:
            return None
        return self.user_object_from_credentials(user_email, user_pwd)
