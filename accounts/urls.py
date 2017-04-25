from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.profile_home, name='home'),


    # Management
    url(r'^users/$',
        views.UserListView.as_view(),
        name='users_list'),
    url(r'^users/(?P<pk>\d+)/edit/$',
           views.UserUpdateView.as_view(),
           name='user_edit'),
]