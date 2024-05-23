#!/usr/bin/env python3
"""Implements basic authentication"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """Represents subclass basic auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            encoded_value = base64.b64encode(
                decoded_value.encode('utf-8')).decode('utf-8')
            if encoded_value == base64_authorization_header:
                return decoded_value
            else:
                return None
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value."""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(':'))
