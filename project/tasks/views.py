from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Create_Task_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from http import HTTPStatus

class create_task(APIView):
    def post(self, request):
        serializer = Create_Task_Serializer(data = request.data)
        try: 
            if serializer.is_valid(raise_exception=True):
                task = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except
        

           
       







