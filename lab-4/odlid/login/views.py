from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from .models import Client
import requests


class LoginView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"
    

    joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()

    def get(self, request):
        return render(
            request,
            "login.html",
            context={"form": self.form_class(), "joke_setup": self.joke["setup"], "joke_punchline": self.joke["punchline"]},
        )

    success_url = "/home"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        print('Session is activated')
        return super(LoginView, self).form_valid(form)


class RegistrationView(FormView):
    form_class = RegistrationForm

    success_url = '/auth/login'
    template_name = 'registration.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()

        # Client.objects.create(email=form.cleaned_data['email'], 
        #                       unique_code=form.cleaned_data['unique_code'], 
        #                       phone=form.cleaned_data['phone'], 
        #                       city=form.cleaned_data['city'], 
        #                       address=form.cleaned_data['address'] ).save()
        
        return super(RegistrationView, self).form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        print('Form is invalid')
        return super(RegistrationView, self).form_invalid(form)



class LogoutView(FormView):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/home')
