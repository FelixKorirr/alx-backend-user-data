#!/usr/bin/env python3
"""Implements basic authentication"""
from .auth import Auth


class BasicAuth(Auth):
    """Represents subclass basic auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns base64 part of Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        prefix = 'Basic '
        if authorization_header.startswith(prefix):
            return authorization_header[len(prefix):]
        else:
            return None
