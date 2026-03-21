from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import forms
from django.views import generic


#регистрация
class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'

# def register_view(request):
#     if request.method == 'POST':
#         #form = UserCreationForm(request.POST, request.FILES)
#         form = forms.CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         #form = UserCreationForm()
#         form = forms.CustomUserCreationForm()
#     return render(request, 'register.html',
#                   {'form': form,}
#                   )
    
#авторизация
from django.contrib.auth.views import LoginView, LogoutView

class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/congratulation/'

# def auth_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/congratulation/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html',
#                   {'form': form,}
#                   )
    
#выход из аккаунта
from django.urls import reverse_lazy

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# def auth_logout_view(request):
#     logout(request)
#     return redirect('/login/')

#успешная авторизация
class CongratulationView(generic.TemplateView):
    template_name = 'cong.html'

# def cong_view(request):
#     if request.method == 'GET':
#         user = User.objects.all()
#     return render(request, 'cong.html', 
#                   {'user': user,}
#                   )
    