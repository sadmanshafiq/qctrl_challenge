import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from .models import Controls, Control_Types
from .serializers import ControlSerializer

#Initialize API Client app
client = Client()

class GetAllControlsTest(TestCase):
    """ Test module for GET all controls API """

    def setUp(self):
        Control_Types.objects.create(control_types='Gaussian')
        Control_Types.objects.create(control_types='Primitive')
        Control_Types.objects.create(control_types='CinSK')
        Control_Types.objects.create(control_types='CinBB')
        
        Controls.objects.create(
            name='Casper', ctype=Control_Types.objects.get(control_types='Gaussian'), maximum_rabi_rate=12, polar_angle=0.32)
        Controls.objects.create(
            name='Jas', ctype=Control_Types.objects.get(control_types='Primitive'), maximum_rabi_rate=53, polar_angle=0.212)
        Controls.objects.create(
            name='Dev Single', ctype=Control_Types.objects.get(control_types='CinSK'), maximum_rabi_rate=10, polar_angle=0.8231)
        Controls.objects.create(
            name='Zresk pro', ctype=Control_Types.objects.get(control_types='CinBB'), maximum_rabi_rate=62, polar_angle=0.4323)

    def test_get_all_controls(self):
        # get API response
        response = client.get(reverse('get_post_control'))
        # get data from db
        controls = Controls.objects.all()
        serializer = ControlSerializer(controls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        Control_Types.objects.create(control_types='Gaussian')
        Control_Types.objects.create(control_types='Primitive')
        Control_Types.objects.create(control_types='CinSK')
        Control_Types.objects.create(control_types='CinBB')
        self.casper = Controls.objects.create(
            name='Casper', ctype=Control_Types.objects.get(control_types='Gaussian'), maximum_rabi_rate=12, polar_angle=0.32)
        self.muffin = Controls.objects.create(
            name='Jas', ctype=Control_Types.objects.get(control_types='Primitive'), maximum_rabi_rate=53, polar_angle=0.212)           
        self.rambo = Controls.objects.create(
            name='Dev Single', ctype=Control_Types.objects.get(control_types='CinSK'), maximum_rabi_rate=10, polar_angle=0.8231)
        self.ricky = Controls.objects.create(
            name='ricky', ctype=Control_Types.objects.get(control_types='CinBB'), maximum_rabi_rate=62, polar_angle=0.4323)

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