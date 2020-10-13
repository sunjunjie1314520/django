from django.contrib import admin

from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'phone', 'address', 'house', 'label')
    list_display_links = ['id', 'name']