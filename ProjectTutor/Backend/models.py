from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hours = models.IntegerField()
    learning_goals = models.TextField(max_length=400)
    assigned_tutors = models.ManyToManyField("Tutor", related_name="students_assigned", blank=True)

    def __str__(self):
        return f'username: {self.user.username}'


class Tutor(models.Model):
    SUBJECT_CHOICES = [
        ("Math", "Math"),
        ("BioChem", "BioChem"),
        ("Physics", "Physics"),
        ("Engineering", "Engineering"),
        ("History", "History"),
        ("English", "English"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student, related_name="tutors_assigned", blank=True)
    subjects_taught = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    hours = models.IntegerField()
    name = models.TextField(max_length=400)

    def __str__(self):
        return self.name
