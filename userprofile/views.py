from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Profile, User

# Create your views here.

def view_profile(request):

    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, author=request.user)
    return render(
        request, 
        'profile.html',
        {
            'profile': profile,
            },
    )