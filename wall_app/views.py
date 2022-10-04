from django.shortcuts import render, redirect
from .models import User,Message,Comment
from django.contrib import messages
import bcrypt



def wall(request):
    if 'User_id' not in request.session:  
        return redirect('/')
    context = {
        "user": User.objects.get(id = request.session['User_id']),
        'messages':Message.objects.all().order_by('-created_at'),
    }
    return render(request, "wall.html",context)



def post_message(request):
    if request.POST:
        Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['User_id']))
    return redirect('/wall')

def add_comment(request):
    if request.POST:
        Comment.objects.create(comment=request.POST['comment'], 
        user= User.objects.get(id=request.session['User_id']),
        message= Message.objects.get(id=request.POST['message_id']))
    return redirect("/wall")


def delete_message(request):
    if request.POST:
        message_delete=Message.objects.get(id=request.POST['delete_message_id'])
        message_delete.delete()
    return redirect('/wall')

def delete_comment(request):
    if request.POST:
        comment_delete=Comment.objects.get(id=request.POST['delete_comment_id'])
        comment_delete.delete()
    return redirect('/wall')

