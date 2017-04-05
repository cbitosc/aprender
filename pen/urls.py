from django.conf.urls import url

from .views import view_article, post_article, post_edit

urlpatterns = [
    url(r'^$', view_article, name='article'),
    url(r'^post/$', post_article, name='post_article'),
    url(r'^edit/(?P<q_id>[0-9]+)/$', post_edit, name='edit_article'),
]
