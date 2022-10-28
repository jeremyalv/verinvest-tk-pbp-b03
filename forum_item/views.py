from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from collection.models import Post
from forum_item.models import ForumComment
from forum_item.forms import ForumForm

# @login_required
def view_post(request, id):
    pass

# ajax
@csrf_exempt
def create_post(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            post_type='forum',
            # TODO UNCOMMENT
            # author=request.user,
            title=title,
            content=content,
            upvotes=0,
            viewers=0,
            comments_count=0,
        )

        return HttpResponseRedirect(reverse('collection:forum'))
    else:
        form = ForumForm()
        
    context = {
        'form' : form,
    }

    return render(request, 'create_forum.html', context)

@csrf_exempt
def delete_post(request, id):
    post = Post.objects.get(id=id, author=request.user)
    post.delete()

    return HttpResponseRedirect(reverse('collection:forum'))


