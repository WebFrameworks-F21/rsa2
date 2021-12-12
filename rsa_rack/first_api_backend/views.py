from rest_framework import viewsets
from .serializers import *
from django.shortcuts import render
from first_api_backend.models import *
# Create your views here.

# def index(request):
#     return render(request, 'first_api_backend/first_api_backend_index.html')

# def second_page(request):
#     second_page_rack_list = Rack.objects.order_by('id')
#     second_page_router_list = Router.objects.order_by('id')
#     second_page_ipv4_network_list = ipv4_network.objects.order_by('name')
#     second_page_switch_list = Switch.objects.order_by('id')
#     second_page_patch_panel_list = PatchPanel.objects.order_by('id')
#     second_page_server_list = Server.objects.order_by('id')
#     second_page_battery_backup_list = BatteryBackup.objects.order_by('id')
#     second_page_network_interface_card_list = NetworkInterfaceCard.objects.order_by('id')
#     second_page_dict = {'second_page_rack_key': second_page_rack_list, 'second_page_router_key': second_page_router_list, 'second_page_ipv4_network_key': second_page_ipv4_network_list,'second_page_switch_key': second_page_switch_list,'second_page_patch_panel_key': second_page_patch_panel_list,'second_page_server_key': second_page_server_list,'second_page_battery_backup_key': second_page_battery_backup_list,'second_page_network_interface_card_key': second_page_network_interface_card_list }
#     return render(request, 'first_api_backend/first_api_backend_2.html', context = second_page_dict)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('location_name')
    serializer_class = LocationSerializer
    
class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all().order_by('id')
    serializer_class = RackSerializer

class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all().order_by('id')
    serializer_class = RouterSerializer

class ipv4_networkViewSet(viewsets.ModelViewSet):
    queryset = ipv4_network.objects.all().order_by('name')
    serializer_class = ipv4_networkSerializer

class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all().order_by('id')
    serializer_class = SwitchSerializer

class PatchPanelViewSet(viewsets.ModelViewSet):
    queryset = PatchPanel.objects.all().order_by('id')
    serializer_class = PatchPanelSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('id')
    serializer_class = ServerSerializer

class BatteryBackupViewSet(viewsets.ModelViewSet):
    queryset = BatteryBackup.objects.all().order_by('id')
    serializer_class = BatteryBackupSerializer

class NetworkInterfaceCardViewSet(viewsets.ModelViewSet):
    queryset = NetworkInterfaceCard.objects.all().order_by('id')
    serializer_class = NetworkInterfaceCardSerializer






