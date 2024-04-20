from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.

def profile_page(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.
    
    **Template**
    :template:`about/about.html`
    """
    userprofile = Profile.objects.all()
    

    return render(
        request,
        "profile.html",
        {
            "userprofile": userprofile,
            },
    )