from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='companies'),
    path('<int:company_id>', views.company, name='company'),
    path('search', views.search, name='search'),
]
