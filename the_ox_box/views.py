from django.views import generic

def custom_400(request, exception):
    return render(request,"400.html", status=400)

def custom_403(request, exception):
    return render(request,"403.html", status=403)

def custom_404(request, exception):
    return render(request,"404.html", status=404)