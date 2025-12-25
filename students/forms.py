from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    enrollment_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 
                  'date_of_birth', 'enrollment_date', 'gpa', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '4'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ImportCSVForm(forms.Form):
    csv_file = forms.FileField(
        label='Select CSV File',
        help_text='Upload a CSV file with columns: first_name, last_name, email, gpa, phone, address',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )

class FilterForm(forms.Form):
    min_gpa = forms.DecimalField(
        required=False,
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min GPA', 'step': '0.01'})
    )
    max_gpa = forms.DecimalField(
        required=False,
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max GPA', 'step': '0.01'})
    )
    performance = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('excellent', 'Excellent'), ('good', 'Good'), ('needs_improvement', 'Needs Improvement')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )