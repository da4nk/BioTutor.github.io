from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from . import Apiviews
from django.urls import path, include
from rest_framework import views as drf_views
from rest_framework_simplejwt import views as jwt_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'students', Apiviews.StudentViewSet, basename='student')

from .views import (
    LogoutView,
    IndexView,
    LoginView,
    TutorSelection
    
)



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login", LoginView.as_view(), name = "login"),
    path('TutorSelection', TutorSelection.as_view(), name = "TutorSelection"),
    path('logout', LogoutView.as_view(), name = "Logout"),


    # API VIEWS 
    path('api-auth/', include('rest_framework.urls')),
    path("auth", include(router.urls)),  # 👈 Make sure this is included

    
]
urlpatterns += router.urls
