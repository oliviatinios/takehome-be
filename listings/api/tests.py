from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import House
from .serializers import HouseSerializer


class GetAllHousesTest(APITestCase):
    """ 
    Test module for GET all houses route 
    """

    def setUp(self):
        # Create objects in db
        House.objects.create(area_unit='SqFt', home_type='SingleFamily', link='www.example.com/1',
                             price=500000.00, address='55 Street Avenue', city='San Diego', state='California', zipcode=123456)
        House.objects.create(area_unit='SqFt', home_type='SingleFamily', link='www.example.com/2',
                             price=400000.00, address='56 Street Avenue', city='Portland', state='Oregon', zipcode=987654)

    def test_get_all_houses(self):
        # Fetch all houses using api
        url = reverse('get_post_houses')
        response = self.client.get(url)
        # Fetch all houses from db
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        # Assertions
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleHouseTest(APITestCase):
    """ 
    Test module for GET house by id 
    """

    def setUp(self):
        # Create objects in db
        House.objects.create(area_unit='SqFt', home_type='SingleFamily', link='www.example.com/1',
                             price=500000.00, address='55 Street Avenue', city='San Diego', state='California', zipcode=123456)
        House.objects.create(area_unit='SqFt', home_type='SingleFamily', link='www.example.com/2',
                             price=400000.00, address='56 Street Avenue', city='Portland', state='Oregon', zipcode=987654)

    def test_get_single_house_valid(self):
        """
        Ensure we can fetch all houses
        """
        # Fetch house by id using api
        house_id = 1
        url = reverse('get_update_delete_houses', kwargs={'pk': house_id})
        response = self.client.get(url)
        # Fetch house by id from db
        house = House.objects.get(id=house_id)
        serializer = HouseSerializer(house)
        # Assertions
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_house_invalid(self):
        """
        Ensure we can fetch all houses
        """
        # Fetch house by id using api
        url = reverse('get_update_delete_houses', kwargs={'pk': 3})
        response = self.client.get(url)
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
