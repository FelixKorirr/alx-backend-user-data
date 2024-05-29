#!/usr/bin/env python3
"""Hash password module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Generates a password hash value"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user in the database if he does not exist"""
        try:
            user_data = self._db.find_user_by(email=email)
            if user_data:
                raise ValueError(f'User {email} already exists')

        except NoResultFound:
            hashed = _hash_password(password)
            self._db.add_user(email, hashed)
        else:
            return None