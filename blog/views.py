from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.
def search(request):
    query = request.GET['query']
    allposts = Post.objects.filter(title__icontains=query)
    #dsec = Post.objects.filter(title__icontains=query)
    paras = { 'allpost': allposts }

    return render(request,'blog/search.html',paras)

def home(request):
    allposts = Post.objects.all()
    context = {"allpost": allposts}
    template = "blog/bhome.html"

    return render(request,template,context)

def blog_post(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,"blog/blogpost.html",context)

def signup(request):
    if request.method == 'POST':
        uname= request.POST['uname']
        fname= request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['sphone']
        password1 = request.POST['spassword1']
        password2 = request.POST['spassword2']


        #check error here
        if len(uname) >10:
            messages.success(request, 'user name must be under 10 characters.')
            return redirect("home")
        if not uname.isalnum():
            messages.success(request, 'user must be letters and number.')
            return redirect("home")
        if password1 != password2:
            messages.success(request, 'your password did not match.')
            return redirect("home")



    #create user
        bloguser = User.objects.create_user(uname,email,password1)
        bloguser.first_name = fname
        bloguser.last_name = lname
        bloguser.save()
        messages.success(request, 'your account has been successfully  created.')
        return redirect('home')
    else:
        return HttpResponse("404 not found")

def loginblog(request):
    if request.method == 'POST':
        loginname= request.POST['loginname']
        logpassword = request.POST['logpassword']
        user = authenticate(username=loginname,password=logpassword)
        if user is not None:
            login(request,user)
            messages.success(request, ' successfully logged In')
            return redirect('/admin')
        else:
            messages.error(request, 'please try again')
    return render(request,"blog/bhome.html")


def logoutblog(request):
    logout(request)
    messages.success(request, 'successfully logout')
    return redirect('home')



