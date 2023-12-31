from django.contrib import admin
from custom_booking_section.models import booking_data,departure_city,destination_city
# Register your models here.
class test(admin.ModelAdmin):
    list_display=('name','number','departure','destination','travellers','date','amount')
admin.site.register(booking_data,test)


class test1(admin.ModelAdmin):
    list_display=['departure_city']
admin.site.register(departure_city,test1)


class test2(admin.ModelAdmin):
    list_display=['destination_city']
admin.site.register(destination_city,test2)

