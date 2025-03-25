from rest_framework import serializers
from .models import Users, Task

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name','email', 'phoneNumber', 'password']
        extra_kwargs = {'password': {'write_only': True}, }

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = Users.objects.all(), many=True, required=False, allow_empty=True
    )

    class Meta:
        model = Task
        fields = ['id','name', 'description', 'type', 'status', 'user']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)



