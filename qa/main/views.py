from django.shortcuts import HttpResponse, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.signals import post_syncdb
from django.contrib.sites.models import Site
from django.template import RequestContext
from qa.main.models import UserProfile
import datetime

def index(request):
    return render_to_response("index.html")

def home(request):
    return HttpResponse("Home")

@login_required
def check_qa(request):
    if request.method == "POST":
        answer = request.POST.get("answer", None)
        if answer == request.user.get_profile().answer:
            profile = request.user.get_profile()
            profile.last_login = datetime.datetime.now()
            return redirect(reverse("home")) 
    question = request.user.get_profile().question
    return render_to_response("check.html", {"question":question}, context_instance=RequestContext(request))

@login_required
def save_profile(request):
    profile = request.user.get_profile()
    profile.question = request.POST.get("question", "")
    profile.answer = request.POST.get("answer", "")
    profile.save()
    return redirect(reverse("check_qa"))