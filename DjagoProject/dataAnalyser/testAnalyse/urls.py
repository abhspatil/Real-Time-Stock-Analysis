from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addNotifyUsers', views.addNotifyUsers, name='addNotifyUsers'),
    path('sendNotifyUsers',views.sendNotifyUsers,name='sendNotifyUsers'),
]