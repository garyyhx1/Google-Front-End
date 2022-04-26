from django.shortcuts import render
from django.http import HttpResponse
from . import util
import random

# Create your views here.
def home (request):
    return render(request, "UCLAwiki/index.html", {
           "entries":util.list_entries()
       })

def index(request, name):
    if (name =="random"):
        entry = random.choice(util.list_entries())
        return render(request, "UCLAwiki/edit.html", {
           "name":util.get_entry(entry)
       })
    else:
        if (util.get_entry(name) != None):
            return render(request, "UCLAwiki/edit.html", {
           "name":util.get_entry(name)
       })
        else:
            return render (request, "UCLAwiki/index.html", {"name": ": Entry can't be found","entries":util.list_entries()})
#def random (request):
 #   entry = random.choice(util.list_entries)
  #  return render(request, "UCLAwiki/edit.html", {
   #        "name":entry
     #  })
    #return render(request, "UCLAwiki/edit.html", {"name":entry})

#def edit(request):

    # return render(request, "UCLAwiki/edit.html")
