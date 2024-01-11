from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('department', views.department, name='department'),
    path('add_department', views.add_department, name='add-department'),
    path('edit_department/<str:pk>/', views.edit_department, name="edit-department"),
    path('delete_department/<str:pk>/', views.delete_department, name="delete-department"),
    path('students/', views.students, name="students"),
    path('add_student', views.add_student, name='add-student'),
    path('edit_student/<str:pk>/', views.edit_student, name="edit-student"),
    path('delete_student/<str:pk>/', views.delete_student, name="delete-student"),
    path('course', views.course, name='course'),
    path('add_course', views.add_course, name='add-course'),
    path('edit_course/<str:pk>/', views.edit_course, name="edit-course"),
    path('delete_course/<str:pk>/', views.delete_course, name="delete-course"),

    path('enrollment', views.enrollment, name='enrollment'),
    path('add_enrollment', views.add_enrollment, name='add-enrollment'),
    path('edit_enrollment/<str:pk>/', views.edit_enrollment, name="edit-enrollment"),
    path('delete_enrollment/<str:pk>/', views.delete_enrollment, name="delete-enrollment"),

    path('contact', views.contact, name='contact'),
    path('add_contact', views.add_contact, name='add-contact'),
    path('edit_contact/<str:pk>/', views.edit_contact, name="edit-contact"),
    path('delete_contact/<str:pk>/', views.delete_contact, name="delete-contact"),
]