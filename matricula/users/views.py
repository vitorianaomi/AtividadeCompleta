from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print("Valid login")
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect('login')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'create.html', context)