from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Workout, WorkoutComment
from .forms import WorkoutcommentForm

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

    :template:`workout/workout.html`
    """
    queryset = Workout.objects.filter(status=1).order_by("created_on")
    template_name = "workout.html"
    paginate_by = 6

def workout_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
        """

    queryset = Workout.objects.filter(status=1)
    workout = get_object_or_404(queryset, slug=slug)

    workoutcomments = workout.workout_comments.all().order_by("-created_on")

    if request.method == "POST":
        workout_form = WorkoutcommentForm(data=request.POST)
        if workout_form.is_valid():
            workout_post = workout_form.save(commit=False)
            workout_post.author = request.user
            workout_post.post = workout
            workout_post.save()
            messages.add_message(
                request, messages.SUCCESS,'Score submitted and awaiting approval'
                )

    workout_form = WorkoutcommentForm()

    return render(
        request,
        "workout_detail.html",
        {
            "workout": workout,
            "workoutcomments": workoutcomments,
            "workout_form": workout_form,
            },
    )