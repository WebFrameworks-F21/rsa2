from django.db import models

# Create your models here.
class Rack(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    size = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return "Rack ID: " + str(self.id) + "\n" + "Rack Location: " + self.location + "\n"

class Router(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    size = models.IntegerField()

    def __str__(self):
        return "Router ID: " + str(self.id) + "\n"

class ipv4_network(models.Model):
    #id = models.IntegerField(primary_key = True, auto_created = True)
    name = models.CharField(max_length = 200, unique = True, primary_key = True)
    ip_range = models.CharField(max_length = 200)

    def __str__(self):
        return "Name: " + self.name + "\n" + "IP Range: " + self.ip_range + "\n"

class Switch(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    router_id = models.ForeignKey(Router, on_delete=models.CASCADE)
    size = models.IntegerField()
    network_name = models.ForeignKey(ipv4_network, on_delete=models.CASCADE )

    def __str__(self):
        return "Switch ID: " + str(self.id) + "\n"

class PatchPanel(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    size = models.IntegerField()
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    switch_id = models.ForeignKey(Switch, on_delete=models.CASCADE)
    number_of_ports = models.IntegerField()

    def __str__(self):
        return "Patch Panel ID: " + str(self.id) + "\n"

class Server(models.Model):
    id = models.IntegerField(primary_key= True, auto_created=True)
    size = models.IntegerField()
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    patch_panel_id = models.ForeignKey(PatchPanel, on_delete=models.CASCADE)
    owner = models.CharField(max_length = 200)

    def __str__(self):
        return "Server ID: " + str(self.id) + "\n"

class BatteryBackup(models.Model):
    id = models.IntegerField(primary_key= True, auto_created=True)
    rack_id = models.ForeignKey(Rack, on_delete=models.CASCADE)
    size = models.IntegerField()

    def __str__(self):
        return "Battery Backup ID: " + str(self.id) + "\n"

class NetworkInterfaceCard(models.Model):
    id = models.IntegerField(primary_key= True, auto_created=True)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length = 1000, unique = True)

    def __str__(self):
        return "Network Interface Card's IP Address: " + self.ip_address + "\n"
