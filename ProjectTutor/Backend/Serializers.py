from .models import Student, Tutor
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'user', 'hours', 'learning_goals', 'tutor']

class TutorSerializer(serializers.ModelSerializer):
    class meta: 
        model = Tutor
        fields = '__all__' 
    def validate_students(self, students):
        """Limit the number of students a tutor can have"""
        if len(students) > 3:
            raise serializers.ValidationError("A tutor can only have up to 3 students.")
        return students
