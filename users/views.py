import random

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.services import send_code_email, send_new_password
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        obj = form.save()
        obj.is_active = False
        obj.save()
        send_code_email(obj)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification_user(request, user_pk):
    """Верификация почты, после прохождения по ссылке перенаправляет на личные данные"""
    user = get_object_or_404(User, pk=user_pk)
    user.is_active = True
    user.save()
    login(request, user)
    return redirect(reverse('users:profile'))


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(10)])

    request.user.set_password(new_password)
    request.user.save()
    send_new_password(email=request.user.email, new_password=new_password)
    return redirect(reverse('users:profile'))
