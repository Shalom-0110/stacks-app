from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from loguru import logger


class LoginForm(AuthenticationForm):
    error_css_class = "is-invalid"
    error_messages = {
        "invalid_login": (
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": "Your account has been disabled.",
    }

    username = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "autofocus": "true",
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
            }
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Password", "class": "form-control"}
        )
        self.fields["username"].label = "Email"

    def clean(self):
        super_clean = super(LoginForm, self).clean()
        email = super_clean.get("username")
        if email and email.endswith((".ru", ".cn")):
            logger.warning("RU/CN login attempt blocked.")
            raise ValidationError(
                "Invalid email address: Please check the format.",
                code="invalid",
                params={"email": email},
            )
        user = self.get_user()
        if user.usermetadata.tenant.gsuite_domain:
            raise ValidationError(
                "Please use your organisation Single Sign-on."
            )
        return super_clean
