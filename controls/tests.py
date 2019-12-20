from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Controls
from .serializers import ControlsSerializer

# Create your tests here.
class BaseViewTest(APITestCase):

    client = APIClient()



    @staticmethod

    def create_control(title="", artist=""):

        if title != "" and artist != "":

            Controls.objects.create(title=title, artist=artist)



    def setUp(self):

        # add test data

        self.create_control("like glue", "sean paul")

        self.create_control("simple song", "konshens")

        self.create_control("love is wicked", "brick and lace")

        self.create_control("jam rock", "damien marley")





class GetAllSongsTest(BaseViewTest):



    def test_get_all_controls(self):

        """

        This test ensures that all controls added in the setUp method

        exist when we make a GET request to the controls/ endpoint

        """

        # hit the API endpoint

        response = self.client.get(

            reverse("controls-all", kwargs={"version": "v1"})

        )

        # fetch the data from db

        expected = Controls.objects.all()

        serialized = ControlsSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)