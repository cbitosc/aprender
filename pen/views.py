from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Article
from .forms import ArticleForm


@login_required
def view_article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles.html', context)


def post_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'post.html', context)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('/')
