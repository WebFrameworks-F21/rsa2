from django.db import models
from django.conf import settings
# Create your models here.

        
class Rack(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    size = models.IntegerField()

    def __str__(self):
        return f'Rack {self.id} of size {self.size} units with {self.size} location spaces'

class Location(models.Model):
    #id = models.IntegerField(primary_key = True, auto_created = True)
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    location_name = models.CharField(max_length =200, unique= True)

    def __str__(self):
        return f'{str(self.location_name)} location of the {self.rack_id} is used.'


class Router(Location):
    routers_id = models.IntegerField(unique= True)
    #size = models.IntegerField()
    
    def __str__(self):
        return "Router ID: " + str(self.routers_id) + "."

class ipv4_network(models.Model):
    name = models.CharField(max_length = 200, unique = True, primary_key = True)
    ip_range = models.CharField(max_length = 200)
    ip_address = models.CharField(max_length = 1000, unique = True, default='192.168.1.0')


    def __str__(self):
        return self.name + "," + self.ip_address

class Switch(Location):
    switchs_id = models.IntegerField(unique= True)
    #rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    #locations = models.OneToOneField(Location, on_delete=models.CASCADE)
    router_id = models.ForeignKey(Router, on_delete=models.CASCADE)
    #size = models.IntegerField()
    network_name = models.ForeignKey(ipv4_network, on_delete=models.CASCADE )

    def __str__(self):
        return "Switch ID: " + str(self.switchs_id)+ "."

class PatchPanel(Location):
    patchpanels_id = models.IntegerField(unique= True)
    #size = models.IntegerField()
    #rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    #locations = models.OneToOneField(Location, on_delete=models.CASCADE)
    switch_id = models.ForeignKey(Switch, on_delete=models.CASCADE)
    number_of_ports = models.IntegerField()

    def __str__(self):
        return "PatchPanel ID: " + str(self.patchpanels_id)+ "."

class Server(Location):
    servers_id = models.IntegerField(unique= True)
    #size = models.IntegerField()
    #rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    #locations = models.OneToOneField(Location, on_delete=models.CASCADE)
    patch_panel_id = models.ForeignKey(PatchPanel, on_delete=models.CASCADE)
    owner = models.CharField(max_length = 200)

    def __str__(self):
        return  "Server ID: " +str(self.servers_id) + "."

class BatteryBackup(Location):
    battery_id = models.IntegerField(unique= True)
    #rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    #locations = models.OneToOneField(Location, on_delete=models.CASCADE)
    #size = models.IntegerField()

    def __str__(self):
        return "Battery Backup ID: " + str(self.battery_id) + "."

class NetworkInterfaceCard(models.Model):
    id = models.IntegerField(primary_key= True, auto_created=True)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    ip_address = models.OneToOneField(ipv4_network, to_field='ip_address', on_delete=models.CASCADE)

    def __str__(self):
        return "Network Interface Card's :: " + str(self.ip_address) + "."
