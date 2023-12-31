from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from .models import Event
from .models import Attendee
from django.contrib.auth.models import User


# model test

class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.old_event = Event.objects.create(title='Test Event', description='Test description 1', datetime='2024-12-12 12:00', location='Test location', owner=self.user)

    def test_model_can_create_a_event(self):
        old_count = Event.objects.count()
        try:
            self.new_event = Event.objects.create(title='New Test Event', description='Test description 2', datetime='2024-12-12 12:00', location='Test location', owner=self.user)
            self.new_event.full_clean()
            self.new_event.save()
        except ValidationError as e:
            self.fail(f'ValidationError raised: {e}')
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)

class AttendeeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.old_event = Event.objects.create(title='Test Event', description='Test description', datetime='2024-12-12 12:00', location='Test location', owner=self.user)
        self.old_attendee = Attendee.objects.create(event=self.old_event, user=self.user)

    def test_model_can_create_a_attendee(self):
        old_count = Attendee.objects.count()
        try:
            self.new_event = Event.objects.create(title='New Test Event', description='Test description', datetime='2024-12-12 12:00', location='Test location', owner=self.user)
            self.new_attendee = Attendee.objects.create(event=self.new_event, user=self.user)
            self.new_attendee.full_clean()
            self.new_attendee.save()
        except ValidationError as e:
            self.fail(f'ValidationError raised: {e}')
        new_count = Attendee.objects.count()
        self.assertNotEqual(old_count, new_count)

# view tests
    
# class IndexViewTest(TestCase):
#     def test_index_view(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No events are available.")
#         self.assertQuerysetEqual(response.context['latest_event_list'], [])
    