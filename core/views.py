from django.shortcuts import render, redirect


from .models import Blog
from .forms import BlogForm



def home(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        form = BlogForm()

        context = {
            'blogs': blogs,
            'form': form
        }
        return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def dashboard(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        form = BlogForm()

        context = {
            'blogs': blogs,
            'form': form
        }
        return render(request, 'core/dashboard.html', context)

    if request.method == 'POST':
        blogs = Blog.objects.all()
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
        context = {
            'blogs': blogs,
            'form': form
        }
        return render(request, 'core/dashboard.html', context)


def update(request, pk):
    if request.method == 'GET':
        blog = Blog.objects.get(id=pk)
        form = BlogForm(instance=blog)
        context = {'form': form}

        return render(request, 'core/update.html', context)

    if request.method == 'POST':
        blog = Blog.objects.get(id=pk)
        form = BlogForm(data=request.POST, files=request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
        context = {'form': form}

        return render(request, 'core/update.html', context)


def delete(request, pk):
    Blog.objects.get(id=pk).delete()
    return redirect('/dashboard/')