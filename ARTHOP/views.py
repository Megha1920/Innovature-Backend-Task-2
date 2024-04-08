from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import perform_arithmetic_operation



class AdditionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            if not request.user.is_authenticated:
                return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
            
            data = request.data
            num1 = data.get('num1')
            num2 = data.get('num2')

            if not num1 or not num2:
                return Response({'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

            result = perform_arithmetic_operation(num1, num2, 'add')

            return Response({'result': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubtractionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            if not request.user.is_authenticated:
                return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
            
            data = request.data
            num1 = data.get('num1')
            num2 = data.get('num2')

            if not num1 or not num2:
                return Response({'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

            result = perform_arithmetic_operation(num1, num2, 'subtract')

            return Response({'result': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MultiplicationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            if not request.user.is_authenticated:
                return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
            
            data = request.data
            num1 = data.get('num1')
            num2 = data.get('num2')

            if not num1 or not num2:
                return Response({'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

            result = perform_arithmetic_operation(num1, num2, 'multiply')

            return Response({'result': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DivisionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            if not request.user.is_authenticated:
                return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
            
            data = request.data
            num1 = data.get('num1')
            num2 = data.get('num2')

            if not num1 or not num2:
                return Response({'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
            elif float(num2) == 0:
                return Response({'message': 'Cannot divide by zero'}, status=status.HTTP_400_BAD_REQUEST)

            result = perform_arithmetic_operation(num1, num2, 'divide')

            return Response({'result': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
