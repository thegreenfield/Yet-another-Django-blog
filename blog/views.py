from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from blog.models import *
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]


def post(request, pk, slug=None):
    """Single post with comments and a comment form."""
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)

def delete_comment(request, post_pk, pk=None):
    """Delete comment(s) with primary key `pk` or with pks in POST."""
    if request.user.is_staff:
        if not pk: pklst = request.POST.getlist("delete")
        else: pklst = [pk]

        for pk in pklst:
            Comment.objects.get(pk=pk).delete()
        
        if request.is_ajax():
            return HttpResponse('ok');
        return HttpResponseRedirect(reverse("blog.views.post", args=[post_pk]))

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]
        comment = Comment(post=Post.objects.get(pk=pk))

        # save comment form
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False
        comment = cf.save(commit=False)

        # save comment instance
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))


def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, user=request.user, post_list=posts.object_list))

