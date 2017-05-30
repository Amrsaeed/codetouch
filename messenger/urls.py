from django.conf.urls import url

from . import views

app_name = 'messenger'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webchat/$', views.webchat, name='webchat'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout')

]
