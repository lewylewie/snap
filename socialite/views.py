from django.shortcuts import render,get_object_or_404, redirect
from .models import Profile, Comment
from .forms import ProfileForm, CommentForm, UserForm
from django.contrib.auth import login, authenticate,logout
from django.views.generic import CreateView
# Create your views here.
def index(request):
    profiles = Profile.objects.all()

    return render(request, 'socialite/index.html', {'profiles':profiles})
def indexs(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'socialite/comment.html', {'profile':profile})

def post_picha(request, profile_id):
    form = ProfileForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, pk=profile_id)
    comment = form.save()
    comment.profile = profile
    profile.image_cover = request.FILES['image_cover']
    comment.save()

    return render(request, 'socialite/profile_form.html', {'form':form})

def signup(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('socialite:index')
    return render(request, 'registration/signup.html', {'form':form})

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('socialite:index')
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('socialite:login')
class Comment(CreateView):
    model = Comment
    fields =['comment']
def allcomment(request, image_cover_id):
    image_cover = get_object_or_404(Profile, pk=image_cover_id)
    return render(request, 'socialite/comment-list.html', {'image_cover': image_cover})

class ProfileCreateView(CreateView):
    model = Profile
    fields = ['image_cover', 'image_caption']


