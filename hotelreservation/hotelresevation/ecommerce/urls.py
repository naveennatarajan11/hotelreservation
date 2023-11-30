from . import views
from django.urls import path

app_name = 'ecommerce:login'


urlpatterns = [
    path('register1/',views.register,name='register1'),
    path('login',views.login,name='login')


]