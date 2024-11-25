from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('pay/', views.pay),
     path('stk/', views.stk)
]
