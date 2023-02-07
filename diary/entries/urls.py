from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('entry-detail/<str:pk>', views.entryDetail, name='entry-detail')
]