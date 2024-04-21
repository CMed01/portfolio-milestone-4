from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutList.as_view(), name='workout'),
    path('<slug:slug>/', views.workout_detail, name='workout_detail'),
]