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
        """Returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns False"""
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns none"""
        return None
