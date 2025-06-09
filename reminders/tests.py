from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from reminders.models import Reminder

class ReminderAPITest(APITestCase):

    def setUp(self):
        self.url = "/api/reminders/create/"
        self.valid_payload = {
            "date": "2025-06-10",
            "time": "14:30:00",
            "message": "Meeting with the product team",
            "reminder_type": "EMAIL"
        }
        self.invalid_payload = {
            "date": "",
            "time": "14:30:00",
            "message": "",
            "reminder_type": "WHATSAPP" 
        }

    def test_create_valid_reminder(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Reminder saved successfully!")
        self.assertEqual(Reminder.objects.count(), 1)

    def test_create_invalid_reminder(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('date', response.data)
        self.assertIn('message', response.data)
        self.assertIn('reminder_type', response.data)
