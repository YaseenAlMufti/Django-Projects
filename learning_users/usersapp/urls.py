from django.urls import path
from django.conf.urls import url, include
from usersapp import views

app_name = 'usersapp'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
