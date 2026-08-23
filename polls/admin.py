from django.contrib import admin

# Register your models here.

from .models import Question,Choice

admin.site.register(Question,list_display=['question_text','pub_date'],search_fields=['question_text'])
admin.site.register(Choice,search_fields=['choice_text'])