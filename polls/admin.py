from django.contrib import admin

# Register your models here.
from .models import Choice, Question


# You can change admin.TabularInline to
# admin.StackedInline if you want to instead
# have inputs stacked
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# The simply renders pub_date
# before question_text ( old change )
class QuestionAdminOld(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


# This splits the admin section into groups
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date']}), ]

    inlines = [ChoiceInline]

    # Note the addition of the function, `was_published_recently`
    # the `list_display` shows how the list of data will be rendered,
    # i.e. which columns will be shown.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # This adds a filter to the page, allowing you to filter by
    # this field/ these listed fields
    list_filter = ['pub_date']

    # Adding this allows for searching of the list fields
    search_fields = ['question_text']


# You'll follow this pattern when you want to customize
# Django admin.
admin.site.register(Question, QuestionAdmin)
# This is in-efficient to add a choice, but technically works fine.
# Refer to the addition of the above class ChoiceInline to the
# QuestionAdmin class
# admin.site.register(Choice)
