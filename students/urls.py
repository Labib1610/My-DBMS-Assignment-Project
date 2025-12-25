from django.urls import path
from django.contrib.auth import views as auth_views # <--- Import this
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
    path('export/', views.export_students_csv, name='export_csv'),
]