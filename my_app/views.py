from django.shortcuts import render, redirect
from .models import User, Book
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
            return redirect('/add_books/')
    else:
        messages.error(request, "Wrong info")
    return redirect('/')
    




def logout(request):
    request.session.clear()
    return redirect ("/")



def add_books(request):
    context = {
        "user": User.objects.get(id = request.session['User_id']),
        "books" : Book.objects.all(),
    }
    return render(request, "add_books.html", context)

def add_book(request):
    if request.POST:
        errors = Book.objects.basicc_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/add_books/")
        else:
            title=request.POST["title"]
            desc=request.POST["desc"]
            user=User.objects.get(id=request.session['User_id'])
            added_book = Book.objects.create(title = title, desc = desc, uploaded_by=user)
            added_book.users_who_like.add(user)
            return redirect("/add_books/")
    return redirect("/add_books/")

def add_to_fav(request, id):
    book=Book.objects.get(id=id)
    user= User.objects.get(id = request.session['User_id'])
    book.users_who_like.add(user)
    return redirect("/add_books/")

def edit_book(request, id):
    context = {
        "user": User.objects.get(id = request.session['User_id']),
        "book" : Book.objects.get(id=id),
    }
    return render(request, "edit_book.html", context)

def update(request, id):
    book=Book.objects.get(id=id)
    book.title=request.POST["title"]
    book.desc=request.POST["desc"]
    book.save()
    return redirect('/add_books/')

def un_fav(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['User_id'])
    book.users_who_like.remove(user)
    return redirect('/edit_book/' + str(book.id) + '/')

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/add_books/')