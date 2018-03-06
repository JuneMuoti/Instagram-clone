from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile



@login_required(login_url='/accounts/login/')

def index(request):
    images=Image.my_image()
    return render(request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profiles= Profile.objects.get(id = user_id)
    return render(request,'profile.html',{"profiles":profiles})


def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        queryList = request.GET.get("user")
        searched_users = Image.search_by_user(queryList)
        message = f"{queryList}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

# Create your views here.
