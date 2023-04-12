from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, UserSignupForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def getAllTodos(request):
    user = request.user
    todos = Todo.objects.filter(user = user)
    print(todos)
    context = {
        'todos': todos,
        'user': user
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def getTodoById(request, id):
    selectedTodo = Todo.objects.get(id=id)
    todoItems = selectedTodo.todoitem_set.all()
    context = {
        'todos': selectedTodo,
        'todoItems': todoItems,
    }
    return render(request, 'tododetails.html', context)

@login_required(login_url='login')
def createTodo(request):

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

@login_required(login_url='login')
def updateTodo(request, id):
    selectedTodo = Todo.objects.get(id=id)
    form = TodoForm(instance=selectedTodo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=selectedTodo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

@login_required(login_url='login')
def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def userSignup(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context= {
        'form': form,
    }
    return render(request, 'signup.html', context)

def userLogin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def userLogout(request):
    logout(request)
    return redirect('/login')