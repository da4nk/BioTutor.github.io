from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from .models import Student, Tutor
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import logout

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache




class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "html/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user

        context['is_tutor'] = user.groups.filter(name='Tutor').exists()
        context['is_student'] = user.groups.filter(name='Students').exists()  
        context['tutoring'] = Tutor.objects.all()
        print("Tutors available:", context['tutoring'])  

        return context 
    
class TutorSelection(LoginRequiredMixin, View):
    def get(self, request):
        tutors = Tutor.objects.all()
        return render(request, 'html/index.html', {"tutoring": tutors})

    def post(self, request):
        tutor_id = request.POST.get('tutor')  
        student_id = request.POST.get('user')

        if not tutor_id or not student_id:
            return redirect('/')

        try:
            tutor = Tutor.objects.get(id=tutor_id)
            student = Student.objects.get(id=student_id)

            # Assign the tutor to the student (add to ManyToMany relationship)
            student.assigned_tutors.add(tutor)
            tutor.students.add(student)

            student.save()
            tutor.save()

            return redirect('/')  # or wherever you want to redirect after assignment
        except (Tutor.DoesNotExist, Student.DoesNotExist):
            return redirect('/')  # handle errors, like tutor or student not found

@method_decorator(never_cache, name='dispatch')
class LoginView(LoginView):
    template_name = "html/login.html"

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)  # Logs out the user
        return redirect('index')



class Hours(View):
    def get(self, request):
        students = Student.objects.get(id = request.user.id)
        hours = students.hours


        if request.user.is_authenticated:

            return redirect(reverse("index", kwargs = {"student_hours" : hours}))
        
