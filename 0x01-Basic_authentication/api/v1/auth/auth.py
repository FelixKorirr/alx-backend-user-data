#!/usr/bin/env python3
"""
Module to manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Represents the class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Defines routes require or don't need authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for item in excluded_paths:
            if path.rstrip('/') == item.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns none"""
        return None
