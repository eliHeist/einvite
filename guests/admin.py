from django.contrib import admin

from guests.models import Guest

# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'email')
    list_display = ['name', 'phone', 'email']

admin.site.register(Guest, GuestAdmin)