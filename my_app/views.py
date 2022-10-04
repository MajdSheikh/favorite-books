from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        "User": User.objects.all()
    }
    return render(request, 'index.html', context)


def success(request):
    if 'User_id' not in request.session:   #check if the session doesnt have the user_id, return to login page.
        return redirect('/')
    context = {
        "user": User.objects.get(id = request.session['User_id'])
    }
    return redirect("/wall/")



def register_user(request):
    
    if request.POST:
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], 
            email=request.POST["email"],  password = pw_hash)

            messages.success(request, "successfully registered")

            request.session['User_id'] = user.id 
            return redirect("/success")


def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['User_id'] =  logged_user.id
            return redirect('/success')
    else:
        messages.error(request, "Wrong info")
    return redirect('/')
    




def logout(request):
    request.session.clear()
    return redirect ("/")

def delete_all(request):
    if User.objects.all():
        for user in User.objects.all():
            user.delete()
    return redirect("/")
        