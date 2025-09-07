from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # ✅ only meta options here


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
        ('Librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default="Unknown")  # put default here

    def __str__(self):
        return self.name

   