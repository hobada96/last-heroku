from django.shortcuts import render , get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Blog.objects # 쿼리셋
    return render(request,'home.html', {'blogs':blogs})

def detail(request, blog_id) :
    blogs = Blog.objects # 쿼리셋
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blogs':blogs, 'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받는 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #url은 항상 문자열
