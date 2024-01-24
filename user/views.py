from django.shortcuts import render, redirect
from . models import Users
from . forms import Usersforms1

def list_users(request):
    users = Users.objects.all()

    return render(request, "list_users.html", {"users": users})

def create_user(request):
    form = Usersforms1()

    if request.method == 'POST':
        form = Usersforms1(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # user = Users(**form.cleaned_data)
            # user.save()

            return redirect('listusers')

    return render(request, 'create_user.html', {'form': form})

def update_user(request):
    pass

def delete_user(request):
    pass

