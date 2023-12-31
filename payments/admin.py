from django import forms
from django.contrib import admin
from .models import CombinedData


class CombinedDataAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'package_names_string','package_price_string','date_time','nationality','cnic','phone','no_of_travellers', 'account_name', 'account_number', 'image', 'total_amount','status')

admin.site.register(CombinedData, CombinedDataAdmin)




