from django.contrib import admin
from first_api_backend.models import *
# Register your models here
admin.site.register(Location)
admin.site.register(Rack)
admin.site.register(Router)
admin.site.register(ipv4_network)
admin.site.register(Switch)
admin.site.register(PatchPanel)
admin.site.register(Server)
admin.site.register(BatteryBackup)
admin.site.register(NetworkInterfaceCard)
