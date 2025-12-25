from django.db import models
from django.utils import timezone

class Student(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    
    # Additional Information
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def performance_level(self):
        if self.gpa >= 3.5:
            return "Excellent"
        elif self.gpa >= 3.0:
            return "Good"
        else:
            return "Needs Improvement"