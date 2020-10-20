from django.contrib import admin

from .models import Bill

@admin.register(Bill)
class BilleAdmin(admin.ModelAdmin):
    list_display = ('id', 'curr_date', 'price', 'remarks', 'create_time')
    list_display_links = ['id','price']