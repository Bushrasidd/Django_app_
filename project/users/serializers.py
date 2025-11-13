from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length = 50)
    email = serializers.EmailField(max_length = 50)
    password = serializers.CharField(write_only = True, min_length = 8)

    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("email already exist")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)   # always hash password properly

        instance.save()
        return instance


    