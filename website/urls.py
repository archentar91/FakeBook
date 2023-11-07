from django.urls import path
from django.conf import settings
from. import views
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('user/profile/', views.profile_user, name='profile'),
    path('user/change_password/', views.change_password_user, name='change_password'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('api/register_check_password/', views.register_check_password, name='register_check_password'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)