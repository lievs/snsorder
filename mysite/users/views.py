from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm



def register(request):
    print("Inside register view")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("snsorder:index")
    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)