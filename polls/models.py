from django.db import models
from django.utils import timezone

import datetime


# Create your models here.
class Question(models.Model):
    # You should add __str__() methods to your class
    # as it helps to identify the objects when debugging
    # and is used in djangos auto gen'd admin.
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        '''
        Method to check if the question was published recently
        i.e. in the last day
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
