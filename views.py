from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.decorators import action

from expense.forms import LoginForm


class AuthMixin:
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthMixin, self).dispatch(  # noqa
            request, *args, **kwargs
        )


class DownloadMixin:
    def pre_download_method(self, instance):
        """Override in child class"""
        pass

    def post_download_method(self, instance):
        """Override in child class"""
        pass

    @action(methods=["GET"], detail=True)
    def download(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(
            instance.create_for_sending(request),
            content_type="application/pdf",
        )
        response["Content-Disposition"] = f"filename={instance.pdf_name()}.pdf"
        return response


class Login(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = "expense/login.html"


class Home(AuthMixin, TemplateView):
    template_name = "expense/home.html"


class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGIN_URL)
