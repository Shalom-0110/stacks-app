from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class StacksLoginView(LoginView):
    template_name = "expense/login.html"
    redirect_authenticated_user = True


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "expense/home.html"


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "expense/signup.html", {"form": form})
