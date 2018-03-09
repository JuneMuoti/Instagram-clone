from django.shortcuts import render,redirect
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



def profile(request,user_id):
    profiles= Profile.objects.get(id = user_id)
    my_images=Image.objects.filter(id = user_id)
    return render(request,'profile.html',{"profiles":profiles},{"my_images":my_images})


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

    form = CommentsForm(request.POST)
    image = Image.objects.filter(id=image_id)

    if form.is_valid():
        comment = Comment()

        comment.image_id = image
        comment.user = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

        # Django does not allow to see the comments on the ID, we do not save it,
        # Although PostgreSQL has the tools in its arsenal, but it is not going to
        # work with raw SQL queries, so form the path after the first save
        # And resave a comment


        comment.save()

    return redirect('index')

# Create your views here.
