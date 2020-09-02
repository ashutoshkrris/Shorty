from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['username'] and request.POST['password']:
                try:
                    login_username = request.POST['username']
                    login_password = request.POST['password']
                    user = authenticate(username=login_username, password=login_password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        return render(request, 'login.html', {'error': 'Username or Password is incorrect.'})    
                    if request.POST['next'] != '':
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')
                    return redirect('/')
                except User.DoesNotExist:
                    return render(request, 'login.html', {'error': 'User doesn\'t exist.'})
            else:
                return render(request, 'login.html', {'error': 'Empty Fields.'})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['username'] and request.POST['password']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'signup.html', {'error' : 'User already exists.'})
                except User.DoesNotExist:
                    User.objects.create_user(
                        email = request.POST['email'],
                        username=request.POST['username'],
                        password = request.POST['password']
                    )
                    messages.success(request, "Signup Successful, \n Login Here.")
                    return redirect(loginPage)
            else:
                return render(request, 'signup.html', {'error' : 'Empty fields.'})    
        else:
            return render(request, 'signup.html', {'error' : 'Passwords do not match.'})
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/loginPage')

@login_required(login_url='/loginPage/')
def passwordChange(request):
    if request.method == 'POST':
        current = request.POST['oldPassword']
        newpass = request.POST['newPassword']
        conpass = request.POST['confirmPassword']
        if newpass==conpass:
            user = User.objects.get(id=request.user.id)
            check = user.check_password(current)
            if check == True:
                user.set_password(newpass)
                user.save()
                messages.success(request, "Password Changed")
                return redirect(loginPage)
            else:
                return render(request, 'passwordChange.html', {'error' : 'Current password is incorrect.'})
        else:
            return render(request,'passwordChange.html', {'error' : 'New Password and Confirm password don\'t match.'})
    return render(request,'passwordChange.html')