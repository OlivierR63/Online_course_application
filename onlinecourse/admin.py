from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display=['content']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
