from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin

from .models import UserDetails
from .forms import SurveyForm

class SurveyView(FormView): 
    form_class = SurveyForm
    template_name = "home.html"

    def get_success_url(self):
        return reverse('dashboard')

    def form_valid(self, form):
        form.instance.super_user = self.request.user
        form.save()
        return redirect('dashboard')

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')

    def get_success_url(self):
        return reverse('home')

class LogoutView(View):
    # template_name = "frontend/logout.html"
    
    def get(self, request):
        logout(self.request)
        return redirect('login')


class AdminLoginView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "backend/admin_login.html"

    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))
            elif not self.user_cache.is_superuser:
                raise forms.ValidationError(_("User does not have SuperUser privileges."))
        self.check_for_test_cookie()
        return self.cleaned_data

    def get_success_url(self):
        return reverse('admin_page')