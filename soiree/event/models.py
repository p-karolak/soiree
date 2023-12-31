from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200,validators=[MinLengthValidator(5)])
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} attending {self.event}'