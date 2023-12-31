from django.contrib import admin
from django.urls import path



from django.conf import settings
from django.conf.urls.static import static
from urllib.parse import quote

from xpedition_tour import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('mainpage', views.home,name="mainpage"),
    path('custom_booking/', views.custom_booking, name='custom_booking'),
    path('details/<test>/', views.details, name="details"),
    path('all_packages/', views.all_packages, name='all_packages'),
    path('payment',views.payment,name="payment"),
    path('payment_view/', views.payment_view, name='payment_view'),
    path('test/',views.test,name="test"),
    
    
    path('game/',views.game,name="game"),
    
    path('childaccess/',views.childaccess,name="childaccess"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('update_status/<int:combined_data_id>/', views.update_status_view, name='update_status_view'),
    # path('users/',views.users,name="users"),


]

# Always serve media files, even when DEBUG is False
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Example of using encoded dynamic value in URL construction
dynamic_value = "Special Package 1/"
encoded_value = quote(dynamic_value)
urlpatterns.append(path(f'details/{encoded_value}/', views.details, name="details"))

# Configure the custom 404 view
handler404 = 'yourapp.views.custom_404_view'


