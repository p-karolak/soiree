from django.test import TestCase
from django.urls import reverse
from .models import Event
from django.contrib.auth.models import User


# model test

def test_model_can_create_a_event(self):
    old_count = Event.objects.count()
    self.event.save()
    new_count = Event.objects.count()
    self.assertNotEqual(old_count, new_count)

# view tests
    
def test_index_view(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No events are available.")
    self.assertQuerysetEqual(response.context['latest_event_list'], [])
    