from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, User
from .forms import ProfileForm
from django.contrib import messages


@login_required
def view_profile(request):
    """
    """
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, author=request.user)
    profile_form = ProfileForm()
    return render(
        request, 
        'profile.html',
        {
            'profile': profile,
            'profile_form': profile_form,
            },
    )


@login_required
def edit_profile(request):
    """
    """
    profile = request.user.profile

    if request.method == 'POST':
        profile = get_object_or_404(Profile, pk=profile_id)
        profile_form = ProfileForm(data=request.POST, instance=profile)
        if profile_form.is_valid() and profile.author == request.user:
            profile = profile_form.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                'Profile updated'
                )
        else:
            messages.add_message(
            request, 
            messages.ERROR, 
            'Error updating profile!'
            )

    return HttpResponseRedirect(reverse('profile',args=[slug])) 
    