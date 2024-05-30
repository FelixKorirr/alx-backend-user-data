#!/usr/bin/env python3
"""Hash password module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Generates a password hash value"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """Generates a random id"""
    random_id = str(uuid.uuid4())
    return random_id


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
            return User()
        else:
            return None

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if password is hashed"""
        try:
            usr = self._db.find_user_by(email=email)
            if usr:
                stored_passwd = usr.hashed_password
                provided_passwd = password.encode('utf-8')
                return bcrypt.checkpw(provided_passwd, stored_passwd)
        except (AttributeError, NoResultFound):
            return False

    def create_session(self, email: str) -> str:
        """Creates session id"""
        try:
            usr = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(usr.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Finds user by session ID"""
        if session_id is None:
            return None
        try:
            user_data = self._db.find_user_by(session_id=session_id)
            return user_data

        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session"""
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(user_id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates reset password token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        random_id = _generate_uuid()
        self._db.update_user(user.id, reset_token=random_id)
        return random_id
