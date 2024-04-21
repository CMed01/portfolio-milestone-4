from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
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

    blog_form = BlogcommentForm()
            
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            'blog_form': blog_form,
            },
    )