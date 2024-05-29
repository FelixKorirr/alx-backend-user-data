#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def _hash_password(password):
    """Generates a password hash value"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
