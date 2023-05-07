from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts':allPosts}
    print(context)
     
    return render(request,'blog/bloghome.html',context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)