from django.contrib import admin
from .models import TGUsers, Group, Lesson, Result, Test, Topic


admin.site.register(TGUsers)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Result)
admin.site.register(Test)
admin.site.register(Topic)

