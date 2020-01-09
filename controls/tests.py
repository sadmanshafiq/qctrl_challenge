# Tests.py is used for testing the controls and the controls serializer to make sure the api responds correctly
# Used alongside Postman to check if the CRUD operations work correctly.

import json
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from .views import BaseViewSet,import_controls,export_controls
from .models import Controls
from .serializers import ControlSerializer

#Initialize API Client app
client = APIClient()
factory = APIRequestFactory()


class GetAllControlsTest(TestCase):
    """ Test module for GET all controls API """

    def setUp(self):
        Controls.objects.create(
            name='Jas', type='Primitive', maximum_rabi_rate=53, polar_angle=0.212)
        Controls.objects.create(
            name='Dev Single', type='CORPSE', maximum_rabi_rate=10, polar_angle=0.8231)
        Controls.objects.create(
            name='Zresk pro', type='CinSK', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_all_controls(self):
        # get API response
        response = client.get(reverse('controls-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleControlTest(TestCase):
    """ Test module for GET single Control API """

    def setUp(self):
        self.casper = Controls.objects.create(
            name='Casper', type='Gaussian', maximum_rabi_rate=12, polar_angle=0.32)
        self.muffin = Controls.objects.create(
            name='Jas', type='Primitive', maximum_rabi_rate=53, polar_angle=0.212)           
        self.rambo = Controls.objects.create(
            name='Dev Single', type='CinSK', maximum_rabi_rate=10, polar_angle=0.8231)
        self.ricky = Controls.objects.create(
            name='ricky', type='CinBB', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_valid_single_control(self):
        response = client.get(
            reverse('controls-detail', kwargs={'pk': self.rambo.pk}))
        controls = Controls.objects.get(pk=self.rambo.pk)
        serializer = ControlSerializer(controls)
        self.assertDictEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_control(self):
        response = client.get(
            reverse("controls-detail", kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewControlTest(TestCase):
    """ Test module for inserting a new Control """

    def setUp(self):
        self.invalid_payload = {
                "type": "Controls",
                "attributes": {
                    "name": "Muffin",
                    "type": "Primitive",
                    "maximum_rabi_rate": 123.24,
                    "polar_angle": 0.345
                }
            }
        
    def test_create_invalid_control(self):
        response = client.post(
            reverse("controls-list"), 
            data=self.invalid_payload,
            content_type='application/vnd.api+json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)