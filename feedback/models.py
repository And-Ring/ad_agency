from django.db import models
from django.utils.translation import gettext_lazy as _

class Feedback(models.Model):
    name = models.CharField(_("Имя"), max_length=100)
    email = models.EmailField(_("Электронная почта"))
    message = models.TextField(_("Сообщение"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
