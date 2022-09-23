from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from .model_queries import get_questions, create_question

html_index = loader.get_template('index.html')
html_question_administration = loader.get_template("question_administration.html")


class IndexView(View):
    def get(self, request):
        questions = get_questions()
        return HttpResponse(html_index.render({"data": questions}, request))


class SuccessView(View):
    def get(self, request):
        return HttpResponse("Thank you for taking part in our survey")

    def post(self, request):
        return HttpResponse("Thank you for taking part in our survey. POST")


class QuestionAdministrationView(View):
    def get(self, request):
        return HttpResponse(html_question_administration.render({}, request))

    def post(self, request):
        print(request.POST["question"])
        print(request.POST["question_type"])
        create_question(request.POST["question"], request.POST["question_type"])
        return HttpResponse("Successfully created question!")
