from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('people', views.people, name='people'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:pk>', views.edit_todo, name='edit_todo')
]