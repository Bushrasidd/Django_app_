from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.Serializer): # syntax research

    username = serializers.CharField(max_length = 50) # syntax research
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
    


class LoginSerializers(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username = username, password = password)

        if not user:
            raise serializers.ValidationError("Invalid username or password") # syntax research
        

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            }
        }
    

class deleteUser(serializers.Serializer):
    id = serializers.IntegerField()

    def del_user(self):
        user_id = self.validated_data.get('id')
        deleted_count, _ = User.objects.filter(id=user_id).delete()
        if deleted_count == 0:
            raise serializers.ValidationError("User does not exist")
        return {"message": "User deleted successfully"}
    

    







    