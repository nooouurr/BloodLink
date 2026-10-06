from django.urls import path
from .views import HomeView, AdminLoginView, DonorLoginView, PatientLoginView, PatientSignupView, DonorSignupView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("adminlogin", AdminLoginView.as_view(), name="adminlogin"),
    path("donor/donorlogin", DonorLoginView.as_view(), name="donorlogin"),
    path("patient/patientlogin", PatientLoginView.as_view(), name="patientlogin"),
    path("patient/patientsignup", PatientSignupView.as_view(), name="patientsignup"),
    path("donor/donorsignup", DonorSignupView.as_view(), name="donorsignup"),
]