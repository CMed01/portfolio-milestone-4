from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Workout, WorkoutComment

# Create your views here.

class WorkoutList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    queryset = Workout.objects.filter(status=1).order_by("created_on")
    template_name = "workout.html"
    paginate_by = 6