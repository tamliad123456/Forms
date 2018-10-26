from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=250)
    can_view = models.CharField(max_length=350)
    answer_counter = models.IntegerField()
    form_id = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.CharField(max_length=350)
    question_number = models.IntegerField()

    def __str__(self):
        return self.question

class Ans(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

