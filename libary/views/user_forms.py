from django.shortcuts import render, redirect
from libary.forms import RegisterForm, ResgisteUpdateForm
from django.contrib import messages, auth  # type: ignore
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso.')

            return redirect('libary:login')

    return render(request, 'libary/register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso.')
            return redirect('libary:index')
        messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'libary/login.html', {'form': form})


@login_required(login_url='libary:login')
def user_update(request):
    form = ResgisteUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'libary/update_user.html', {'form': form})

    form = ResgisteUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'libary/update_user.html', {'form': form})

    form.save()
    return redirect('libary:user_update')


@login_required(login_url='libary:login')
def logout_view(request):
    auth.logout(request)
    return redirect('libary:login')
