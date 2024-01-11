from django import forms 
from django.forms import ModelForm
from .models import Department, Student, Course, Enrollment, Contact

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentForm(ModelForm):
  class Meta:
    model = Student
    fields = ('first_name', 'last_name', 'birth_date', 'department')

    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
        }
    
class CourseForm(ModelForm):
  class Meta:
    model = Course
    fields = "__all__"

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'department': forms.Select(attrs={'class': 'form-select'}),
    }

class EnrollmentForm(ModelForm):
  class Meta:
    model = Enrollment
    fields = ('student', 'course', 'enrollment_date')

    widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),  # Fix the typo here
            'enrollment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"


    widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # Fix the typo here
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }