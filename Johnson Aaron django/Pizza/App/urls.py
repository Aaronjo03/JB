from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('customer_info/<int:pizza_id>/', views.customer_info, name='customer_info'),
  path('confirmation/<int:pizza_id>/<int:customer_id>/', views.confirmation, name='confirmation'),

  
]