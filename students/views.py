from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg, Count
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
import csv

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('student_list')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# READ with sorting and statistics
@login_required
def student_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'id')
    
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        students = Student.objects.all()
    
    # Apply sorting
    if sort_by == 'first_name':
        students = students.order_by('first_name')
    elif sort_by == '-first_name':
        students = students.order_by('-first_name')
    elif sort_by == 'last_name':
        students = students.order_by('last_name')
    elif sort_by == '-last_name':
        students = students.order_by('-last_name')
    elif sort_by == 'email':
        students = students.order_by('email')
    elif sort_by == '-email':
        students = students.order_by('-email')
    elif sort_by == 'gpa':
        students = students.order_by('gpa')
    elif sort_by == '-gpa':
        students = students.order_by('-gpa')
    
    # Calculate statistics
    stats = Student.objects.aggregate(
        total=Count('id'),
        avg_gpa=Avg('gpa'),
        excellent=Count('id', filter=Q(gpa__gte=3.5)),
        good=Count('id', filter=Q(gpa__gte=3.0, gpa__lt=3.5)),
        needs_improvement=Count('id', filter=Q(gpa__lt=3.0))
    )
    
    context = {
        'students': students,
        'query': query,
        'sort_by': sort_by,
        'stats': stats
    }
    
    return render(request, 'student_list.html', context)

# CREATE
@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form, 'title': 'Add New Student'})

# UPDATE
@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form, 'title': 'Edit Student'})

# DELETE
@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.error(request, 'Student deleted successfully.')
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

# DETAIL VIEW
@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})

# EXPORT TO CSV
@login_required
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'GPA'])
    
    students = Student.objects.all().values_list('id', 'first_name', 'last_name', 'email', 'gpa')
    for student in students:
        writer.writerow(student)
    
    messages.success(request, 'Student data exported successfully!')
    return response
