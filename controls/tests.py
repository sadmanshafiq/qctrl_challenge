import json
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from .models import Controls
from .serializers import ControlSerializer

#Initialize API Client app
client = APIClient()
factory = APIRequestFactory()
class GetAllControlsTest(TestCase):
    """ Test module for GET all controls API """

    def setUp(self):
        
        Controls.objects.create(
            name='Casper', ctype='GAUS', maximum_rabi_rate=12, polar_angle=0.32)
        Controls.objects.create(
            name='Jas', ctype='PRIM', maximum_rabi_rate=53, polar_angle=0.212)
        Controls.objects.create(
            name='Dev Single', ctype='CORP', maximum_rabi_rate=10, polar_angle=0.8231)
        Controls.objects.create(
            name='Zresk pro', ctype='CINS', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_all_controls(self):
        # get API response
        response = client.get(reverse('get_post_control'))
        # get data from db
        controls = Controls.objects.all()
        serializer = ControlSerializer(controls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleControlTest(TestCase):
    """ Test module for GET single Control API """

    def setUp(self):
        #Control_Types.objects.create(control_types='Gaussian')
        #Control_Types.objects.create(control_types='Primitive')
        #Control_Types.objects.create(control_types='CinSK')
        #Control_Types.objects.create(control_types='CinBB')
        self.casper = Controls.objects.create(
            name='Casper', ctype='GAUS', maximum_rabi_rate=12, polar_angle=0.32)
        self.muffin = Controls.objects.create(
            name='Jas', ctype='PRIM', maximum_rabi_rate=53, polar_angle=0.212)           
        self.rambo = Controls.objects.create(
            name='Dev Single', ctype='CINS', maximum_rabi_rate=10, polar_angle=0.8231)
        self.ricky = Controls.objects.create(
            name='ricky', ctype='CINB', maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_valid_single_control(self):
        response = client.get(
            reverse('get_delete_update_control', kwargs={'pk': self.rambo.pk}))
        controls = Controls.objects.get(pk=self.rambo.pk)
        serializer = ControlSerializer(controls)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_control(self):
        response = client.get(
            reverse('get_delete_update_control', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewControlTest(TestCase):
    """ Test module for inserting a new Control """

    def setUp(self):
        #Control_Types.objects.create(control_types='Gaussian')
        #Control_Types.objects.create(control_types='Primitive')
        #Control_Types.objects.create(control_types='CinSK')
        #Control_Types.objects.create(control_types='CinBB')
        self.valid_payload = {
            'name': 'Muffin',
            'ctype': 'PRIM',
            'maximum_rabi_rate': 23.24,
            'polar_angle': 0.345
        }
        self.invalid_payload = {
            'name': 'ADE',
            'ctype': 'GAUS',
            'maximum_rabi_rate': 123.24,
            'polar_angle': 0.345
        }

    def test_create_valid_control(self):
        response = client.post(
            reverse('get_post_control'),
            data=self.valid_payload,
            content_type='application/vnd.api+json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_control(self):
        response = client.post(
            reverse('get_post_control'), 
            data=self.invalid_payload,
            content_type='application/vnd.api+json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)