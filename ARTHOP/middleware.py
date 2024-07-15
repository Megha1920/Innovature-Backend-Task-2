# backend/middleware.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_authentication = JWTAuthentication()
        try:
            # Validate the JWT token
            user, _ = jwt_authentication.authenticate(request)
            request.user = user  # Set the authenticated user in the request object
            return self.get_response(request)
        except Exception as e:
            # Token validation failed
            return Response({'message': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)
