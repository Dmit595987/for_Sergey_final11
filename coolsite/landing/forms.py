
from django import forms
from django.core.exceptions import ValidationError

from .models import *


class Clients_phone(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email_client', 'phone',  'comment_client']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Имя"}),
            'email_client': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Контактный телефон"}),
            # 'date_meeting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Дата мероприятия"}),
            # 'place_meeting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Место проведения"}),
            # 'topic_meeting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Тема мероприятия"}),
            'comment_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Комментарий"}),

        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone[0] == '+':
            if not all([item.isdigit() for item in phone[1:]]):
                raise ValidationError('Номер телефона может состоять только из цифр!')
        else:
            if not all([item.isdigit() for item in phone]):
                raise ValidationError('Номер телефона может состоять только из цифр!')

        return phone

    def clean_comment_client(self):
        comment_client = self.cleaned_data['comment_client']
        if len(comment_client) > 201:
            raise ValidationError('Длина коментрия не может превышать 200 символов!')
        return comment_client

    def save(self, commit=True):
        user = super().save(commit=True)
        user.send_email()
        return user



