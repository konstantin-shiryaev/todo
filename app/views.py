from django.shortcuts import render, HttpResponse,redirect
from .models import Todo, Person


# Create your views here.
def home(request):

    # Сделать запрос на вывод всех задач
    todos = Todo.objects.all()
    new_todo = request.POST.get('todo')
    todo_pk = request.GET.get('todo')

    if todo_pk:
        todo = todos.get(pk=todo_pk)
        todo.is_done = False if todo.is_done else True
        todo.save()
        return redirect('app:home')

    if request.method == 'POST' and new_todo:

        Todo.objects.create(text=new_todo, is_done=False)
        return redirect('app:home')
    # ожидает отправки POST апроса
    stat = {
        'all': todos.count(),
        'finished': todos.filter(is_done=True).count(),
        'open': todos.filter(is_done=False).count()
    }
    print(stat)
    context = {'todos': todos, 'stat' : stat}
    return render(request, 'home.html', context)

def delete_todo(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('app:home')
    return render(request, 'delete_todo.html', {})

def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    new_text = request.POST.get('todo')
    if new_text:
        Todo.objects.filter(pk=pk).update(text=new_text)
        # todo.text = new_text
        # todo.save()
        return redirect('app:home')
    return render(request, 'edit_todo.html', {'todo': todo})

def people(request):
    # Сделать запрос на вывод всех задач
    persons = Person.objects.all()
    context = {'persons': persons}
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        Person.objects.create(user_name=user_name, last_name=last_name, age=age)
    return render(request, 'people.html', context)