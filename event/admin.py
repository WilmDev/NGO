from django.contrib import admin
from event.models import Event

# Register your models here.
admin.site.register(Event)
admin.site.site_title = 'NGO. Non-Profit Org'
admin.site.site_header = 'NGO'