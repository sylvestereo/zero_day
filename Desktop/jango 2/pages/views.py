from django.shortcuts import render, redirect
from pages.models import Blog
from pages.form import BlogForm

# Create your views here.
def index(request):
    all_blogs = Blog.objects.all().order_by('-date')
    return render(request, 'index.html', {'all_blogs': all_blogs})

def add (request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        form = Blog(title=title, body=body)
        form.save()
        return redirect('index')
    return render(request, 'add.html')

def blog (request, id):
    single_blog = Blog.objects.get(id=id)
    return render(request, 'blog.html', {'single_blog': single_blog})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
