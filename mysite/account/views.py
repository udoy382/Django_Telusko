from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.Info(request, 'Username already Taken')
                messages.success(request, 'Username already Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                # messages.Info(request, 'email already Taken')
                messages.success(request, 'email already Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
        else:
            # messages.info(request, "Password not matching, Please try again")
            messages.success(request, 'Password not matching, Please try again')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'account/register.html')