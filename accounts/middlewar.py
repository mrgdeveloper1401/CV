from typing import Any
from urllib.request import Request
from django.shortcuts import redirect
from django.contrib import messages



LOGIN_EXEMPT_URL = [
    # '/',
    '/accounts/login/',
    '/accounts/signup/',
]


class Authenticated:
    def __init__(self, get_responce):
        self.get_responce = get_responce
        
    def __call__(self, request: Request, *args: Any, **kwds: Any) -> Any:
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged', 'danger')
        responce = self.get_responce(request)
        return responce