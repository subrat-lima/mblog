from django.shortcuts import redirect, render

from accounts.forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_success")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def register_success(request):
    return render(request, "registration/register_success.html")
