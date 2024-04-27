from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
from .forms import ContactForm

# Create your views here.

class AboutList(generic.ListView):
    """
    Returns all about post with a maximum of four displayed in order of creation.
    This allows the super user to modify the content
    in the admin portal
    **Context**

    ``queryset``
        All published instances of :model:`about.About`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`index.html`
    """

    queryset = About.objects.filter(status=1).order_by("updated_on")
    template_name = "index.html"
    paginate_by = 4

def contact_me(request):
    """
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Contact request received! We aim to respond within 2 working days'
            )

    contact_form = ContactForm()

    return render(
        request,
        "index.html",
        {
            "about": about,
            "contact_form": collaborate_form,
            },
        )