from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from Passenger.models import User_home_owner
from Room.models import Rooms


class RoomEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User_home_owner.objects.create(user=self._create_user('owner', 'owner@example.com'), slug='owner-slug')
        self.room = Rooms.objects.create(
            owner=self.owner,
            location='تهران',
            city='تهران',
            Dormitory='ویلا تست',
            building_Information='توضیح',
            Bed_Service='2 تخت',
            Toilet_Bathroom='1 دستشویی',
            Accommodation_cap='4',
            Perspective='چشم‌انداز',
            Internal_Faclities='WiFi',
            Additional_details='متن',
            price='1000000',
        )

    def _create_user(self, username, email):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.create_user(username=username, email=email, password='Pass1234!')

    def test_room_list_returns_rooms(self):
        response = self.client.get(reverse('roomList'))
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
