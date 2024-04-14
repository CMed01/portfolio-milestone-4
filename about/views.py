from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About, Header

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