from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerialzer,LoginSerialzer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

class Registerview(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerialzer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,   
                    'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response({
                    'data': {
                        'refresh': str(refresh),
                        'access': access_token
                    },   
                    'message': 'your account created'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
               'data': {},   
               'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST) 


class Loginview(APIView): 
    def post(self, request):
        try:
            print("Request data:", request.data)  # Log the incoming data
            data = request.data
            serializer = LoginSerialzer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,   
                    'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            
            response = serializer.get_jwt_token(serializer.data)     
            return Response(response, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            print(e)
            return Response({
               'data': {},   
               'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)