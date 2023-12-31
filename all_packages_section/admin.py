from django.contrib import admin
from all_packages_section.models import all_package
# Register your models here.
class test(admin.ModelAdmin):
    list_display=('package_name','image','title','description')
admin.site.register(all_package,test)