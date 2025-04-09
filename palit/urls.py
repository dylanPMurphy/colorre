from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/save/', views.save_scheme, name='save_scheme'),
    path('api/load/<int:scheme_id>/', views.get_scheme, name='get_scheme'),
]