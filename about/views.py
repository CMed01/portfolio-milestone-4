from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Header

# Create your views here.

def header_content(request):
    header = Header.objects.all().order_by("updated_on").first()

    return redner(
        request,
        "index.html",
        {
            "title": title,
            "sub_title": sub_title,
        },
    )