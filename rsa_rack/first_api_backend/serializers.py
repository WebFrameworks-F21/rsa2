from rest_framework import serializers
from .models import * 

class RackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rack
        fields = ('id', 'size')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('rack_id', 'location_name')

class RouterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Router
        fields = ('rack_id','location_name','routers_id') 

class ipv4_networkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ipv4_network
        fields = ('name', 'ip_range', 'ip_address')

class SwitchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Switch
        fields = ('rack_id','location_name','switchs_id', 'router_id', 'network_name')

class PatchPanelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatchPanel
        fields = ('rack_id','location_name','patchpanels_id', 'switch_id', 'number_of_ports')

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('rack_id','location_name','servers_id', 'patch_panel_id', 'owner')

class BatteryBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BatteryBackup
        fields = ('rack_id','location_name','battery_id')

class NetworkInterfaceCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkInterfaceCard
        fields = ('id', 'server_id', 'ip_address')