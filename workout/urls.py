from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutList.as_view(), name='workout'),
    path('<slug:slug>/', views.workout_detail, name='workout_detail'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.workout_comment_delete, name='workout_comment_delete'),
]
