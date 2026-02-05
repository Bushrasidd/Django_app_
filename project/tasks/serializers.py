from rest_framework import serializers
from .models import Task


class Create_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id','created_at']





# class del_task(serializers.Serializer):
#         id = serializers.IntegerField()
#         def save(self):
#             task_id = self.validated_data.get('id')
#             task  = task.objects.filter(id=task_id)
#             if not task.exists():
#                 raise serializers.ValidationError({"id": "User does not exist"})
#             task.delete()

#             return {"message": "Task deleted successfully"}

   