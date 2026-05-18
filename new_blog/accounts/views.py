from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomSetPasswordForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'registration/password_reset_confirm.html'
    # this is the placeholder token used after the real one is consumed
    reset_url_token = 'set-password'
