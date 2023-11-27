
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('user_logout', views.user_logout, name='user_logout'),

    # CRUD
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_record', views.create_record, name='create_record'),

]
