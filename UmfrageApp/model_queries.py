from UmfrageApp.models import Questions, Answers, AnswerChoices, Surveys, Interviewees
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder


def create_survey(survey_json):
    """Creates a full survey from a json
    See json_templates/create_survey.json for an example.
    """
    survey = survey_json
    survey_id = add_survey(survey["title"], survey["description"])
    for question in survey["questions"].values():
        question_id = add_question(question["question"], question["html_representation"], survey_id)
        for answer_choice in question["answer_choices"].values():
            add_answer_choice(answer_choice, question_id)


def add_survey(title, description):
    """Adds a survey to the database
    :param title: The title of the survey
    :param description: The description of the survey"""
    new_survey = Surveys(title=title, description=description)
    new_survey.save()
    return new_survey.id


def add_question(question_text, html_representation, survey_id):
    """Adds a question to the database
    :param question_text: The text of the question
    :param html_representation: The html representation of the question
    :param survey_id: The id of the survey the question belongs to foreign key"""
    new_question = Questions(question_text=question_text, html_representation=html_representation, survey_id=survey_id)
    new_question.save()
    return new_question.id


def add_answer_choice(answer_text, question_id):
    """Adds an answer choice to the database
    :param answer_text: The text of the answer choice
    :param question_id: The id of the question the answer choice belongs to foreign key"""
    new_answer_choice = AnswerChoices(answer_text=answer_text, question_id=question_id)
    new_answer_choice.save()
    return new_answer_choice.id


# get-----------------------------------------------------------------------------------------------------------------

def get_all_surveys():
    surveys = Surveys.objects.all()
    return surveys


def get_questions(survey_id=None):
    questions = Questions.objects.all()
    return questions

# def get_questions():
#    return
#    question_query = Question.objects.all()  # .values("question_text", "question_type")
#    # question_json = json.dumps(list(question_query), cls=DjangoJSONEncoder)
#    return question_query


# def create_question(text="", question_type="text", choices=None):
#    return
#    new_question = Question(question_text=text, question_type=question_type)
#    new_question.save()
#
#
# def add_answer(**kwargs):
#    return
#    new_answer = UserAnswer(**kwargs)
#    new_answer.save()
