from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import TodoItem

def homepage(request):

    item_list = TodoItem.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TO DO LIST",
    }
    return render(request, 'todoapp/index.html', page)

def remove(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')