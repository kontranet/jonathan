from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='persons'),
    path('<int:person_id>', views.person, name='person'),
    path('search', views.search, name='search'),
]
