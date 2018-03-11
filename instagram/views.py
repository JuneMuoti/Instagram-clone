from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import NewImageForm,CommentsForm
from django.http import JsonResponse
from friendship.models import Friend, Follow



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
    my_images=Image.objects.filter(Profile__id=user_id)
    followers=Follow.objects.followers(request.user)
    return render(request,'profile.html',{"profiles":profiles,"my_images":my_images,'followers':followers})


def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        queryList = request.GET.get("user")
        searched_users = Profile.search_by_user(queryList)
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
@login_required
def add_comment(request, image_id):
    image = Image.objects.filter(id=image_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.image=image
            comment.save()
            return redirect('index')
    else:
        form=CommentsForm()
    return render(request,'add_comment.html',{'form':form})

def my_image(request,image_id):
    try:
        item= Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"item":item})

# Create your views here.
