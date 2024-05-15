import random
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.utils.timezone import now
from django.shortcuts import render, redirect
from apps.users.models import CustomUser, UserAuthCode
from apps.users.services import send_email_to_user
from django.contrib.auth.decorators import login_required
from apps.users.forms import CustomUserCreateForm


def register_page(request):
    return render(request, template_name='register.html', context={'error':False})


def send_code_to_email(request):
    if request.method != "POST":
        return redirect("register-page")
    email, password, re_password = request.POST.get('email'), request.POST.get('password'), request.POST.get('re_password')

    if not (email and password and re_password):
        messages.error(request, message="Malumotlarni to'liqkiriting")
        return redirect('register-page')

    if password != re_password:
        messages.error(request, message='Parollar biexil emas')
        return redirect('register-page')

    if CustomUser.objects.filter(email=email).exists():
        messages.error(request, message='Bu email mavjud\nBoshqa email kiriting yoki shu email orqali login qiling')
        return redirect('register-page')

    code = random.randint(1000, 10000)
    send_email_to_user(email, code)
    UserAuthCode.objects.create(email=email, code=code, expire_at=now() + timedelta(minutes=5))

    context = {
        'email': email,
        'password': password,
    }
    return render(request, 'confirm_email.html', context)


def register_user(request):
    if request.method != "POST":
        return redirect('register-page')
    code = request.POST.get('code')
    email = request.POST.get('email')
    password = request.POST.get('password')

    UserAuthCode.objects.filter(expire_at__lte=now()).delete()

    objs = UserAuthCode.objects.filter(code=code, email=email, expire_at__gte=now())
 
    if objs.exists():

        CustomUser.objects.create_user(email=email, password=password)
        objs.delete()
    elif UserAuthCode.objects.filter(email=email, expire_at__gte=now()):
        context = {
            'email': email,
            'password': password,
            'code': code,
            'code_error': "Noto'g'ri kod kirittingiz."
        }
        return render(request, 'confirm_email.html', context)

    else:
        return redirect('register-page')
    return render(request, 'login.html')


def login_page(request):
    if request.method != "POST":
        return render(request, 'login.html')

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        redirect_url = request.POST.get('next')
        if redirect_url:
            return redirect(redirect_url)
        else:
            return redirect('home-page')
    else:
        messages.error(request, "Lofgin yokiparolni noto'g'ri kirittingiz")
        return redirect('login_page')


@login_required
def logout_page(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def profil_page(request):
    form = CustomUserCreateForm(instance=request.user)
    return render(request, template_name='profil.html', context={'form': form})


@login_required
def profil_crud(request):
    if request.method != 'POST':
        return redirect('profil_page')

    form = CustomUserCreateForm(data=request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your new profile has been saved.')
    else:
        messages.error(request, form.errors)
    return redirect('profil_page')