from django.contrib import admin
from .models import CallMe, Repair, Other, Objects, Image

admin.site.register(CallMe)
admin.site.register(Repair)
admin.site.register(Other)
admin.site.register(Objects)
admin.site.register(Image)