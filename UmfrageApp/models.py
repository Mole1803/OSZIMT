from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    question_type = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    choice = models.TextField()
    question = models.ForeignKey("Question", on_delete=models.CASCADE)


_dict = {
    'question_1': models.TextField(),
    'question_2': models.TextField()
}


class UserAnswer(models.Model):
    locals().update(_dict)
