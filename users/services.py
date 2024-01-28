from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from config import settings
from users.models import User


def send_code_email(user: User):
    """Отправляет ссылку для подтверждения почты"""
    verification_url = reverse('users:verification', kwargs={
                               'user_pk': user.pk, 'verification_code': user.verification_code})
    full_url = f'http://localhost:8000{verification_url}'

    send_mail(
        'Подтверждение почты',
        f'Чтобы подтвердить почту, перейдите по этой ссылке {full_url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )


def send_new_password(email, new_password):
    send_mail(
        'Вы сменили пароль!',
        f'Ваш новый пароль: {new_password}',
        settings.EMAIL_HOST_USER,
        [email]
    )
