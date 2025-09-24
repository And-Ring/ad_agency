from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import Feedback
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)  # добавляем капчу
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'captcha']
        labels = {
            'name': _("Имя"),
            'email': _("Электронная почта"),
            'message': _("Сообщение"),
        }
        widgets = {
            'name': forms.TextInput(attrs={'size': '20'}),       # ширина поля Имя
            'email': forms.EmailInput(attrs={'size': '20'}),     # ширина поля Email
            'message': forms.Textarea(attrs={'cols': '100', 'rows': '5'}),  # прямоугольное сообщение
        }