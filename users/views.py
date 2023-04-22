from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User

# Create your views here.


class UserLoginView(LoginView):
    """ Class for login user """
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """ Class for user registration """
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы зарегестрировались'
    title = 'Регистрация'


class UserProfileView(LoginRequiredMixin, TitleMixin, UpdateView):
    """ Class for rendering user-profile templates and change user info on profile templates """
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Личный кабинет'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id, ))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verify = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
