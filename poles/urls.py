from django.urls import path
from . import views

app_name = 'poles'

urlpatterns = [
    path('', views.list_poles, name='list'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/request/', views.request_service, name='request_service'),
]
