#!/usr/bin/env python3
"""
Module to manage API authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """
    Represents the class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Defines routes that need authentication.
        returns False if it exists in excluded paths
        else it returns True.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for item in excluded_paths:
            if path.rstrip('/') == item.rstrip('/'):
                return False
            if item.endswith('*') and path.startswith(item[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns none"""
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns none"""
        return None

    def session_cookie(self, request=None) -> str:
        """Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
