from django.urls import path
from . import views

app_name = 'taskapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('details/', views.dataview, name='details'),
    path('logout/', views.logout, name='logout'),
    path('getbranch', views.load_branches, name='ajax_load_branches')
]
