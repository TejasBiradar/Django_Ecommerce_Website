from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.


def index(request):

    allPosts = Blogpost.objects.all()
    posts = []
    for items in allPosts:
        posts.append(items)
    params = {"posts":posts}
    return render(request, "blog/index.html",params)


# def blogpost(request,id):

#     len_post = Blogpost.objects.all()
#     post = Blogpost.objects.filter(post_id = id)[0]
#     avl_ids = []
#     for ids in len_post:
#         avl_ids.append(ids.post_id)

#     avl_ids = avl_ids.sort()

#     current_index = avl_ids.index(post.post_id)

#     # Determine previous and next IDs
#     prev_id = avl_ids[current_index - 1] if current_index > 0 else avl_ids[0]
#     next_id = avl_ids[current_index + 1] if current_index < len(avl_ids) - 1 else avl_ids[-1]

#     # print(avl_ids)
#     # avl_ids = avl_ids.sort()

#     # prev_id = (post.post_id)-1
#     # next_id = (post.post_id)+1

#     # if(prev_id <=1):
#     #     prev_id = 1

#     # if(next_id >= len(len_post)):
#     #     next_id = len(len_post)

#     params = {"post": post, "prev_id": prev_id, "next_id": next_id}
#     return render(request, "blog/blogpost.html",params)

from django.shortcuts import render, get_object_or_404


def blogpost(request, id):
    # Get all posts and their IDs
    len_post = Blogpost.objects.all()
    avl_ids = [ids.post_id for ids in len_post]
    avl_ids.sort()

    # Get the current post or return a 404 if not found
    post = get_object_or_404(Blogpost, post_id=id)

    try:
        current_index = avl_ids.index(post.post_id)
    except ValueError:
        # Handle the case where the current post ID is not in the list (should not happen with get_object_or_404)
        current_index = None

    # Determine previous and next IDs
    prev_id = avl_ids[current_index - 1] if current_index > 0 else avl_ids[0]
    next_id = (
        avl_ids[current_index + 1] if current_index < len(avl_ids) - 1 else avl_ids[-1]
    )

    params = {"post": post, "prev_id": prev_id, "next_id": next_id}
    return render(request, "blog/blogpost.html", params)


def addpost(request):

    if request.method == "POST":
        title = request.POST.get("title",'')
        head0 = request.POST.get("head0", "")
        chead0 = request.POST.get("chead0", "")
        head1 = request.POST.get("head1", "")
        chead1 = request.POST.get("chead1", "")
        head2 = request.POST.get("head2", "")
        chead2 = request.POST.get("chead2", "")
        pub_date = request.POST.get("pub_date", "")
        thumbnail = request.POST.get("thumbnail", "")

        addpost = Blogpost(
            title=title,
            head0=head0,
            chead0=chead0,
            head1=head1,
            chead1=chead1,
            head2=head2,
            chead2=chead2,
            pub_date=pub_date,
            thumbnail=thumbnail,
        )
        addpost.save()
    return render(request, "blog/addpost.html")
