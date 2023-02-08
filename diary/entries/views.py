from django.shortcuts import render, redirect
from .models import Enrty
from django.http import HttpResponse

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
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('body')
        entry = Enrty.objects.create(title=title, content=content)
        entry.save()
        return redirect('home')
    return render(request, 'entries/create_entry.html')


def deleteEntry(request, pk):
    entry = Enrty.objects.get(id=pk)
    
    if request.method == "POST":
        entry.delete()
        return redirect('home')
    
    context = {'obj': entry}
    return render(request, 'entries/delete_entry.html', context)