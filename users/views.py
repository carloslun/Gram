from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.db.utils import IntegrityError

# Create your views here.
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
             
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
        


    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']
        if password != password_confirmation:         
            return render(request, 'users/signup.html',{'error':'Los password no coinciden'} )
        if User.objects.filter(email = request.POST['email']):
            return render(request, 'users/signup.html',{'error':'El email ya existe'} )

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'No se pudo crear el usuario'} )


        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile  = Profile(user = user)
        profile.save()
        login(request, user)
        return redirect('feed')

    return render(request, 'users/signup.html')
@login_required
def update_profile(request):
    profile = request.user.profile
    print(profile.picture.url)
    return render(
        request = request,
        template_name = 'users/update_profile.html',
        context = {
            'profile' : profile,
            'user' : request.user
        }
        )

