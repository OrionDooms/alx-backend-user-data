#!/usr/bin/env python3
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """SessionAuth that inherits Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is not None and type(user_id) == str:
            client_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[client_id] = user_id
            return client_id
        return None
