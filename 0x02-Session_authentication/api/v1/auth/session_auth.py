#!/usr/bin/env python3
"""SessionAuth class that update authentication"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """SessionAuth that inherits Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session allows multiple session IDs to be associated
        with the same user_id."""
        if user_id is not None:
            if type(user_id) == str:
                client_id = str(uuid.uuid4())
                self.user_id_by_session_id[client_id] = user_id
                return client_id
            return None
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method fetch the user_id based on the
        session ID and ensuring the authentication works by linking a user
        to a session ID."""
        if session_id is not None:
            if type(session_id) == str:
                return self.user_id_by_session_id.get(session_id)
            return None
        return None
