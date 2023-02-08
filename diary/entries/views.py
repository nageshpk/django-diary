from django.shortcuts import render, redirect
from .models import Enrty
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def homeView(request):
    entry_list = Enrty.objects.all()
    context = {'entry_list': entry_list}
    return render(request, "entries/entry_list.html", context)


def entryDetail(request, pk):
    entry = Enrty.objects.get(id=pk)
    context = {'entry': entry}
    return render(request, 'entries/entry_detail.html', context)


def createEntry(request):
    page = 'create'
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('body')
        entry = Enrty.objects.create(title=title, content=content)
        entry.save()
        messages.success(request, "New entry created")
        return redirect('home')
    
    context = {'page': page}
    return render(request, 'entries/create_entry.html')


def deleteEntry(request, pk):
    entry = Enrty.objects.get(id=pk)
    
    if request.method == "POST":
        entry.delete()
        messages.info(request, "Entry deleted")
        return redirect('home')
    
    context = {'obj': entry}
    return render(request, 'entries/delete_entry.html', context)


def editEntry(request, pk):
    entry = Enrty.objects.get(id=pk)
    context = {'entry': entry}
    if request.method == "POST":
        entry.title = request.POST.get('title')
        entry.content = request.POST.get('body')
        entry.save()
        messages.info(request, "Updated !!")
        return redirect('entry-detail', pk)
    
    return render(request, 'entries/create_entry.html', context)
