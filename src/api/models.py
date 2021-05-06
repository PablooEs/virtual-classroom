from django.db import models
from django.core.validators import MaxValueValidator


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Person(models.Model):
    dni = models.PositiveIntegerField(primary_key=True, validators=[
                                      MaxValueValidator(99999999)])
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=False)


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50, unique=True)


class User(models.Model):
    dni = models.OneToOneField(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Participant(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
