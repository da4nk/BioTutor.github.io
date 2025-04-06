from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Tutor, Student
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# Custom form to limit students to 3 per tutor
class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

    def clean_students(self):
        students = self.cleaned_data.get('students', [])
        if len(students) > 3:
            raise ValidationError("A tutor can have a maximum of 3 students.")
        return students

class TutorAdmin(admin.ModelAdmin):
    form = TutorForm  # Apply custom form with validation
    list_display = ['name', 'subjects_taught', 'hours']
    search_fields = ['name']

class StudentInline(admin.TabularInline):
    model = Tutor.students.through  # ManyToMany intermediate table
    extra = 0  # Prevent extra empty forms

# Register Tutor with custom admin
admin.site.register(Tutor, TutorAdmin)

# Register Student model
admin.site.register(Student)
