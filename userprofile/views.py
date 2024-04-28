from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, User
from .forms import UpdateProfileForm



@login_required
def view_profile(request):
    """Create profile View

    Returns user details for authenticated user in :model:`username.Profile`
    and displays them in a page 
    
    **Context**

    ``queryset``
        All published instances of :model:`username.Profile`
    ``profile``
        Returns the autenticated user and associated data
        
    **Template:**

    :template:`profile.html`
    """
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, author=request.user)
    profile_form = UpdateProfileForm()
    return render(
        request, 
        'profile.html',
        {
            'profile': profile,
            'profile_form': profile_form,
            },
    )


@login_required
def edit_profile(request, slug):
    """Edit functionaility of profile biograpghy

    Returns profile biography details for authenticated user in :model:`username.Profile`
    and displays them in a pag
    
    **Context**

    ``queryset``
        All published instances of :model:`username.Profile`
    ``profile``
        An instance of :model:`username.Profile`
    ``profile_form``
        An instance of :form:`blog.BlogcommentForm`
        
    **Template:**

    :template:`edit_profile.html`
    """
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, author=request.user)

    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid() and profile.author == request.user:
            profile_form.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                'Profile updated'
                )
            return redirect(to='profile')

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
       

    return render(
        request, 
        'edit_profile.html',
        {
            'profile': profile,
            'profile_form': profile_form,
            },
    )
    