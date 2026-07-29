from django.urls import path
from . import views

app_name = 'poles'

urlpatterns = [
    path('immobilier/', views.immobilier, name='immobilier'),
    path('invest/', views.invest, name='invest'),
    path('international/', views.international, name='international'),
    path('mobility/', views.mobility, name='mobility'),
    path('solutions/', views.solutions, name='solutions'),
]
