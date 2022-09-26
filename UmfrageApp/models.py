import os.path

from django.db import models
import json

# converts the question.json to db
path_ = os.path.dirname(os.path.abspath(__file__))
path_ = os.path.join(path_, "question.json")
f = open(path_)
_dict = {}
json_file = json.load(f)
for key, value in json_file.items():
    _dict[key] = getattr(models, value)(null=True)
f.close()


# end of conversion

class Question(models.Model):
    question_text = models.TextField()
    question_type = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    choice = models.TextField()
    question = models.ForeignKey("Question", on_delete=models.CASCADE)


class UserAnswer(models.Model):
    locals().update(_dict)
