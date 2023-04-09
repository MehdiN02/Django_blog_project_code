from django.shortcuts import render, redirect, reverse
from .models import Post
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy


# ----------------------------------------------------------------------------------------
# def posts_list_view(request):
    # all_posts_list = Post.objects.all()
    # posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
    # return render(request, 'blog/posts_list.html', {'all_posts_list': posts_list})

class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'all_posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


# --------------------------------------------------------------------------------------
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk) # behtarin ravesh
    # try:
        # post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist: # ravesh 1
    # except ObjectDoesNotExist:  # ravesh 2
        # post = None
        # print('exception')
    # return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# -----------------------------------------------------
# def create_new_post_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
            # form = NewPostForm()
#
#     else:  # Get request
#         form = NewPostForm()
#
#     return render(request, 'blog/post_create.html', {'form': form})

    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('GET request')
    # return render(request, 'blog/post_create.html')


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


# ----------------------------------------------------------------------
# def post_edit_views(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', {'form': form})


class PostEditView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


# ---------------------------------------------------------------------
# def post_delete_views(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', {'post': post})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')
