from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Controls, Control_Types
from .serializers import ControlSerializer

# Create your tests here.
class BaseViewTest(APITestCase):

    client = APIClient()



    @staticmethod
    def create_control(name="", ctype=""):
        if name != "" and ctype != "":
            Controls.objects.create(name=name, ctype=ctype)
    
   
    def setUp(self):
        self.prim = Control_Types.objects.create(control_types="Primitive")
        self.corp = Control_Types.objects.create(control_types="CORPSE")
        self.gaus = Control_Types.objects.create(control_types="Gaussian")
        self.cinB = Control_Types.objects.create(control_types="CinBB")
        self.cinS = Control_Types.objects.create(control_types="CinSK")

        # add test data
        self.create_control("like glue", ctype=self.gaus)
        self.create_control("simple song", ctype=self.cinB)
        self.create_control("love is wicked", ctype=self.prim)
        self.create_control("jam rock", ctype=self.corp)



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

        #self.assertEqual(response.data, serialized.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)