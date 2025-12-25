# Student Management System - Django & MySQL

> **A comprehensive web-based CRUD application demonstrating database integration and user authentication**

[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Database Configuration](#-database-configuration)
- [Running the Application](#-running-the-application)
- [Project Components](#-project-components)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## 📖 Project Overview

This is a **Student Management System** developed as part of the **Database Management Systems Laboratory** course. The application demonstrates the practical implementation of database concepts through a full-stack web application that manages student records with complete CRUD (Create, Read, Update, Delete) functionality.

### Course Information
- **Course:** CSE 3522 - Database Management Systems Laboratory
- **Institution:** UIU (United International University)
- **Semester:** Fall 2025
- **Project Type:** Mid-term Assignment

### Key Learning Objectives
- Understand Django ORM and database connectivity
- Implement user authentication and authorization
- Design and execute CRUD operations
- Apply database constraints and data integrity rules
- Build responsive user interfaces with Bootstrap
- Manage database migrations and schema changes

---

## ✨ Features

### Core Functionality
- ✅ **User Authentication System**
  - Secure user registration with password validation
  - Beautiful login/logout pages with modern design
  - Session management
  - Protected routes with `@login_required` decorator

- ✅ **Student Management (CRUD Operations)**
  - **Create:** Add new student records with validation
  - **Read:** View all students in a responsive table with sorting
  - **Update:** Edit existing student information
  - **Delete:** Remove student records with confirmation modal
  - **Detail View:** View comprehensive student information

- ✅ **Advanced Features**
  - **Real-time Search:** Multi-field search (First Name, Last Name, Email)
  - **Column Sorting:** Sort by any column (ascending/descending)
  - **Statistics Dashboard:** View total students, average GPA, performance breakdown
  - **Export to CSV:** Download all student data in CSV format
  - **Color-coded GPA badges:** Visual indicators (Green: ≥3.5, Yellow: ≥3.0, Red: <3.0)

- ✅ **Data Validation & Integrity**
  - Email uniqueness constraint
  - GPA decimal validation (0.00 - 4.00)
  - Required field validation
  - Form-level and model-level validation

- ✅ **Beautiful User Interface**
  - Modern gradient-based design with custom CSS
  - Smooth animations and transitions
  - Responsive design (mobile, tablet, desktop)
  - Success/error message notifications with icons
  - Material Icons integration throughout
  - Professional color scheme with hover effects
  - Card-based layouts for better organization

---

## 🛠️ Technology Stack

### Backend
- **Framework:** Django 6.0
- **Language:** Python 3.12
- **Database:** MySQL 8.0+
- **ORM:** Django ORM
- **Authentication:** Django Auth System

### Frontend
- **Framework:** Bootstrap 5.3
- **Icons:** Material Icons
- **Template Engine:** Django Templates (Jinja2-like syntax)
- **Custom Styling:** Custom CSS with gradient themes and animations

### Development Tools
- **Virtual Environment:** Python venv (django_sql)
- **Database Client:** MySQL Workbench
- **Code Editor:** VS Code
- **Version Control:** Git

### Python Dependencies
```
django==6.0
mysqlclient==2.2.7
pymysql==1.1.2
sqlparse==0.5.5
asgiref==3.11.0
```

---

## 📁 Project Structure

```
my_dbms_project/
│
├── manage.py                     # Django management script
├── README.md                     # Project documentation (this file)
│
├── myproject/                    # Main project configuration
│   ├── __init__.py
│   ├── settings.py              # Project settings & database config
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py                  # WSGI server configuration
│   └── asgi.py                  # ASGI server configuration
│
├── students/                     # Main application module
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models (Student table)
│   ├── views.py                 # Business logic & request handlers
│   ├── forms.py                 # Form definitions
│   ├── urls.py                  # App-specific URL routing
│   ├── tests.py                 # Unit tests
│   │static/                  # Static files (CSS, JS, Images)
│   │   └── css/
│   │       └── style.css        # Custom CSS with gradients & animations
│   │
│   ├── migrations/              # Database migration files
│   │   ├── __init__.py
│   │   ├── 0001_initial.py     # Initial Student model migration
│   │   └── __pycache__/
│   │
│   └── templates/               # HTML templates
│       ├── base.html            # Base template with navbar & layout
│       ├── login.html           # User login page
│       ├── register.html        # User registration page
│       ├── student_list.html    # Dashboard with student table & stats
│       ├── student_detail.html  # Student detail view pag
│       ├── student_list.html    # Dashboard with student table
│       ├── student_form.html    # Add/Edit student form
│       └── student_confirm_delete.html  # Delete confirmation
│
└── django_sql/                  # Virtual environment (venv)
    ├── bin/                     # Python executable & scripts
    ├── lib/                     # Installed packages
    ├── include/
    ├── pyvenv.cfg
    └── lib64 -> lib
```

---

## 🔧 Prerequisites

Before setting up the project, ensure you have the following installed:

### Required Software

1. **Python 3.10 or higher**
   ```bash
   # Check Python version
   python3 --version
   # or
   python --version
   ```

2. **MySQL Server 8.0+**
   ```bash
   # Check MySQL version
   mysql --version
   ```
   - Download from: [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
   - Ensure MySQL service is running on port 3306

3. **MySQL Workbench** (Optional but recommended)
   - For database visualization and management
   - Download from: [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)

4. **pip** (Python package manager)
   ```bash
   # Usually comes with Python, verify:
   pip --version
   ```

### System Requirements
- **OS:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **RAM:** Minimum 4GB (8GB recommended)
- **Disk Space:** 500MB for project + dependencies

---

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project

```bash
# If using Git
git clone <repository-url>
cd my_dbms_project

# Or extract the project ZIP file and navigate to the folder
cd /path/to/my_dbms_project
```

### Step 2: Set Up Virtual Environment

A virtual environment isolates project dependencies from your system Python.

```bash
# The virtual environment 'django_sql' should already exist
# If not, create it:
python3 -m venv django_sql        # Linux/macOS
python -m venv django_sql         # Windows

# Activate the virtual environment
source django_sql/bin/activate    # Linux/macOS
django_sql\Scripts\activate       # Windows

# You should see (django_sql) prefix in your terminal
```

### Step 3: Install Python Dependencies

```bash
# Install required packages
pip install django mysqlclient

# If mysqlclient installation fails on Windows:
# Install Microsoft C++ Build Tools first, then retry
# OR use pymysql as an alternative:
pip install pymysql

# If using pymysql, add this to myproject/__init__.py:
# import pymysql
# pymysql.install_as_MySQLdb()
```

### Step 4: Verify Installations

```bash
# Check Django installation
django-admin --version  # Should show 6.0 or higher

# Check installed packages
pip list
```

---

## 🗄️ Database Configuration

### Step 1: Create MySQL Database

Open MySQL Workbench or MySQL command line:

```sql
-- Login to MySQL
mysql -u root -p

-- Create database
CREATE DATABASE student_db;

-- Verify database creation
SHOW DATABASES;

-- (Optional) Create a dedicated user for security
CREATE USER 'example_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON student_db.* TO 'example_user'@'localhost';
FLUSH PRIVILEGES;
```

### Step 2: Configure Django Database Settings

Open `myproject/settings.py` and locate the `DATABASES` section (around line 76):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_db',           # Database name
        'USER': 'example_user',         # Your MySQL username
        'PASSWORD': 'password',         # Your MySQL password
        'HOST': 'localhost',            # Database host (127.0.0.1 or localhost)
        'PORT': '3306',                 # Default MySQL port
    }
}
```

**⚠️ Important:** Replace `'example_user'` and `'password'` with your actual MySQL credentials.

### Step 3: Run Database Migrations

Migrations create the necessary database tables based on your Django models.

```bash
# Create migration files (converts models to SQL)
python manage.py makemigrations

# Expected output:
# Migrations for 'students':
#   students/migrations/0001_initial.py
#     - Create model Student

# Apply migrations to database
python manage.py migrate

# Expected output:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, students
# Running migrations:
#   Applying students.0001_initial... OK
```

### Step 4: Verify Database Tables

In MySQL Workbench or command line:

```sql
USE student_db;

-- Show all tables
SHOW TABLES;

-- Expected tables:
-- auth_user, auth_group, students_student, django_migrations, etc.

-- View Student table structure
DESCRIBE students_student;

-- Expected columns:
-- id, first_name, last_name, email, gpa
```

---

## ▶️ Running the Application

### Step 1: Start the Development Server

```bash
# Ensure virtual environment is activated
# (You should see (django_sql) in your terminal)

# Run the Django development server
python manage.py runserver

# Expected output:
# Watching for file changes with StatReloader
# Performing system checks...
# System check identified no issues (0 silenced).
# December 25, 2025 - 10:00:00
# Django version 6.0, using settings 'myproject.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```

### Step 2: Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

or

```
http://localhost:8000/
```

### Step 3: Create Your First User

1. Click **"Sign Up"** or navigate to: `http://127.0.0.1:8000/register/`
2. Fill in the registration form:
   - Username (required)
   - Password (minimum 8 characters)
   - Password confirmation
3. Click **"Register"**
4. You'll be automatically logged in and redirected to the dashboard

### Step 4: Using the Application

#### Dashboard (`/`)
- View all students in a table
- Search students by name or email
- Click "Add Student" to create new records

#### Add Student (`/new/`)
- Fill in: First Name, Last Name, Email (unique), GPA (0.00-4.00)
- Click "Save" to add the student

#### Edit Student (`/edit/<id>/`)
- Click "Edit" button on any student row
- Modify fields and click "Save"

#### Delete Student (`/delete/<id>/`)
- Click "Delete" button on any student row
- Confirm deletion on the confirmation page

#### Logout
- Click "Logout" button in the navbar
- You'll be redirected to the login page

---

## 🧩 Project Components

### 1. Models (`students/models.py`)

Defines the database schema using Django ORM:

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Enforces uniqueness
    gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

**Generated SQL Table:**
```sql
CREATE TABLE students_student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    gpa DECIMAL(4,2) NOT NULL
);
```

### 2. Forms (`students/forms.py`)

Handles form validation and rendering:

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'gpa']
```

### 3. Views (`students/views.py`)

Contains the business logic for all operations:
, sorting, and statistics
- `student_create()`: Add new student
- `student_update()`: Edit existing student
- `student_delete()`: Remove student with confirmation
- `student_detail()`: View detailed student information
- `export_students_csv()`: Export all students to CSV file

#### CRUD Views
- `student_list()`: Display all students with sea
- Aggregation functions for statistics (Count, Avg)
- Column sorting with query parameters
- CSV export using Python's csv modulerch functionality
- `student_create()`: Add new student
- `student_update()`: Edit existing student
- `student_delete()`: Remove student with confirmation

**Key Features:**
- All CRUD views are protected with `@login_required` decorator
- Uses Django messages framework for user feedback
- Implements Q objects for complex search queries

### 4. URLs (`students/urls.py` & `myproject/urls.py`)

#### App URLs (`students/urls.py`):
```python
urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # CRUD Operations
    path('', views.student_list, name='student_list'),
    path('new/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
```

#### Root URLs (`myproject/urls.py`):
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Includes all student app URLs
]
``` with modern gradient design
- **register.html**: User registration form with validation feedback
- **student_list.html**: Main dashboard with statistics cards, search, sorting, and table
- **student_detail.html**: Detailed student profile view with avatar
- **student_form.html**: Form for creating/editing students
- **student_confirm_delete.html**: Deletion confirmation page with warning
- Contains navigation bar, user menu, and message display
- Uses Bootstrap 5 for responsive design
- Provides blocks for child templates to extend

#### Key Templates:
- **login.html**: User login form
- **register.html**: User registration formwith stats & sorting | ✅ Yes |
| GET | `/login/` | `LoginView` | Show login form | ❌ No |
| POST | `/login/` | `LoginView` | Process login | ❌ No |
| POST | `/logout/` | `LogoutView` | Logout user | ✅ Yes |
| GET | `/register/` | `register` | Show registration form | ❌ No |
| POST | `/register/` | `register` | Process registration | ❌ No |
| GET | `/new/` | `student_create` | Show create form | ✅ Yes |
| POST | `/new/` | `student_create` | Create new student | ✅ Yes |
| GET | `/edit/<id>/` | `student_update` | Show edit form | ✅ Yes |
| POST | `/edit/<id>/` | `student_update` | Update student | ✅ Yes |
| GET | `/delete/<id>/` | `student_delete` | Show delete confirmation | ✅ Yes |
| POST | `/delete/<id>/` | `student_delete` | Delete student | ✅ Yes |
| GET | `/detail/<id>/` | `student_detail` | View student details | ✅ Yes |
| GET | `/export/` | `export_students_csv` | Download CSV file | ✅ Yes |
| GET | `/?q=<query>` | `student_list` | Search students | ✅ Yes |
| GET | `/?sort=<field>` | `student_list` | Sort by column |
| POST | `/login/` | `LoginView` | Process login | ❌ No |
| POST | `/logout/` | `LogoutView` | Logout user | ✅ Yes |
| GET | `/register/` | `register` | Show registration form | ❌ No |
| POST | `/register/` | `register` | Process registration | ❌ No |
| GET | `/new/` | `student_create` | Show create form | ✅ Yes |
| POST | `/new/` | `student_create` | Create new student | ✅ Yes |
| GET | `/edit/<id>/` | `student_update` | Show edit form | ✅ Yes |
| POST | `/edit/<id>/` | `student_update` | Update student | ✅ Yes |
| GET | `/delete/<id>/` | `student_delete` | Show delete confirmation | ✅ Yes |
| POST | `/delete/<id>/` | `student_delete` | Delete student | ✅ Yes |
| GET | `/?q=<query>` | `student_list` | Search students | ✅ Yes |

---

## 💾 Database Schema

### Tables Created by Django

#### 1. `students_student` (Main table)
```sql
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| first_name | varchar(50)  | NO   |     | NULL    |                |
| last_name  | varchar(50)  | NO   |     | NULL    |                |
| email      | varchar(254) | NO   | UNI | NULL    |                |
| gpa        | decimal(4,2) | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
```

#### 2. `auth_user` (Django's built-in user table)
Stores registered users with hashed passwords.

#### 3. Other Django tables:
- `django_migrations`: Migration history
- `django_session`: User session data
- `auth_permission`, `auth_group`: Permission management

### Sample SQL Queries

```sql
-- View all students
SELECT * FROM students_student;

-- Search by name
SELECT * FROM students_student 
WHERE first_name LIKE '%John%' OR last_name LIKE '%John%';

-- Find high-performing students
SELECT * FROM students_student 
WHERE gpa >= 3.5 
ORDER BY gpa DESC;

-- Count total students
SELECT COUNT(*) AS total_students FROM students_student;

-- Average GPA
SELECT AVG(gpa) AS average_gpa FROM students_student;

-- Students grouped by GPA range
SELECT 
    CASE 
        WHEN gpa >= 3.5 THEN 'Excellent'
        WHEN gpa >= 3.0 THEN 'Good'
        ELSE 'Needs Improvement'
    END AS performance,
    COUNT(*) AS count
FROM students_student
GROUP BY performance;
```

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. **MySQL Connection Error**
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server")
```
**Solutions:**
- Verify MySQL service is running: `sudo systemctl status mysql` (Linux)
- Check credentials in `settings.py`
- Ensure database `student_db` exists
- Try changing `HOST` from `'127.0.0.1'` to `'localhost'` or vice versa

#### 2. **mysqlclient Installation Fails**
```
ERROR: Failed building wheel for mysqlclient
```
**Solutions:**
- **Windows:** Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Linux:** `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
- **macOS:** `brew install mysql`
- **Alternative:** Use pymysql instead:
  ```bash
  pip install pymysql
  ```
  Then add to `myproject/__init__.py`:
  ```python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

#### 3. **Migration Errors**
```
django.db.utils.ProgrammingError: (1146, "Table 'student_db.students_student' doesn't exist")
```
**Solutions:**
```bash
# Reset migrations (⚠️ Warning: Deletes data)
python manage.py migrate students zero
rm students/migrations/0001_initial.py
python manage.py makemigrations
python manage.py migrate
```

#### 4. **Port 8000 Already in Use**
```
Error: That port is already in use.
```
**Solutions:**
```bash
# Use a different port
python manage.py runserver 8080

# Or kill the process using port 8000 (Linux/macOS)
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

#### 5. **Static Files Not Loading**
**Solutions:**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Ensure Bootstrap CDN links are correct in `base.html`
- Check internet connection (Bootstrap is loaded from CDN)

#### 6. **CSRF Token Missing**
```
Forbidden (403): CSRF verification failed
```
**Solutions:**
- Ensure all POST forms have `{% csrf_token %}`
- Check `MIDDLEWARE` in `settings.py` includes `CsrfViewMiddleware`
- Clear cookies and try again

#### 7. **Virtual Environment Not Activating**
**Solutions:**
```bash
# Linux/macOS
source django_sql/bin/activate

# Windows (Command Prompt)
django_sql\Scripts\activate.bat

# Windows (PowerShell)
django_sql\Scripts\Activate.ps1

# If PowerShell gives execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🚀 Future Enhancements

### Planned Features

1. **Advanced Filtering**
   - Filter by GPA range
   - Sort by columns (name, email, GPA)
   - Pagination for large datasets

2. **Student Profiles**
   - Add photo upload
   - Add date of birth, phone number, address
   - Add course enrollment tracking

3. **Export Functionality**
   - Export to CSV
   - Export to PDF
   - Generate reports

4. **Email Notifications**
   - Send welcome email on registration
   - Password reset via email
   - Notifications for grade changes

5. **Role-Based Access**
   - Admin vs. Student roles
   - Teachers can edit, students can only view
   - Permission-based CRUD operations

6. **Data Visualization**
   - Charts for GPA distribution
   - Student statistics dashboard
   - Trend analysis

7. **REST API**
   - Django REST Framework integration
   - JSON API endpoints
   - Token authentication for API access

8. **Testing**
   - Unit tests for models
   - Integration tests for views
   - Test coverage reports

9. **Deployment**
   - Docker containerization
   - Production-ready settings
   - CI/CD pipeline

---

## 📄 License

This project is created for educational purposes as part of the Database Management Systems Laboratory course at UIU.

**Note:** This is a learning project and is not intended for production use without further security enhancements and testing.

---

## 📞 Support

For questions or issues:

- **Course Instructor:** Contact via UIU email
- **Django Documentation:** [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **MySQL Documentation:** [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/)
- **Bootstrap Documentation:** [https://getbootstrap.com/docs/](https://getbootstrap.com/docs/)

---

## 🙏 Acknowledgments

- Django Software Foundation for the excellent framework
- Bootstrap team for the responsive CSS framework
- MySQL for the reliable database system
- UIU CSE Department for course guidance
- Material Design team for the icon set

---

**Last Updated:** December 25, 2025  
**Version:** 1.0.0  
**Author:** UIU Student - CSE 3522 Fall 2025
