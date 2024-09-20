#!/usr/bin/env python3
"""Managing the API authentication"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """This is the template for all authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth return True if path or excluded_paths is None,
        and at end of paths should have '/' ."""
        if path is None or excluded_paths is None:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            if not path.endswith('/'):
                path += '/'
            if fnmatch.fnmatch(path, path):
                return False
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header return None if request or request.
        headers.get('Authorization') is None else return request.
        headers.get('Authorization')"""
        if request is not None:
            if request.headers.get('Authorization') is None:
                return None
            else:
                return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current_user currenty return None"""
        return None
