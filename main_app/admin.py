from django.contrib import admin
from .models import Finch, Feeding, Study

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Study)
