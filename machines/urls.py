from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='machines'),
    path('<int:machine_id>', views.machine, name='machine'),
    path('m_search', views.m_search, name='m_search'),
]
