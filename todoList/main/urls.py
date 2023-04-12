from django.urls import path
from .views import getAllTodos, getTodoById, createTodo, updateTodo, deleteTodo, userSignup, userLogin, userLogout

urlpatterns = [
    path('', getAllTodos),
    path('todos/<str:id>', getTodoById, name='todos'),
    path('create/', createTodo, name='create'),
    path('update/<str:id>', updateTodo, name='update'),
    path('delete/<str:id>', deleteTodo, name='delete'),
    path('signup/', userSignup, name='signup'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
]
