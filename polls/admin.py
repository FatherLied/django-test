from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

# class ChoiceInline(admin.StackedInline):		# Wide
class ChoiceInline(admin.TabularInline):		# More Compact
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']		# Enables filtering

    search_fields = ['question_text']	# Enables search

    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

### Simple way of adding choices ###
# admin.site.register(Choice)