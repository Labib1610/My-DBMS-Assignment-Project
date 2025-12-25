from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm, ImportCSVForm, FilterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import csv
import io
from datetime import datetime, timedelta

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

# READ with sorting, filtering, and pagination
@login_required
def student_list(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', '-created_at')
    min_gpa = request.GET.get('min_gpa', '')
    max_gpa = request.GET.get('max_gpa', '')
    performance = request.GET.get('performance', '')
    page_number = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', '10')
    
    students = Student.objects.all()
    
    # Search filter
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    
    # GPA range filter
    if min_gpa:
        students = students.filter(gpa__gte=float(min_gpa))
    if max_gpa:
        students = students.filter(gpa__lte=float(max_gpa))
    
    # Performance filter
    if performance == 'excellent':
        students = students.filter(gpa__gte=3.5)
    elif performance == 'good':
        students = students.filter(gpa__gte=3.0, gpa__lt=3.5)
    elif performance == 'needs_improvement':
        students = students.filter(gpa__lt=3.0)
    
    # Apply sorting
    students = students.order_by(sort_by)
    
    # Calculate statistics
    stats = Student.objects.aggregate(
        total=Count('id'),
        avg_gpa=Avg('gpa'),
        excellent=Count('id', filter=Q(gpa__gte=3.5)),
        good=Count('id', filter=Q(gpa__gte=3.0, gpa__lt=3.5)),
        average=Count('id', filter=Q(gpa__gte=2.0, gpa__lt=3.0)),
        poor=Count('id', filter=Q(gpa__lt=2.0))
    )
    
    # Recent activity
    recent_students = Student.objects.all().order_by('-created_at')[:5]
    recently_updated = Student.objects.all().order_by('-updated_at')[:5]
    
    # Pagination
    paginator = Paginator(students, int(per_page))
    students_page = paginator.get_page(page_number)
    
    context = {
        'students': students_page,
        'query': query,
        'sort_by': sort_by,
        'stats': stats,
        'recent_activity': recent_students,
        'page_obj': students_page,
        'filter_params': f"&q={query}&min_gpa={min_gpa}&max_gpa={max_gpa}&performance={performance}",
        'sort_params': f"&sort={sort_by}",
    }
    
    return render(request, 'student_list.html', context)

# CREATE
@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'title': 'Add New Student'})

# UPDATE
@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
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
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'GPA', 'Date of Birth', 'Enrollment Date'])
    
    students = Student.objects.all().values_list('id', 'first_name', 'last_name', 'email', 'phone', 'gpa', 'date_of_birth', 'enrollment_date')
    for student in students:
        writer.writerow(student)
    
    return response

# IMPORT FROM CSV
@login_required
def import_students_csv(request):
    if request.method == 'POST':
        form = ImportCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a CSV file.')
                return redirect('import_csv')
            
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)
            
            success_count = 0
            error_count = 0
            
            for row in reader:
                try:
                    Student.objects.create(
                        first_name=row.get('first_name', ''),
                        last_name=row.get('last_name', ''),
                        email=row.get('email', ''),
                        phone=row.get('phone', ''),
                        address=row.get('address', ''),
                        gpa=float(row.get('gpa', 0)),
                    )
                    success_count += 1
                except Exception as e:
                    error_count += 1
            
            messages.success(request, f'Successfully imported {success_count} students. {error_count} errors.')
            return redirect('student_list')
    else:
        form = ImportCSVForm()
    
    return render(request, 'import_csv.html', {'form': form})

# BULK DELETE
@login_required
def bulk_delete(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        if student_ids:
            Student.objects.filter(id__in=student_ids).delete()
            messages.success(request, f'Successfully deleted {len(student_ids)} students.')
        else:
            messages.error(request, 'No students selected.')
    return redirect('student_list')

# BULK EXPORT
@login_required
def bulk_export(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        if not student_ids:
            messages.error(request, 'No students selected.')
            return redirect('student_list')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_students.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'GPA'])
        
        students = Student.objects.filter(id__in=student_ids).values_list('id', 'first_name', 'last_name', 'email', 'phone', 'gpa')
        for student in students:
            writer.writerow(student)
        
        return response
    return redirect('student_list')

# SEND EMAIL
@login_required
def send_email_to_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        if not subject or not message:
            messages.error(request, 'Subject and message are required!')
            return render(request, 'send_email.html', {'student': student})
        
        try:
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'nlabibs2003@gmail.com')
            result = send_mail(
                subject,
                message,
                from_email,
                [student.email],
                fail_silently=False,
            )
            if result == 1:
                messages.success(request, f'Email sent successfully to {student.full_name}!')
            else:
                messages.warning(request, 'Email may not have been sent. Check console output.')
        except Exception as e:
            messages.error(request, f'Failed to send email: {str(e)}')
            print(f"Email Error: {str(e)}")  # Print to console for debugging
        
        return redirect('student_detail', id=id)
    
    return render(request, 'send_email.html', {'student': student})

# CHART DATA API
@login_required
def chart_data(request):
    stats = Student.objects.aggregate(
        excellent=Count('id', filter=Q(gpa__gte=3.5)),
        good=Count('id', filter=Q(gpa__gte=3.0, gpa__lt=3.5)),
        average=Count('id', filter=Q(gpa__gte=2.0, gpa__lt=3.0)),
        poor=Count('id', filter=Q(gpa__lt=2.0))
    )
    
    data = {
        'labels': ['Excellent', 'Good', 'Average', 'Poor'],
        'values': [
            stats['excellent'],
            stats['good'],
            stats['average'],
            stats['poor']
        ]
    }
    return JsonResponse(data)

# PRINT VIEW
@login_required
def print_student_list(request):
    students = Student.objects.all().order_by('last_name')
    stats = Student.objects.aggregate(
        total=Count('id'),
        avg_gpa=Avg('gpa'),
        excellent=Count('id', filter=Q(gpa__gte=3.5)),
        good=Count('id', filter=Q(gpa__gte=3.0, gpa__lt=3.5)),
        average=Count('id', filter=Q(gpa__gte=2.0, gpa__lt=3.0)),
        poor=Count('id', filter=Q(gpa__lt=2.0))
    )
    context = {
        'students': students,
        'stats': stats,
        'today': datetime.now().strftime('%B %d, %Y')
    }
    return render(request, 'print_student_list.html', context)

@login_required
def print_student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
        'today': datetime.now().strftime('%B %d, %Y')
    }
    return render(request, 'print_student_detail.html', context)
