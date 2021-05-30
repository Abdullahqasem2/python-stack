from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request): 
    return render(request,"index.html")

def reglog(request):
    if request.POST['action'] ==  "register":
        errors = user.objects.reg(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:    
            if request.POST['action'] ==  "register":
                if request.POST['pass'] == request.POST['cpass']:
                    request.session['email'] = request.POST['email']
                    user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
                    email=request.POST['email'],password=request.POST['pass'])
                    return redirect("/welcome")
                else:
                    return redirect("/")
    else:
        errors = user.objects.log(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            if request.POST['action'] ==  "login":
                users = user.objects.filter(email=request.POST['Lemail'])
                if users:
                    if users[0].password == request.POST['Lpass']:
                        request.session['email']=users[0].email
                        request.session['id']=users[0].id
                        request.session['name']=users[0].first_name
                        
                        return redirect("/welcome")
                    else:
                        return redirect("/")

def welcome(request):
    
    context={
        "fname": request.session['name'],
        "email": request.session['email'],
        "this_user_id": request.session['id'],
        "all_books": Book.objects.all(),
    }
    return render(request,"profile.html",context)

def logout(request):
    del request.session['email']
    return redirect("/")
def add_book(request):
    this_user_id = request.session['id']
    this_user = user.objects.get(id = this_user_id)
    Book.objects.create(title = request.POST['title'],description = request.POST['description'], users = this_user)
    return redirect("/welcome")
def show_books(request,id):
    context={
        "this_user_id": request.session['id'],
        "book": Book.objects.get(id = id),
    }
    return render(request,"book.html",context)
def add_to_fav(request,id):
    this_user_id = request.session['id']
    this_book = Book.objects.get(id = id)
    sp_user = user.objects.get(id = this_user_id)
    this_book.favorit.add(sp_user)
    return redirect("/welcome")
def edit(request,id):
    e_t = Book.objects.get(id = id)
    e_t.title = request.POST['edit_title']
    e_t.save()
    e_b = Book.objects.get(id = id)
    e_b.description = request.POST['edit_description']
    e_b.save()
    return redirect('/show_books/'+ str(id))
def delete(request,id):
    book_to_delete = Book.objects.get(id = id)
    book_to_delete.delete()
    return redirect('/welcome')
def breack_up(request,id):
    this_user_id = request.session['id']
    this_book = Book.objects.get(id = id)
    sp_user = user.objects.get(id = this_user_id)
    this_book.favorit.remove(sp_user)
    return redirect('/show_books/'+ str(id))
