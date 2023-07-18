from django.shortcuts import render
from django.http import HttpResponse
from PhotoIndex.models import Directory, Item

def collection(request):
    dirs = []
    for dir in Directory.objects.filter(parent=None):
        dirs.append({"parent": dir, "children": dir.directory_set.all()})
    context = {"dirs": dirs}
    return render(request, 'PhotoIndex/collection.html', context)