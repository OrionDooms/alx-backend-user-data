#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound as ORMNoResultFound

from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add_user method allows you to create s new user in the table
        """
        session = self._session
        client = User(email=email, hashed_password=hashed_password)
        session.add(client)
        session.commit()
        return client

    def find_user_by(self, **kwargs) -> User:
        """find_user_by it will print the user's ID or it will print an
        error message based on the exception raised."""
        session = self._session
        user = session.query(User).filter_by(**kwargs).first()
        if not kwargs:
            raise InvalidRequestError("Invalid Request")
        if user is None:
            raise NoResultFound("NO Result Found")
        return user
