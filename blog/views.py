from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, PostComment
from .forms import BlogcommentForm

# Create your views here.
class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "blog/post.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
        """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")

    if request.method == "POST":
        blog_form = BlogcommentForm(data=request.POST)
        if blog_form.is_valid():
            blog_comment = blog_form.save(commit=False)
            blog_comment.author = request.user
            blog_comment.post = post
            blog_comment.save()
            messages.add_message(
                request, messages.SUCCESS,'Comment submitted and awaiting approval'
                )

    blog_form = BlogcommentForm()
            
    return render(
        request,
        "blog/post_detail.html",
        {
            'post': post,
            'comments': comments,
            'blog_form': blog_form,
            },
    )

def comment_edit(request, slug, comment_id):
    """
    View to edit blog comments
    """

    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        blog_comment = get_object_or_404(PostComment, pk=comment_id)
        comment_form = BlogcommentForm(data=request.POST, instance=blog_comment)

        if comment_form.is_valid() and blog_comment.author == request.user:
            blog_comment = comment_form.save(commit=False)
            blog_comment.post = post
            blog_comment.approved = False
            blog_comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    
    return HttpResponseRedirect(reverse('blog_detail',args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View to delete blog comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    blog_comment = get_object_or_404(PostComment, pk=comment_id)
    
    if blog_comment.author == request.user:
        blog_comment.delete()
        messages.add_message(
            request, 
            messages.SUCCESS, 
            "Comment deleted!"
            )
    else:
        messages.add_message(
            request, 
            messages.ERROR, 
            "You can only delete yout own comments!"
            )
    return HttpResponseRedirect(reverse('blog_detail',args=[slug]))