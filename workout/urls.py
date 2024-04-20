from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutList.as_view(), name='workout'),
]