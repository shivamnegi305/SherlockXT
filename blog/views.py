from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
     posts = Post.objects.all()
     return render(request, 'home.html', {'posts': posts})



def contact(request):
     return render(request, 'contact.html')



def about(request):
     return render(request, 'about.html')


def create(request):
     return render(request, 'create.html')



def create_process(request):
     a = request.POST['title']
     b = request.POST['text']

     post = Post.objects.create(title=a, text=b)
     post.save()

     return HttpResponseRedirect('/')


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return HttpResponseRedirect('/')
