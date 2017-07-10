from django.conf.urls import url
from . import views

urlpatterns = [
    # Non management
    url(r'^myprograms/$',
        views.IndividualProgramListView.as_view(),
        name='myprograms_list'),
    url(r'^myprograms/(?P<pk>\d+)/$',
        views.IndividualProgramDetailView.as_view(),
        name='myprogram_detail'),
    url(r'^myprograms/new/$',
        views.IndividualPrequestAddView.as_view(),
        name='new_myprogram'),
    url(r'^myprequests/$',
        views.IndividualPrequestListView.as_view(),
        name='myprequests_list'),


    # Management
    url(r'^fields/$',
        views.FieldListView.as_view(),
        name='fields_list'),
    url(r'^fields/new/$',
        views.FieldAddView.as_view(),
        name='new_field'),
    url(r'^fields/(?P<pk>\d+)/edit/$',
        views.FieldUpdateView.as_view(),
        name='field_edit'),

    url(r'^prequests/$',
        views.PrequestListView.as_view(),
        name='prequests_list'),
    url(r'^prequests/new/$',
        views.PrequestAddView.as_view(),
        name='new_prequest'),
    url(r'^prequests/(?P<pk>\d+)/edit/$',
        views.PrequestUpdateView.as_view(),
        name='prequest_edit'),
    url(r'^prequests/(?P<pk>\d+)/delete/$',
        views.PrequestDeleteView.as_view(),
        name='prequest_delete'),

    url(r'^programs/$',
        views.ProgramListView.as_view(),
        name='programs_list'),
    url(r'^programs/new/$',
        views.ProgramAddView.as_view(),
        name='new_program'),
    url(r'^programs/(?P<pk>\d+)/edit/$',
        views.ProgramUpdateView.as_view(),
        name='program_edit'),
    url(r'^programs/(?P<id>\d+)/end/$',
        views.ProgramEndView.as_view(),
        name='program_end'),
]