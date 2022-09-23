from django.urls import path
from .views import IndexView, SuccessView, QuestionAdministrationView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("success/", SuccessView.as_view(), name="success"),
    path("create_question/", QuestionAdministrationView.as_view(), name="create_question"),
]