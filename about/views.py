from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About, ContactRequest
from .forms import ContactForm


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
