from django.contrib import admin
from special_packages_section.models import special_package
# Register your models here.

class test(admin.ModelAdmin):
    list_display=('package_url','package_name','image','title','description','days_nights','max_people','location','reviews','price','details')
admin.site.register(special_package,test)