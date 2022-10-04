import os.path

from django.db import models
import json


# converts the question.json to db

class Surveys(models.Model):
    title = models.TextField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Questions(models.Model):
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    question_text = models.TextField()
    html_representation = models.CharField(max_length=15)

    def __str__(self):
        return self.question_text


class AnswerChoices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_choice = models.ForeignKey(AnswerChoices, on_delete=models.CASCADE)


class Interviewees(models.Model):
    date = models.DateTimeField(auto_now_add=True)
