from django.contrib import admin
from .models import Student, Marks
# Register your models here.

admin.site.register(Marks)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'marks_in_maths',)

    def student_name(self, obj):
        return obj.name

    def marks_in_maths(self, obj):
        if obj.marks_set.filter(subject='Maths').exists():
            return obj.marks_set.filter(subject='Maths')[0].marks
        else:
            return None

    student_name.short_description = 'Name'
    marks_in_maths.short_description = 'Maths'
