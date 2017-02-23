from django.test import TestCase
from django.urls import reverse
from bangazon_storefront.models import *
from bangazon_storefront.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class TestOrder(TestCase):
    """
    This class tests everything related to an order.

    Method List
    test_customer_can_create_an_order
    Arguments unittest.TestCase allows the unittest model to know what to test.
    Author Zoe LeBlanc, Python Ponies
    """
    def setUp(self):
        '''This method sets up initial instances of Customer from the database'''
        user = User.objects.create_user(
            first_name = "Zoe",
            last_name = "LeBlanc",
            username = "zoe",
            email = "z@z.com",
            password = "1234asdf"
        )
        self.customer = customer_model.Customer.objects.create(
            user = user,
            phone = "513498234",
            shipping_address="asdfasf"
        )
        self.customer_order = order_model.Order.objects.create(
            buyer=self.customer
        )
        print(self.customer_order.pk)
        self.client.login(
            username = "zoe",
            password = "1234asdf"
        )

    def test_order_view(self):
        """
        Test that a customer can view on order
        """
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)
        

    def test_customer_can_display_order_and_products_view(self):
        """
        Test that a customer can create an order on order view
        """
        response = self.client.get(reverse('bangazon_storefront:order'))
        self.assertEqual(response.context['order'].pk, self.customer_order.pk)

        
       
