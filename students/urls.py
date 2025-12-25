from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth Routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # App Routes
    path('', views.student_list, name='student_list'),
    path('new/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('detail/<int:id>/', views.student_detail, name='student_detail'),
    
    # Export/Import
    path('export/', views.export_students_csv, name='export_csv'),
    path('import/', views.import_students_csv, name='import_csv'),
    
    # Bulk Operations
    path('bulk-delete/', views.bulk_delete, name='bulk_delete'),
    path('bulk-export/', views.bulk_export, name='bulk_export'),
    
    # Email
    path('send-email/<int:id>/', views.send_email_to_student, name='send_email'),
    
    # API
    path('api/chart-data/', views.chart_data, name='chart_data'),
    
    # Print
    path('print/', views.print_student_list, name='print_student_list'),
    path('print/<int:id>/', views.print_student_detail, name='print_student_detail'),
]