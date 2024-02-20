from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        CANCELLED = 'cancelled', 'Cancelled'

    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(5)], help_text="Enter the title of the event (minimum 5 characters).")
    description = models.TextField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    description = models.TextField(help_text="Enter a description for the event.", null=True)
    location = models.CharField(max_length=100, validators=[MinLengthValidator(3)], help_text="Enter the location of the event (minimum 3 characters or leave blank).", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='events', help_text="Select the user who owns the event.")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT, help_text="Select the status of the event.")

    def __str__(self):
        return self.title

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} attending {self.event}'