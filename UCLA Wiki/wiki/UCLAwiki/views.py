from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
import random



# Create your views here.
def home (request):
    if request.method=="POST":
            searchvalue = request.POST['search']      
            return HttpResponseRedirect("/UCLAwiki/entry/" + searchvalue)
       
    else:
            return render(request, "UCLAwiki/index.html", {
             "entries":util.list_entries()
       })

def index(request, name):
    
        if (util.get_entry(name) != None):
            return render(request, "UCLAwiki/edit.html", {
           "results":util.get_entry(name),
           "entries":util.list_entries(),
           "entryname":name
       })
        else:
            entrylist=util.list_entries()
            containname=[]
            for entry in entrylist:
                if name.lower() in entry.lower():
                    containname.append(entry)
            isnotempty=len(containname)!=0
            return render (request, "UCLAwiki/searchresults.html",  {
                "entries":util.list_entries(),
                "results": containname, 
                "isnotempty":isnotempty})

def randomentry(request):
     entry = random.choice(util.list_entries())
     return redirect("entry/" + entry)

def newentry(request):
    return render(request, "UCLAwiki/newentry.html", {
        "entries":util.list_entries()
    })

def saveentry(request):
    if request.method=="POST":
        newtitle = request.POST['title']      
        newcontent = request.POST['content']
        if newtitle in util.list_entries():
            return render(request, "UCLAwiki/newentryfailed.html",{
            "entries":util.list_entries()
    })
            
        else:
            util.save_entry(newtitle, newcontent)
            return HttpResponseRedirect("entry/" + newtitle)
           

def editentry(request, entryname):

    return render(request, "UCLAwiki/editentry.html", {
        "entries":util.list_entries(), 
        "existingentry": util.get_entry(entryname), 
        "existingentryname":entryname
    })

def saveedit(request):

    if request.method=="POST":
        title = request.POST['title']     
        content = request.POST['content']

        util.save_entry(title, content)
        return HttpResponseRedirect("entry/" + title)
           