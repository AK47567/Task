from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated


from .serializers import UserRegistrationSerializer, UserLoginSerializer, TaskSerializer
from .models import Users, Task

# Create your views here.


class UserRegistrationAPIView(APIView):
    """
    Creates a new user.
    
    Parameters:
    - `username`: the username of the user
    - `first_name`: the first name of the user
    - `last_name`: the last name of the user
    - `email`: the email address of the user
    - `password`: the password of the user
    
    Returns:
    - `201 Created`: the user has been successfully created
    - `400 Bad Request`: if the request contains invalid data
    """

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user_data = serializer.validated_data
                user=Users(username=user_data['username'], first_name=user_data['first_name'], last_name=user_data['last_name'],email=user_data['email'])
                user.set_password(user_data['password'])
                user.save()
                return Response("User Registered Successfully", status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):

    """
    Logs in a user.

    Parameters:
    - `username`: the username of the user
    - `password`: the password of the user

    Returns:
    - `202 Accepted`: the user has been successfully logged in
    - `401 Unauthorized`: if the username or password is incorrect
    - `400 Bad Request`: if the request contains invalid data
    """
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            try:
                user=authenticate(request, username=username, password=password)
                if user:
                    return Response("User Logged in Successfully", status.HTTP_202_ACCEPTED)
                return Response("Invalid credentials", status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response(str(e), status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            

class TaskCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    """
    Gets all the tasks for the logged in user.

    Parameters:
    - `id`: the id of the task (optional)

    Returns:
    - `200 OK`: a list of tasks
    - `400 Bad Request`: if the request contains invalid data
    - `401 Unauthorized`: if the user is not logged in
    """

    def get(self, request,id=None):
        try:
            if id:
                query = Task.objects.filter(user=request.user, id=id)
                if not query:
                    return Response("Please enter valid Task Id", status.HTTP_400_BAD_REQUEST)
            else:
                query = Task.objects.filter(user=request.user)
            serializer = TaskSerializer(query, many=True)
            
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)
        

    """
    Creates a new task for the logged in user.

    Parameters:
    - `name`: the name of the task
    - `description`: the description of the task
    - `type`: the type of the task
    - `status`: the status of the task

    Returns:
    - `201 Created`: the created task
    - `400 Bad Request`: if the request contains invalid data
    - `401 Unauthorized`: if the user is not logged in
    """

    def post(self, request, *args, **Kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

    """
    Updates a task for the logged in user.

    Parameters:
    - `id`: the id of the task to be updated
    - `name`: the name of the task
    - `description`: the description of the task
    - `type`: the type of the task
    - `status`: the status of the task

    Returns:
    - `200 OK`: the updated task
    - `400 Bad Request`: if the request contains invalid data
    - `401 Unauthorized`: if the user is not logged in
    - `404 Not Found`: if the task with the given id does not exist
    """
    
    def put(self, request, id=None, *args, **kwargs):
        try:
            if not id:
                return Response("Method PUT not allowed without ID", status.HTTP_400_BAD_REQUEST)
            query = Task.objects.get(id=id)
            serializer = TaskSerializer(query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)
        
