#!/usr/bin/env python3
"""Managing the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """This is the template for all authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth currenty return False"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header currenty return None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current_user currenty return None"""
        return None
