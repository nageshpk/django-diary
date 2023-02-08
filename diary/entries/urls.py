from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('entry-detail/<str:pk>', views.entryDetail, name='entry-detail'),
    path('create/', views.createEntry, name='create-entry'),
    path('delete/<str:pk>', views.deleteEntry, name='delete-entry'),
    path('edit/<str:pk>', views.editEntry, name='edit-entry'),
]