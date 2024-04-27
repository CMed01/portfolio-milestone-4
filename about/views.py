from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About, ContactRequest
from .forms import ContactForm

# Create your views here.
def about_page(request):
    about_list = About.objects.filter(status=1).order_by("updated_on")

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
            "about_list": about_list,
            "contact_form": contact_form,
        },
        )

def custom_400(request, exception):
    return render(request,"400.html", status=400)

def custom_403(request, exception):
    return render(request,"403.html", status=403)

def custom_404(request, exception):
    return render(request,"404.html", status=404)
