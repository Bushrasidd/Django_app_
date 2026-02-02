import select
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Create_Task_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from http import HTTPStatus
from rest_framework.exceptions import ValidationError, ValidationError, NotAuthenticated, PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .models import Task


class create_task(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = Create_Task_Serializer(data = request.data)
        try: 
            if serializer.is_valid(raise_exception=True):
                task = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except(NotAuthenticated, PermissionDenied):
            return Response({"Message": "Access Denied"},status=status.HTTP_403_FORBIDDEN)
        except IntegrityError:
            return Response({"error": "Integrity Error occurred."}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Requested object does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class get_task(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
         tasks =Task.objects.filter(user=request.user)  # select * from task where user = request.user_id
         serializer = Create_Task_Serializer(tasks, many = True)
         return Response(serializer.data, status = status.HTTP_200_OK)
    


# class update_task(APIView):
#     permission_classes = [IsAuthenticated]


        


        

           
       







