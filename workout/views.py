from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Workout, WorkoutComment
from .forms import WorkoutcommentForm

# Create your views here.

class WorkoutList(LoginRequiredMixin,generic.ListView):
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
    queryset = Workout.objects.filter(status=1).order_by("-created_on")
    template_name = "workout.html"
    paginate_by = 6

@login_required
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
    if request.user.is_authenticated:
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
    else:
        return render (
            request,
            'account/signup.html',
        )

@login_required
def workout_comment_delete(request, slug, comment_id):
    """
    View to delete blog comments
    """
    queryset = Workout.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    workout_comment = get_object_or_404(WorkoutComment, pk=comment_id)
    
    if workout_comment.author == request.user:
        workout_comment.delete()
        messages.add_message(
            request, 
            messages.SUCCESS, 
            "Comment deleted!"
            )
    else:
        messages.add_message(
            request, 
            messages.ERROR, 
            "You can only delete yout own comments!"
            )
    return HttpResponseRedirect(reverse('workout_detail',args=[slug]))