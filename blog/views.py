from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST) #Si el metodo es POST, queremos construir el PostForm
        if form.is_valid(): #Si el formulario es válido
            post = form.save(commit=False) #No guardamos aun hasta completar todos los campos
            post.author = request.user #Agregamos un autor
            post.published_date = timezone.now()
            post.save() #Lo guardamos
            return redirect('post_detail', pk=post.pk) #Una vez guardado, redirigir a la vista de publicaciones donde mostrara la publicacion recien creada por eso manda su id(pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
