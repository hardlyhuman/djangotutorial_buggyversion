from django.shortcuts import render
from django.http import Http404
from . models import tagLine

def index(request):
    if request.POST:
        tagLine(tagline = request.POST.get("tagline",""),username = request.POST.get("name","")).save()
    
    #Fill your code below
    #Hint: Get the list of tagLine objects, complete the context and render all the required objects.
    
    context = {'taglines':''} #set taglinesList to the context so that the template engine can access it


def detail(request,id):
    try:
        tagline = tagLine.objects.get(pk = id)
    except:
        raise Http404("Tagline does not exist")
    if request.POST:
        # Fill the gaps in between.
        tagline.numberOfVotes += 1
        # Hint: What you save , is what you get
    return render(request,'ratemytagline/details.html',{'tagline':tagline})
