from rest_framework import serializers
from .models import Task


class Create_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id','created_at']

   