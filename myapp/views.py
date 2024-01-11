from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Student, Course, Enrollment, Contact
from .forms import DepartmentForm, StudentForm, CourseForm, EnrollmentForm, ContactForm

# Create your views here.
def index(request):
  return render(request, 'index.html')


# def search(request):
#   if request.method == 'POST':
#      searched = request.POST['searched']
#      departments = Department.objects.filter(name__contains=searched)

#      context = {'searched': searched, 'departments': departments}

#      return render(request, 'search.html', context)
#   else:
     
#     return render(request, 'search.html', {})

def department(request):
  department_list = Department.objects.all().order_by('name',)

  context = {'department_list': department_list}
  return render(request, 'department.html', context)

def add_department(request):

  form = DepartmentForm()

  if request.method == "POST":
    form = DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('department')
    
  context = {'form': form}
    
  form = DepartmentForm
  return render(request, 'add_department.html', context)

def edit_department(request, pk):
  department = Department.objects.get(id=pk)
  form = DepartmentForm(instance=department)

  if request.method == 'POST':
    form = DepartmentForm(request.POST, instance=department)

    if form.is_valid():
      form.save()
      return redirect('department')

  context = {'form':form}

  return render(request, 'edit_department.html', context)

def delete_department(request, pk):
	item = get_object_or_404(Department, id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('department')

	context = {'item':item}
	return render(request, 'delete_department.html', context)

def students(request):
  if request.method == 'POST':
     searched = request.POST['searched']
     student_list = Student.objects.filter(first_name__contains=searched)

     context = {'searched': searched, 'student_list': student_list}

     return render(request, 'students.html', context)

  student_list = Student.objects.all()

  context = {'student_list': student_list}

  return render(request, 'students.html', context)

def add_student(request):

  form = StudentForm()

  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('students')
    
  context = {'form': form}
    
  form = DepartmentForm
  return render(request, 'add_student.html', context)


def edit_student(request, pk):
  students = Student.objects.get(id=pk)
  form = StudentForm(instance=students)

  if request.method == 'POST':
    form = StudentForm(request.POST, instance=students)

    if form.is_valid():
      form.save()
      return redirect('students')

  context = {'form':form}

  return render(request, 'edit_student.html', context)

def delete_student(request, pk):
	item = Student.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('students')

	context = {'item':item}
	return render(request, 'delete_student.html', context)


def course(request):
  course_list = Course.objects.all()

  context = {'course_list': course_list}

  return render(request, 'course.html', context)

def add_course(request):
  course = Course.objects.all()

  form = CourseForm()

  if request.method == "POST":
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('course')
    
  context = {'form': form}
    
  form = CourseForm
  return render(request, 'add_course.html', context)

def edit_course(request, pk):
  course = Course.objects.get(id=pk)
  form = CourseForm(instance=course)

  if request.method == 'POST':
    form = CourseForm(request.POST, instance=course)

    if form.is_valid():
      form.save()
      return redirect('course')

  context = {'form':form}

  return render(request, 'edit_course.html', context)

def delete_course(request, pk):
	item = Course.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('course')

	context = {'item':item}
	return render(request, 'delete_course.html', context)


def enrollment(request):
  enrollment_list = Enrollment.objects.all()

  context = {'enrollment_list': enrollment_list}

  return render(request, 'enrollment.html', context)

def add_enrollment(request):
  enrollment = Enrollment.objects.all()

  form = EnrollmentForm()

  if request.method == "POST":
    form = EnrollmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('enrollment')
    
  context = {'form': form}
    
  form = EnrollmentForm
  return render(request, 'add_enrollment.html', context)

def edit_enrollment(request, pk):
  enrollment = Enrollment.objects.get(id=pk)
  form = EnrollmentForm(instance=enrollment)

  if request.method == 'POST':
    form = EnrollmentForm(request.POST, instance=enrollment)

    if form.is_valid():
      form.save()
      return redirect('enrollment')

  context = {'form':form}

  return render(request, 'edit_enrollment.html', context)

def delete_enrollment(request, pk):
	item = Enrollment.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('enrollment')

	context = {'item':item}
	return render(request, 'delete_enrollment.html', context)



def contact(request):
  contact_list = Contact.objects.all()

  context = {'contact_list': contact_list}

  return render(request, 'contact.html', context)

def add_contact(request):
  contact = Contact.objects.all()

  form = ContactForm()

  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contact')
    
  context = {'form': form}
    
  form = ContactForm
  return render(request, 'add_contact.html', context)

def edit_contact(request, pk):
  contact = Contact.objects.get(id=pk)
  form = ContactForm(instance=contact)

  if request.method == 'POST':
    form = ContactForm(request.POST, instance=contact)

    if form.is_valid():
      form.save()
      return redirect('contact')

  context = {'form':form}

  return render(request, 'edit_contact.html', context)

def delete_contact(request, pk):
	item = Contact.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('contact')

	context = {'item':item}
	return render(request, 'delete_contact.html', context)
