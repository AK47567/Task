from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Users(AbstractUser):
    """
    Custom user model with added phoneNumber field.
    """
    groups = models.ManyToManyField(Group,related_name="custom_user_groups",blank=True)
    user_permissions = models.ManyToManyField(Permission,related_name="custom_user_permissions", blank=True)
    phoneNumber = models.CharField(max_length=10)


class Task(models.Model):
    """
    Model representing a task
    """
    Status = (
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Failed", "Failed")
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=200, choices=Status, default="Pending")
    user = models.ManyToManyField(Users, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
