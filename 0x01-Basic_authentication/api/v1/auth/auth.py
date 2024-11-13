#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required. """
        return False


    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header. """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user (to be implemented later). """
        return None

