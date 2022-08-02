from django.shortcuts import render

# Create your views here.
from django.views import generic
from services.models import Services,Customer


class ServicesListView(generic.ListView):
    model = Services
    template_name = 'services_list.html'

class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'customer_list.html'
