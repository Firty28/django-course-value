from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            print(request.user)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form })


def profile(request):
    return render(request, 'user/profile.html')


def login(request):
    return render(request, 'user/login.html')

def home(request):
    return HttpResponseRedirect(reverse('user:login'))




# user = User.objects.create_user(req['username'], req['first_name'], req['email'])
        # user.save()