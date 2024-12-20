from django.contrib import admin

from django.contrib import admin
from polls.models import TemplateCard, GeneratedCard

# Register your models here.

admin.site.register(TemplateCard)
admin.site.register(GeneratedCard)