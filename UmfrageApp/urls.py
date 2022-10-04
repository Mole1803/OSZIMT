from django.urls import path
from .views import SurveysOverviewView, CreateSurveyView, DetailSurveyView  # IndexView, SuccessView, QuestionAdministrationView,

urlpatterns = [

    path("surveys_overview/", SurveysOverviewView.as_view(), name="surveys_overview"),
    path("survey/<str:title>/", DetailSurveyView.as_view(), name="survey"),
    path("create_survey/", CreateSurveyView.as_view(), name="create_survey"),
    #path("survey/<str:survey>/", IndexView.as_view(), name="survey"),
    # path('', IndexView.as_view(), name='index'),
    # path("success/", SuccessView.as_view(), name="success"),
    # path("create_question/", QuestionAdministrationView.as_view(), name="create_question"),
]
