from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Foydalanuvchi nomi qo'llanilgan!")
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email qo'llanilgan!")
                return redirect('sign_up')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
        else:
            messages.info(request, "Parollar bir biriga to'g'ri kelmayabti, boshqa parol kiriting!")
            return redirect('sign_up')
        
        return redirect("../" + username)
    else:
        return render(request, "Sign-up/index.html")


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("../" + username)
        else:
            messages.info(request, 'Foydalanuvchi nomi yoki parol xato!!!')
            return redirect('sign_in')
    else:
        return render(request, "Login/index.html")


def logout(request):
    auth.logout(request)
    return redirect('/')