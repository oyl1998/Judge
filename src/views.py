from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from . import models

problems = models.Problem.objects.all()

def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'user':None})
    elif request.method == 'POST':
        inputId = request.POST.get('inputId')
        inputPassword = request.POST.get('inputPassword')
        users = models.User.objects.all()
        for user in users:
            if user.User_Id == inputId and user.User_Password == inputPassword:
                return render(request, 'index.html', {'user':user, 'problems':problems})
    return redirect("/login")

def problem(request):
    return render(request, 'problem.html', {'problems':problems})

def show_problem(request, problem_id):
    problem = get_object_or_404(models.Problem, pk=problem_id)
    return render(request, 'show_problem.html', {'problem':problem})

def user_home_page(requset, user_id):
    user = get_object_or_404(models.User, pk=user_id)
    return render(requset, 'user_home_page.html', {'user':user})