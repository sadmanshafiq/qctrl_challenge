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
            name='Jas', ctype='Primitive', maximum_rabi_rate=53, polar_angle=0.212)
        Controls.objects.create(
            name='Dev Single', ctype='CORPSE', maximum_rabi_rate=10, polar_angle=0.8231)
        Controls.objects.create(
            name='Zresk pro', ctype='CinSK', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_all_controls(self):
        # get API response
        response = client.get('')
        # get data from db
        controls = Controls.objects.all()
        serializer = ControlSerializer(controls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleControlTest(TestCase):
    """ Test module for GET single Control API """

    def setUp(self):
        self.casper = Controls.objects.create(
            name='Casper', ctype='Gaussian', maximum_rabi_rate=12, polar_angle=0.32)
        self.muffin = Controls.objects.create(
            name='Jas', ctype='Primitive', maximum_rabi_rate=53, polar_angle=0.212)           
        self.rambo = Controls.objects.create(
            name='Dev Single', ctype='CinSK', maximum_rabi_rate=10, polar_angle=0.8231)
        self.ricky = Controls.objects.create(
            name='ricky', ctype='CinBB', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_valid_single_control(self):
        response = client.get(
            reverse('controls-detail', kwargs={'pk': self.rambo.pk}))
        controls = Controls.objects.get(pk=self.rambo.pk)
        serializer = ControlSerializer(controls)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_control(self):
        response = client.get(
            reverse("controls-detail", kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewControlTest(TestCase):
    """ Test module for inserting a new Control """

    def setUp(self):
        #Control_Types.objects.create(control_types='Gaussian')
        #Control_Types.objects.create(control_types='Primitive')
        #Control_Types.objects.create(control_types='CinSK')
        #Control_Types.objects.create(control_types='CinBB')
        self.valid_payload = {
                "type": "Controls",
                "attributes": {
                    "name": "Muffin",
                    "ctype": "Primitive",
                    "maximum_rabi_rate": 23.24,
                    "polar_angle": 0.345
                }
            }
        self.invalid_payload = {
                "type": "Controls",
                "attributes": {
                    "name": "Muffin",
                    "ctype": "Primitive",
                    "maximum_rabi_rate": 123.24,
                    "polar_angle": 0.345
                }
            }
        

    def test_create_valid_control(self):
        response = client.post(
            reverse("controls-list"),
            data=self.valid_payload,
            content_type='application/vnd.api+json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_control(self):
        response = client.post(
            reverse("controls-list"), 
            data=self.invalid_payload,
            content_type='application/vnd.api+json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)