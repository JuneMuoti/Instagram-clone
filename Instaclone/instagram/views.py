from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import NewImageForm,CommentsForm
from django.http import JsonResponse



@login_required(login_url='/accounts/login/')

def index(request):
    images=Image.my_image()
    form = CommentsForm()
    return render(request,'index.html',{"images":images},{"commentForm": form})
def comments(request):
    comment = request.POST.get('your_comment')

    return JsonResponse()


@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profiles= Profile.objects.get(id = user_id)
    images=Image.objects.all()
    return render(request,'profile.html',{"profiles":profiles},{"images":images})


def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        queryList = request.GET.get("user")
        searched_users = Image.search_by_user(queryList)
        message = f"{queryList}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

# Create your views here.
