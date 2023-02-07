from django.shortcuts import render
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