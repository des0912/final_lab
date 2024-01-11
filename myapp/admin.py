from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birth_date", "department"]
    search_fields = ('first_name', 'last_name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "department"]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "enrollment_date"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["student", "email", "phone_number"]