from django.shortcuts import render, get_object_or_404, redirect
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


@login_required
def post_edit(request, q_id):
    q_obj = get_object_or_404(Article, pk=q_id)
    form1 = ArticleForm(instance=q_obj)
    if request.method == 'POST':
        form1 = ArticleForm(request.POST, instance=q_obj)
        obj = form1.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('article')
    return render(request, 'post.html', {'form': form1})
