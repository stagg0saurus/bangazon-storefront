from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from bangazon_ultra.models.customer_model import * 
from bangazon_ultra.models.products_model import * 
from bangazon_ultra.models.product_types_model import * 
from bangazon_ultra.views.product_types_view import * 
from bangazon_ultra.views.all_products_view import * 


# Create your tests here.

class TestProductTypes(TestCase):
    """
    The purpose of this class is to test categories of products on the
    bangazon site.

    Methods: 
        setUp-
        test_get_all_product_types-
        get_all_products_for_a_given_product_type

    Author: Ike, Main Bananas
    """

    # add a category to the database
    # return all categories in the database
    # Can I get all the categories from the database?
        #self.assertContains(response, "category_name")
        #self.assertContains(response, "category_name")


    def setUp(self):
        """ The purpose of this function is to create the conditions
        necessary for my tests to be measured
        Author: Ike, Main Bananas
        """
        
        user = User.objects.create_user(first_name='Kyrie', last_name='Irving', username='unc Drew', email='ky@cl.com', password='ispassword')
        self.kyrie = Customer.objects.create(user=user, phone='4257896453', shipping_address="The Flat Earth", )
        self.shoes = ProductTypes.objects.create(category_name="Shoes")
        self.books = ProductTypes.objects.create(category_name="Books")
        self.book1 = Product.objects.create(title="Man's Search for Meaning", description="Book by Frankl",
        seller=self.kyrie, product_type=self.books, price=15.00, quantity=3)
        self.book2 = Product.objects.create(
            title="The Four Agreements", 
            description="Book by Ruiz",
            seller=self.kyrie,
            product_type=self.books,
            price=16.00, 
            quantity=4)

    def test_all_products_renders(self):
        response = self.client.get(reverse('bangazon_ultra:allProductsView', args={self.books.pk}))
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context['productsType_id'].pk, self.books.pk)