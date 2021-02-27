from django.contrib import admin

# Register your models here.

from lesson1.models import Student, Course

admin.site.register(Student)
admin.site.register(Course)
