
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer, LoginSerializers
from http import HTTPStatus
from rest_framework import status
from django.contrib.auth.models import User



@api_view(['Get'])
def hello(request):
    return Response({"Hii you can do it"})


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            success = {
                'id' : user.id,
                'email': user.email,
                'username' : user.username

            }
            return Response(success, status=status.HTTP_201_CREATED) # syntax research
        

class Login(APIView):
     def post(self, request):
        serializer = LoginSerializers(data = request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             

class listUser(APIView):
    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UpdateUser(APIView):
    def patch(self, request):
        user_id = request.query_params.get('id')
        
        if not user_id:
            return Response({'error': 'User ID is required as query parameter'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK)

