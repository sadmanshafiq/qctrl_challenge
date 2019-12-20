from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Controls
from .serializers import ControlSerializer

# Create your tests here.
class BaseViewTest(APITestCase):

    client = APIClient()



    @staticmethod

    def create_control(name="", artist=""):

        if name != "" and artist != "":

            Controls.objects.create(name=name, artist=artist)



    def setUp(self):

        # add test data

        self.create_control("like glue", "sean paul")

        self.create_control("simple song", "konshens")

        self.create_control("love is wicked", "brick and lace")

        self.create_control("jam rock", "damien marley")





class GetAllControlsTest(BaseViewTest):



    def test_get_all_controls(self):

        """

        This test ensures that all controls added in the setUp method

        exist when we make a GET request to the controls/ endpoint

        """

        # hit the API endpoint

        response = self.client.get('/controls/')

        # fetch the data from db

        expected = Controls.objects.all()

        serialized = ControlSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)