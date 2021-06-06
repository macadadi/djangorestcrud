
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('api/',views.tasks),
    path('api/<int:pk>/',views.task_details)
]
