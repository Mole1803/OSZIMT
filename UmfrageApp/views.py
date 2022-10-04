from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from .model_queries import get_questions, get_all_surveys, create_survey

html_index = loader.get_template('index.html')
html_question_administration = loader.get_template("question_administration.html")
html_survey_overview = loader.get_template("survey_overview.html")
html_create_survey = loader.get_template("create_survey.html")


# class IndexView(View):
#    def get(self, request, survey):
#        questions = get_questions(survey)
#        return HttpResponse(html_index.render({"data": questions}, request))
#
#
# class SuccessView(View):
#    def get(self, request):
#        return HttpResponse("Thank you for taking part in our survey")
#
#    def post(self, request):
#        # print(request.POST[0])
#        dict_ = {
#            "question_1": request.POST["0"],
#            "question_2": request.POST["1"],
#        }
#        add_answer(**dict_)
#        return HttpResponse("Thank you for taking part in our survey. POST")
#
#
# class QuestionAdministrationView(View):
#    def get(self, request):
#        return HttpResponse(html_question_administration.render({}, request))
#
#    def post(self, request):
#        create_question(request.POST["question"], request.POST["question_type"])
#        return HttpResponse("Successfully created question!")


class DetailSurveyView(View):
    def get(self, request, title):
        """A detail view of a single survey"""
        print(title)
        survey = get_all_surveys().filter(title=title).first()
        return HttpResponse(survey.id)


class SurveysOverviewView(View):
    def get(self, request):
        """All surveys in a table"""
        all_surveys = get_all_surveys()
        return HttpResponse(html_survey_overview.render({"surveys": all_surveys}, request))



class CreateSurveyView(View):
    def get(self, request):
        """Loads the create survey page"""
        return HttpResponse(html_create_survey.render({}, request))

    def post(self, request):
        """Creates a new survey"""
        print(request.POST)
        #TODO create survey from json
        #create_survey(request.POST)
        return HttpResponse("Successfully created survey!")
