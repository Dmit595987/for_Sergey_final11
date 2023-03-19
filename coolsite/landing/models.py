from django.db import models
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)
    email_client = models.EmailField(blank=True)
    phone = models.CharField(max_length=11)
    comment_client = models.TextField(blank=True)

    def __str__(self):
        return f'Сергей к вам обратился - {self.name}, Телефон - {self.phone}'

    def send_email(self):
        subject = f'Поступило обращение от {self.name} телефон - {self.phone}'
        if self.comment_client:
            message = f'Клиент с именем: {self.name} - Его телефон: {self.phone} Его комментарий: {self.comment_client} Мыло: {self.email_client}'
        else:
            message = f'Клиент с именем {self.name} - Его телефон {self.phone} Комментарий ПУСТОЙ, Мыло: {self.email_client}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['neodisco@mail.ru'],
            fail_silently=False,
        )

