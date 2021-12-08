from django.shortcuts import render
from first_api_backend.models import *
# Create your views here.

def index(request):
    return render(request, 'first_api_backend/first_api_backend_index.html')

def second_page(request):
    second_page_list = Rack.objects.order_by('id')
    second_page_dict = {'second_page_key': second_page_list}
    return render(request, 'first_api_backend/first_api_backend_2.html', context = second_page_dict)
