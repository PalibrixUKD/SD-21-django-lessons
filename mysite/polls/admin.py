from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
admin.site.register(Choice)


class ChoicesInline(admin.StackedInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline,]


admin.site.register(Question, QuestionAdmin)

