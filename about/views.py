from django.shortcuts import render
from django.views import generic
from .models import About, Header

# Create your views here.

def index(request):
    """
    Renders landing page content for title
    """
    header = Header.objects.all().order_by("updated_on").first()
    return render(
        request,
        "index.html",
        {
            "header": header,
        },
    )