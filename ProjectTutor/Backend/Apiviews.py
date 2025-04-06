from .models import Student, Tutor
from .Serializers import StudentSerializer, TutorSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'  

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    lookup_field = 'id'