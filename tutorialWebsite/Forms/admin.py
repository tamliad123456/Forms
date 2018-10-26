from django.contrib import admin
from .models import Question, Form, Ans
# Register your models here.

admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Ans)


