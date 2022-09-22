from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.views import View

from UmfrageApp.models import UserAnswer

html_index = loader.get_template('index.html')

class IndexView(View):
    def get(self, request):
        query_answer = UserAnswer.objects.filter(id=1).all().values("column_1")
        return HttpResponse(html_index.render({"query": query_answer}, request))


