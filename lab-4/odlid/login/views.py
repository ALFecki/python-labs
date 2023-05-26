from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from .models import Client
import requests


class LoginView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    quote = requests.get("https://favqs.com/api/qotd").json()

    def get(self, request):
        return render(
            request,
            "login.html",
            context={"form": self.form_class(), "quote": self.quote["quote"]["body"]},
        )

    success_url = "/register"


class RegistrationView(FormView):
    form_class = RegistrationForm

    success_url = '/'
    template_name = 'registration.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()

        Client.objects.create(email=form.cleaned_data['email'], 
                              unique_code=form.cleaned_data['unique_code'], 
                              phone=form.cleaned_data['phone'], 
                              city=form.cleaned_data['city'], 
                              address=form.cleaned_data['address'] ).save()
        
        return super(RegistrationView, self).form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        return super(RegistrationView, self).form_invalid(form)


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user != None:
#                 if user.is_active():
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
