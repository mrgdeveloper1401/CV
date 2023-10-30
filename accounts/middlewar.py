from typing import Any
from django.shortcuts import redirect
from django.contrib import messages


LOGIN_EXEMPT_URL = [
    '/',
    '/accounts/login/',
    '/accounts/signup/',
]


class Authenticated:
    def __init__(self, get_responce):
        self.get_responce = get_responce
        
    def __call__(self, request, *args: Any, **kwds: Any) -> Any:
        if not request.user.is_authenticated and request.path not in LOGIN_EXEMPT_URL:
            messages.error(request, "You must be logged in account or signup account", 'warning')
        responce = self.get_responce(request)
        return responce