from django.urls import path
from .views import FeedbackCreateView, FeedbackThanksView

app_name = "feedback"

urlpatterns = [
    path('', FeedbackCreateView.as_view(), name='form'),
    path('thanks/', FeedbackThanksView.as_view(), name='thanks'),
]