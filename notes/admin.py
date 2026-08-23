from django.contrib import admin

# Register your models here.
from .models import Note

admin.site.register(Note,search_fields=['title','body'],list_display=['title','body','created_at'])
