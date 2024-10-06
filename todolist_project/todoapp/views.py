from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import TodoItem
from .forms import TodoForm

# Create your views here.
def home(request):
    return render(request, "todohome.html")

def todos(request):
    # items = TodoItem.objects.all()
    item_list = TodoItem.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos")
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "To Do List",
    }
    return render(request, "todos.html", page)

def remove(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todos')