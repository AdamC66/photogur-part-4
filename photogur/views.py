from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from django.db.models import Q

def root(request):
    return HttpResponseRedirect('pictures')

def pictures(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture':picture}
    return render(request, 'picture.html', context)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(Q(artist__icontains=query) | Q(title__icontains=query))
    context = {'pictures': search_results, 'query':query}
    return render(request, 'search.html', context)

def create_comment(request):
    picture_id = request.POST['picture']
    picture = Picture.objects.filter(id=picture_id).first()
    name = request.POST['name']
    message = request.POST['message']
    new_comment = Comment(name=name, message=message, picture = picture)
    new_comment.save()
    context = {'picture':picture}
    return render(request,'picture.html', context)