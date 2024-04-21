from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Profile, User
from django.contrib import messages

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

# def edit_profile(request):
#     profile = request.user.profile

#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, instance=profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'edit_profile.html', {'form': form})   