from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Feedback
from .forms import FeedbackForm
from django.utils.translation import gettext_lazy as _

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback/feedback_form.html"
    success_url = reverse_lazy('feedback:thanks')

# Страница спасибо
from django.views.generic import TemplateView

class FeedbackThanksView(TemplateView):
    template_name = "feedback/thanks.html"
