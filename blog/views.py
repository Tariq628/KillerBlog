from django.shortcuts import render
from .models import Contact
from .forms import ContactFrom
# Create your views here.
def index(request):
    return render(request, "blog/index.html")
def contact(request):
    thank = False
    form = ContactFrom()
    # print(form)
    if request.method == "POST":
        name = request.POST.get("name", "default")
        phone = request.POST.get("phone", "default")
        email = request.POST.get("email", "default")
        textarea = request.POST.get("textarea", "default")
        contact = Contact(name=name, phone=phone, email=email, textarea=textarea)
        contact.save()
        thank = True
    return render(request, "blog/contact.html", {"thank":thank, "form":form})
def search(request):
    return render(request, "blog/search.html")
def blogpost(request):
    return render(request, "blog/blogpost.html")