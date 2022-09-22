from django.db import models


# Create your models here.



class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


_dict = {
    'column_1': models.IntegerField(),
    'column_2': models.IntegerField()
}


class UserAnswer(models.Model):
    locals().update(_dict)
