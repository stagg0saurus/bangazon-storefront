from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from bangazon_ultra.models import *

def addProduct(request): 
	"""
		# This view allows a user to add a product for sale to the generally viewable product list.
		# Author: PS, Main Bananas

			# When adding a product, users will be directed to a new template with a form for inputs:
			# Function for adding and persisting products: 
	"""
	data = request.POST
	seller = customer_model.Customer.objects.get(user=request.user)
	#the data'[dropdown]' reflects the selected value in the template.
	product_type = product_types_model.ProductTypes.objects.get(category_name=data['dropdown'])
	new_product = products_model.Product.objects.create(
		title = data['title'],
		description = data['description'], 
		seller = seller,
		product_type = product_type, 
		price = data['price'], 
		quantity = data['quantity']
	)
	return HttpResponseRedirect('/add/')

def renderProduct(request):
    categories = product_types_model.ProductTypes.objects.all()
    return render(request, 'bangazon_ultra/add_product.html', {'categories': categories})



