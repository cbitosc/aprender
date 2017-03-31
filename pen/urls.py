from django.conf.urls import url

from .views import view_article, post_article

urlpatterns = [
    url(r'^$', view_article, name='article'),
    url(r'^post/$', post_article, name='post_article'),

]
