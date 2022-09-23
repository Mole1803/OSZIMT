from UmfrageApp.models import Question, Choices
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

def get_questions():
    question_query = Question.objects.all()#.values("question_text", "question_type")
    #question_json = json.dumps(list(question_query), cls=DjangoJSONEncoder)
    return question_query


def create_question(text="", type="text", choices=None):
    new_question = Question(question_text=text, question_type=type)
    new_question.save()
