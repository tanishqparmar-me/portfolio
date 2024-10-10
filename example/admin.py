from django.contrib import admin
from . models import contact_us

class display_contacts(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(contact_us, display_contacts)