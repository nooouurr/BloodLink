from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "blood/index.html"

class AdminLoginView(TemplateView):
    template_name = "blood/adminlogin.html"

class DonorLoginView(TemplateView):
    template_name = "donor/donorlogin.html"

class PatientLoginView(TemplateView):
    template_name = "patient/patientlogin.html"

class PatientSignupView(TemplateView):
    template_name = "patient/patientsignup.html"

class DonorSignupView(TemplateView):
    template_name = "donor/donorsignup.html"